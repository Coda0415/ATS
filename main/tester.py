import requests


def retrieve_contact_info(private_app_access_token, contact_id):
    headers = {
        'Authorization': f'Bearer {private_app_access_token}'
    }

    url = f'https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        contact_data = response.json()
        return contact_data
    else:
        print(f"Failed to retrieve contact information. Status code: {response.status_code}")
        return None

# Example usage
private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'

contact_info = retrieve_contact_info(private_app_access_token, contact_id)
if contact_info is not None:
    # Process the contact information
    print(contact_info)
