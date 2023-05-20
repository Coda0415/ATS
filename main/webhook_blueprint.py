from flask import Flask, Blueprint, request, jsonify, render_template
import requests
import json

webhook_blueprint = Blueprint('webhook', __name__)
data_storage = {}

@webhook_blueprint.route('/webhook/hubspot', methods=['POST'])
def hubspot_webhook():
    global data_storage
    data_storage = json.loads(request.data)
    print(f"Received data: {data_storage}")
    return jsonify({"status":"ok"}), 200

@webhook_blueprint.route('/webhook/data')
def display_data():
    return render_template('webhook_log.html', data=data_storage)
