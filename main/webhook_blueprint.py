from flask import Flask, Blueprint, request, jsonify, render_template
import requests

webhook_blueprint = Blueprint('webhook', __name__)
webhook_log = []  # A list to store the webhook payloads
portal_id = '9145139'
private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'

@webhook_blueprint.route('/webhook/hubspot', methods=['POST'])
def handle_hubspot_webhook():
    payload = request.json
    print('Received webhook payload:', payload)

    # Add the webhook payload to the log
    webhook_log.append(payload)

    return '', 200

@webhook_blueprint.route('/webhook/log', methods=['GET'])
def get_webhook_log():
    return jsonify(webhook_log)

@webhook_blueprint.route('/webhook')
def webhook():
    contacts = []
    for payload in webhook_log:
        if isinstance(payload, dict):
            contact_id = payload.get('objectId')
            if contact_id:
                contact_data = get_contact_info(private_app_access_token, contact_id)
                if contact_data:
                    contacts.append(contact_data)

    return render_template('webhook_log.html', contacts=contacts)


def get_contact_info(private_app_access_token, contact_id):
    headers = {
        'Authorization': f'Bearer {private_app_access_token}'
    }

    url = f'https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        contact_data = response.json()
        return contact_data
    else:
        print(f"Failed to retrieve contact information. Status code: {response.status_code}")
        return None

# Example usage
private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'
