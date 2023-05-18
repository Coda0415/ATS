from flask import Flask, Blueprint, request

webhook_blueprint = Blueprint('webhook', __name__)
@webhook_blueprint.route('/webhook/hubspot', methods=['POST'])
def handle_hubspot_webhook():
    payload = request.json
    print('Received webhook payload:', payload)

    print(payload)

    return '', 200