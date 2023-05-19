import logging
from flask import Flask, request, render_template, Blueprint
import hubspot
from hubspot.crm.contacts import ApiException

webhook_blueprint = Blueprint('webhook', __name__)
private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'


# Create an instance of the API client
api_client = hubspot.Client(access_token=private_app_access_token)


@webhook_blueprint.route('/webhook/hubspot', methods=['POST', 'GET'])
def webhook():
    payload = request.json
    contact_id = payload['objectId']
    # You can now use the contact_id variable in your further processing
    print('Received payload. Contact ID:', contact_id)
    return 'Success'
