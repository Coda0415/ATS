import hubspot
from hubspot.crm.contacts import ApiException

private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'



# Create an instance of the API client
api_client = hubspot.Client(access_token=private_app_access_token)

try:
    # Fetch the contact by ID
    contact_fetched = api_client.crm.contacts.basic_api.get_by_id('1580051', properties=["firstname", "lastname", "phone", "appstatus","best_way_to_contact_you_","drugtestresult","hs_marketable_reason_id"])
    print(contact_fetched)
except ApiException as e:
    print("Exception when requesting contact by ID: %s\n" % e)
