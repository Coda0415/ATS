from .models import applicants
from . import db
import requests
import hubspot
from pprint import pprint
from hubspot.crm.contacts import SimplePublicObjectInput, ApiException

def generate_applicant_id(position_id):
    # Count the number of existing applicants for the position
    num_applicants = applicants.query.filter_by(positionid=position_id).count()

    # Create the applicantid using the positionid and the number of applicants
    applicant_id = f"{position_id}.{num_applicants + 1}"
    return applicant_id


def update_hubspot_contact_property(hubspotcontactid, property_name, property_value):
        client = hubspot.Client.create(access_token="pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68")

        properties = {
            property_name : property_value,

        }
        simple_public_object_input = SimplePublicObjectInput(properties=properties)
        try:
            api_response = client.crm.contacts.basic_api.update(contact_id=hubspotcontactid,
                                                                simple_public_object_input=simple_public_object_input)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling basic_api->update: %s\n" % e)
