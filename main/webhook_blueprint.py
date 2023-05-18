from flask import Flask, Blueprint, request, jsonify, render_template

webhook_blueprint = Blueprint('webhook', __name__)
webhook_log = []  # A list to store the webhook payloads

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
    return render_template('webhook_log.html')