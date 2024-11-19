import requests
from requests.auth import HTTPBasicAuth
import re
from project_config import email, subdomain, api_token

# API endpoint for Zendesk organizations
orgs_url = f"https://{subdomain}.zendesk.com/api/v2/organizations.json"

# Authentication setup using HTTPBasicAuth
auth = HTTPBasicAuth(f"{email}/token", api_token)

# Function to fetch all organizations
def fetch_organizations():
    organizations = []
    url = orgs_url
    while url:
        response = requests.get(url, headers={"Content-Type": "application/json"}, auth=auth)
        if response.status_code == 200:
            data = response.json()
            organizations.extend(data['organizations'])  # Add organizations from the current page
            # Check if there's another page of results
            url = data.get('next_page')  # Get the next page URL if exists
        else:
            print(f"Failed to fetch organizations: {response.status_code} {response.json()}")
            break
    return organizations

# Fetch organizations and print their names
def print_organization_names():
    organizations = fetch_organizations()
    if organizations:
        print("Organization Names:")
        for org in organizations:
            print(org['name'])
    else:
        print("No organizations found or failed to fetch data.")

# Run the function
print_organization_names()
