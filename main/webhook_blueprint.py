import logging
from flask import Flask, request, render_template, Blueprint
import hubspot
from hubspot.crm.contacts import ApiException

webhook_blueprint = Blueprint('webhook', __name__)
private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'


# Create an instance of the API client
api_client = hubspot.Client(access_token=private_app_access_token)


@webhook_blueprint.route('/webhook/hubspot', methods=['POST'])
def handle_hubspot_webhook():
    payload = request.json
    logging.debug('Received webhook payload: %s', payload)

    if isinstance(payload, dict):
        # Extract the contact ID from the payload
        contact_id = payload.get('objectId')

        try:
            # Fetch the contact by ID
            contact_fetched = api_client.crm.contacts.basic_api.get_by_id(contact_id,
                                                                          properties=["firstname", "lastname", "phone",
                                                                                      "appstatus",
                                                                                      "best_way_to_contact_you_",
                                                                                      "drugtestresult",
                                                                                      "hs_marketable_reason_id"])

            # Render the HTML template with contact information
            return render_template('webhook_log.html', contact=contact_fetched)

        except ApiException as e:
            print("Exception when requesting contact by ID: %s\n" % e)
    else:
        print("Invalid payload format")

    return '', 200
