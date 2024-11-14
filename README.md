# Zendesk-Organization-Management-Extension
This extension is designed for managing Zendesk organization data by categorizing organizations based on their email domains and updating specific organization fields. It comprises three scripts that retrieve organization data, fetch field information, and update organization data based on domain mappings. 

**Prerequisites**

Python 3.7+
Zendesk API Access: API token and account with permissions to manage organizations.

**Setup**

Clone or download the repository.
Create a project_config.py file and define the following variables:

email = 'your_email'            # Zendesk account email

subdomain = 'your_subdomain'     # Zendesk subdomain

api_token = 'your_api_token'     # Zendesk API token


**Install dependencies:**

pip install -r requirements.txt

**Requirements**

Only the requests library is necessary for this extension:
requests==2.32.3

**Workflow**

1. Fetch Organization Names (org_names.py)
   
The first script retrieves all organizations in the Zendesk tenant and prints their names. This helps confirm access and identify organizations currently present in your Zendesk environment.

org_names.py
Main function: print_organization_names()
Description: Prints all organization names to the console.
Purpose: Verify that the Zendesk API is correctly set up and lists current organization names.


2. Fetch Organization Field IDs (fetch_field_ids.py)
   
To make targeted updates, this script retrieves all available custom fields for organizations and displays their IDs and types. This step allows you to identify the field ID for the “Business Type” field or any other fields you plan to update.

fetch_field_ids.py
Fetches: Custom fields and options for the organization field.
Purpose: Identify the field ID for specific organization fields to use in updates.


3. Update Organization Field (update_org.py)
   
This script categorizes organizations by matching their email domains to predefined types (domain1 or domain2). Once matched, it updates the “Business Type” field for each organization based on the corresponding field ID.

update_org.py
Domain Mappings: Customize domain1_domains and domain2_domains lists in update_org.py with your specific domains.
Functionality:
Domain Mapping: Maps email domains to business types.
Update Field: Updates the “Business Type” field with the corresponding category.

Main function: categorize_organizations()
Description: Iterates through organizations, matches domains, and updates fields with appropriate business type values.


**Configuration**

In update_org.py:

Add domains for domain1_domains and domain2_domains.
Set business_type_field_id to the ID of the “Business Type” custom field (found in Step 2).

**Usage**

Run each script in sequence to fetch organization names, retrieve field IDs, and finally, update organization fields as needed.
