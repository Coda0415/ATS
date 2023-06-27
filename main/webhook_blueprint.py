from flask import Blueprint, request, jsonify, render_template, current_app
import json
import hubspot
from hubspot.crm.contacts import ApiException
from .models import applicants
from . import db

webhook_blueprint = Blueprint('webhook', __name__)
private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'

# Create an instance of the API client
api_client = hubspot.Client(access_token=private_app_access_token)

contact_fetched = {}

@webhook_blueprint.route('/webhook/hubspot', methods=['POST'])
def hubspot_webhook():
    data = json.loads(request.data)
    event_type = data.get('subscriptionType', None)
    allowed_event_types = ["contact.propertyChange"]

    if event_type not in allowed_event_types:
        return jsonify({"status": "ignored"}), 200

    contact_id = data.get('objectId', None)
    property_name = data.get('propertyName', None)
    property_value = data.get('propertyValue', None)
    print(f"Received object ID: {contact_id}")

    global contact_fetched
    if property_name == "hire_eligibility":
        # Handle 'hire_eligibility' property
        # TODO: add the specific logic for 'hire_eligibility' here
        contact_fetched = fetch_contact(contact_id, db, property_value)
    elif property_name == "background_check_status":
        # Handle 'background_check_status' property
        # TODO: add the specific logic for 'background_check_status' here
        contact_fetched = fetch_contact(contact_id, db, property_value)
    elif property_name == "appstatus":
        # Handle 'background_check_status' property
        # TODO: add the specific logic for 'appstatus' here
        contact_fetched = fetch_contact(contact_id, db, property_value)
    else:
        return jsonify({"status": "ignored"}), 200

    return jsonify({"status":"ok"}), 200


def fetch_contact(contact_id, db, appstatus):
    try:
        # Fetch the contact by ID
        contact = api_client.crm.contacts.basic_api.get_by_id(contact_id, properties=["firstname", "lastname", "phone", "appstatus","best_way_to_contact_you_","drugtestresult","hs_marketable_reason_id"])
        contact_dict = contact.to_dict()
        print(contact_dict)

        # Extract firstname and lastname
        firstname = contact_dict.get('properties', {}).get('firstname', None)
        lastname = contact_dict.get('properties', {}).get('lastname', None)

        with current_app.app_context():
            # Search for the applicant in the database
            applicant = applicants.query.filter_by(firstname=firstname, lastname=lastname).first()
            if applicant:
                # If the applicant is found, update the hubspotcontactid field
                applicant.hubspotcontactid = contact_id
                applicant.applicantstatus = appstatus
                db.session.commit()
                print(f'Updated hubspotcontactid for {firstname} {lastname}')
            else:
                print(f'Applicant {firstname} {lastname} not found in the database')

        return contact_dict
    except ApiException as e:
        print("Exception when requesting contact by ID: %s\n" % e)
        return {}


@webhook_blueprint.route('/webhook/data')
def display_data():
    global contact_fetched
    firstname = contact_fetched.get('properties', {}).get('firstname', None)
    lastname = contact_fetched.get('properties', {}).get('lastname', None)
    appstatus = contact_fetched.get('properties', {}).get('appstatus',None)
    return render_template('webhook_log.html', firstname=firstname, lastname=lastname, appstatus=appstatus)


@webhook_blueprint.route('/webhook/applicant')
def webhook_applicant():
    # Get the request payload
    payload = request.json
    print(payload)
    return 'Webhook received successfully'
