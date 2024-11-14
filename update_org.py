import requests
from requests.auth import HTTPBasicAuth
import re
from project_config import email, subdomain, api_token

# List of company email domains
domain1_domains = []
domain2_domains = []

# Define the domain-to-business-type mapping dynamically for both domain1 and domain2 organizations
domain_to_business_type = {
    **{domain: "domain1" for domain in domain1_domains},  # Mapping domain1 to 'domain1'
    **{domain: "domain2" for domain in domain2_domains}         # Mapping domain2 to 'domain2'
}

# API endpoint for Zendesk organizations
orgs_url = f"https://{subdomain}.zendesk.com/api/v2/organizations.json"

# Authentication setup using HTTPBasicAuth
auth = HTTPBasicAuth(f"{email}/token", api_token)

# Headers for API requests
headers = {
    "Content-Type": "application/json"
}

# Custom field ID for Business Type (Make sure this corresponds to your actual field ID)
business_type_field_id = 123456  # This is the ID for the "Business Type" custom field

def get_domain_from_email(email):
    """Extract the domain from an email address."""
    match = re.search(r'@([a-zA-Z0-9.-]+)', email)
    if match:
        return match.group(1)
    return None

def update_business_type(org_id, business_type_value):
    """Update the organization with the determined business type."""
    url = f"https://{subdomain}.zendesk.com/api/v2/organizations/{org_id}.json"
    data = {
        "organization": {
            "organization_fields": {  # Corrected this part to reflect the right format
                "business_type": business_type_value  # The custom field name ("business_type") with the selected value
            }
        }
    }
    response = requests.put(url, headers=headers, auth=auth, json=data)
    if response.status_code == 200:
        print(f"Successfully updated organization {org_id} with business type '{business_type_value}'")
    else:
        print(f"Failed to update organization {org_id}: {response.status_code} {response.json()}")

def categorize_organizations():
    page_url = orgs_url  # Start with the first page URL

    while page_url:  # Loop until there are no more pages
        response = requests.get(page_url, headers=headers, auth=auth)
        if response.status_code == 200:
            response_json = response.json()
            print("Organizations fetched successfully:")
            organizations = response_json.get("organizations", [])

            for org in organizations:
                org_name = org['name']
                org_id = org['id']
                org_domain_names = org.get('domain_names', [])  # Extract the domain names (if available)
                
                # Print the organization name and domain names
                print(f"\nOrganization: {org_name} (ID: {org_id})")
                print(f"Extracted domain names: {org_domain_names}")

                # Iterate through each domain name
                for domain in org_domain_names:
                    # Print the domain being checked
                    print(f"Checking domain: {domain}")

                    # Match based on the domain
                    if domain in domain_to_business_type:
                        business_type = domain_to_business_type[domain]
                        print(f"Domain '{domain}' matched with business type: {business_type}")
                        update_business_type(org_id, business_type)
                        break  # Stop checking other domains once we find a match
                    else:
                        print(f"Domain '{domain}' for organization '{org_name}' not found in mapping.")
                
                if not org_domain_names:  # If no domain names exist
                    print(f"No valid domains found for organization '{org_name}'")

            # Check for the next page
            page_url = response_json.get('next_page')  # If there's a next page, this will be the URL for it
        else:
            print(f"Failed to fetch organizations: {response.status_code} {response.json()}")
            break  # Exit the loop if the request fails

# Call the function to categorize organizations
categorize_organizations()
