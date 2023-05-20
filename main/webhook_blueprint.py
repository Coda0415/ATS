from flask import Flask, Blueprint, request, jsonify, render_template
import requests
import json

webhook_blueprint = Blueprint('webhook', __name__)
webhook_log = []  # A list to store the webhook payloads

@webhook_blueprint.route('/webhook/hubspot', methods=['POST'])
def hubspot_webhook():
    data = json.loads(request.data)
    print(f"Received data: {data}")
    return jsonify({"status":"ok"}), 200