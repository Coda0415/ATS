from .models import applicants
from . import db
import requests

def generate_applicant_id(position_id):
    # Count the number of existing applicants for the position
    num_applicants = applicants.query.filter_by(positionid=position_id).count()

    # Create the applicantid using the positionid and the number of applicants
    applicant_id = f"{position_id}.{num_applicants + 1}"
    return applicant_id


def update_hubspot_contact_property(hubspotcontactid, property_name, property_value):
    print(hubspotcontactid)
    private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'
    endpoint = f'https://api.hubapi.com/contacts/v1/contact/vid/{hubspotcontactid}/profile'
    headers = {'Content-Type': 'application/json'}
    data = {'properties': [{ 'property': property_name, 'value': property_value }]}
    params = {'hapikey': private_app_access_token}

    response = requests.post(endpoint, json=data, headers=headers, params=params)
    if response.status_code == 200:
        # Property updated successfully
        print('HubSpot contact property updated')
    else:
        # Error occurred while updating the property
        print('Failed to update HubSpot contact property:', response.text)