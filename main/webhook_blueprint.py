from flask import Blueprint, request, jsonify, render_template
import json
import hubspot
from hubspot.crm.contacts import ApiException

webhook_blueprint = Blueprint('webhook', __name__)
private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'

# Create an instance of the API client
api_client = hubspot.Client(access_token=private_app_access_token)

contact_fetched = {}

@webhook_blueprint.route('/webhook/hubspot', methods=['POST'])
def hubspot_webhook():
    data = json.loads(request.data)
    contact_id = data[0].get('objectId', None)  # extract the objectId from the first dictionary in the list
    print(f"Received object ID: {contact_id}")
    global contact_fetched
    contact_fetched = fetch_contact(contact_id)
    return jsonify({"status":"ok"}), 200

def fetch_contact(contact_id):
    try:
        # Fetch the contact by ID
        contact = api_client.crm.contacts.basic_api.get_by_id(contact_id, properties=["firstname", "lastname", "phone", "appstatus","best_way_to_contact_you_","drugtestresult","hs_marketable_reason_id"])
        print(contact)
        return contact
    except ApiException as e:
        print("Exception when requesting contact by ID: %s\n" % e)
        return {}

@webhook_blueprint.route('/webhook/data')
def display_data():
    global contact_fetched
    return render_template('webhook_log.html', data=contact_fetched)
