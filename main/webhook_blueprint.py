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
    contact_id = data[0].get('objectId', None)  # extract the objectId from the first dictionary in the list
    propertyname = data[0].get('propertyName', None)
    if propertyname == "appstatus":
        appstatus = data[0].get('propertyValue', None)
    print(f"Received object ID: {contact_id}")
    global contact_fetched
    contact_fetched = fetch_contact(contact_id, db, appstatus)
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
