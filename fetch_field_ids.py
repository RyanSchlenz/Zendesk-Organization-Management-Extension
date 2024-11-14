import requests
from requests.auth import HTTPBasicAuth
import re
from project_config import email, subdomain, api_token


# Authentication setup using HTTPBasicAuth
auth = HTTPBasicAuth(f"{email}/token", api_token)

# Headers for API requests
headers = {
    "Content-Type": "application/json"
}


# Fetch all organization fields and check their types
fields_url = f"https://{subdomain}.zendesk.com/api/v2/organization_fields.json"
response = requests.get(fields_url, headers=headers, auth=auth)

if response.status_code == 200:
    fields = response.json().get("organization_fields", [])
    for field in fields:
        print(f"Field ID: {field['id']}, Name: {field['title']}, Type: {field.get('type', 'Unknown')}")
else:
    print(f"Failed to fetch fields: {response.status_code}, {response.text}")


# Custom field ID for another field (e.g., 'Line of Business')
line_of_business_field_id = "12345"  # ID for 'Line of Business'

# Fetch options for 'Line of Business' field
options_url = f"https://{subdomain}.zendesk.com/api/v2/organization_fields/{line_of_business_field_id}/custom_field_options.json"
response = requests.get(options_url, headers=headers, auth=auth)

if response.status_code == 200:
    options = response.json().get("custom_field_options", [])
    if options:
        print("Dropdown options for 'Line of Business' field:")
        for option in options:
            print(f"Option ID: {option['id']}, Name: {option['name']}")
    else:
        print("No options found for 'Line of Business' field.")
else:
    print(f"Failed to fetch options for 'Line of Business': {response.status_code}, {response.text}")
