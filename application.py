from flask import Flask, Response, request
from datetime import datetime
import json
from orderResource import Resource
from flask_cors import CORS

# Create the Flask application object.
application = Flask(__name__)

CORS(application)


@application.get("/")
def get_health():
    t = str(datetime.now())
    result = {
        "name": "Microservice-Orders",
        "health": "Good",
        "at time": t
    }

    return result

# Get the raw orders from frontend's json file
@application.route("/item", methods=["POST"])
def get_raw_order():

    order = request.get_json()
    result = Resource.addOrder(order)

    if result:
        return json.dumps(result), 200
    else:
        return "Fail to add raw order!", 500

# Get the transaction from matching engine's request
@application.route("/trade", methods=["POST"])
def add_matched_order():
    order_matched = request.get_json()
    result = Resource.updateOrder(order_matched)

    if result:
        return json.dumps(result), 200
    else:
        return "Fail to add matched order!", 500

# Post the resulting transaction to matching engine
@application.route("/trade", methods=["GET"])
def send_order():
    json_data = []
    active_orders = Resource.get_active_orders()
    for row in active_orders:
        result = {'order_id':row['order_id'], 'instrument':row['instrument'], 
                  'action':row['action'], 'price':row['price'], 'volume':row['volume']}
        json_data.append(result)
    if json_data==[]:
        return "no query found", 301
    else:
        return json.dumps(json_data)

# Post the resulting transaction to matching engine
@application.route("/history/<usr_id>", methods=["GET"])
def send_order_by_usr(usr_id):
    json_data = []
    usr_orders = Resource.get_order_by_user(usr_id)
    for row in usr_orders:
        result = {'order_id':row['order_id'], 'user_id':row['user_id'], 'instrument':row['instrument'],
                  'action':row['action'], 'price':row['price'], 'volume':row['volume'], 'remaining_volume':row['remaining_volume'],
                  'status':row['status']}
        json_data.append(result)
    if json_data==[]:
        return "no query found", 302
    else:
        return json.dumps(json_data)



if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000) #5011

