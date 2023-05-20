from flask import Flask, Blueprint, request, jsonify, render_template
import requests
import json

webhook_blueprint = Blueprint('webhook', __name__)
data_storage = {}

@webhook_blueprint.route('/webhook/hubspot', methods=['POST'])
def hubspot_webhook():
    global data_storage
    data = json.loads(request.data)
    object_id = data[0].get('objectId', None)  # extract the objectId from the first dictionary in the list
    data_storage = object_id
    print(f"Received object ID: {object_id}")
    return jsonify({"status":"ok"}), 200

@webhook_blueprint.route('/webhook/data')
def display_data():
    return render_template('webhook_log.html', data=data_storage)
