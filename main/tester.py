import requests

# Set up authentication
private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'
base_url = 'https://api.hubapi.com'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {private_app_access_token}'
}

# Retrieve last engagement for a contact
contact_id = '1580001'

# Retrieve all engagements for the contact
engagements_url = f'{base_url}/engagements/v1/engagements/associated/contact/{contact_id}/paged'

response = requests.get(engagements_url, headers=headers)
if response.status_code == 200:
    engagements = response.json().get('results', [])
    if engagements:
        last_engagement = engagements[1]
        engagement_type = last_engagement['engagement']['type']
        print(f"Last contact type: {engagement_type}")

        metadata = last_engagement.get('metadata', {})
        print("Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print("No engagements found for the contact.")
else:
    print("Failed to retrieve engagements.")