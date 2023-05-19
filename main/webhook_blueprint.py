import logging
from flask import Flask, request, render_template, Blueprint
import hubspot
from hubspot.crm.contacts import ApiException

webhook_blueprint = Blueprint('webhook', __name__)
private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'

# Create an instance of the API client
api_client = hubspot.Client.create_with_api_key(private_app_access_token)

@webhook_blueprint.route('/webhook/hubspot', methods=['POST'])
def webhook():
    try:
        payload = request.get_json()
        if isinstance(payload, list):
            # Handle a list of payloads
            if len(payload) > 0:
                contact_id = payload[0].get('objectId')
                # You can now use the contact_id variable in your further processing
                app.logger.info('Received payload. Contact ID: %s', contact_id)
        else:
            # Handle a single payload
            contact_id = payload.get('objectId')
            # You can now use the contact_id variable in your further processing
            app.logger.info('Received payload. Contact ID: %s', contact_id)
        return 'Success'
    except Exception as e:
        app.logger.error('Error processing webhook payload: %s', str(e))
        return 'Error', 500