from flask import Flask, jsonify, request
from db.database import FlightDatabase
import random

app = Flask(__name__)
db = FlightDatabase('KSP_FlightManager.db')

def generate_launch_id():
    return f"UKSA-{random.randint(1000, 9999)}"

@app.route('/get_flights', methods=['GET'])
def get_flights():
    flights = db.get_flights()
    return jsonify(flights=flights)

@app.route('/insert_flight', methods=['POST'])
def insert_flight():
    launch_id = generate_launch_id()
    lv_name = request.json.get('lv_name', '')
    payload = request.json.get('payload', '')
    phase = request.json.get('phase', '')
    destination = request.json.get('destination', '')
    manned = request.json.get('manned', False)
    current_status = request.json.get('current_status', '')
    flight_recorder_data = request.json.get('flight_recorder_data', '')
    failures = request.json.get('failures', '')
    comments = request.json.get('comments', '')

    db.insert_flight((launch_id, lv_name, payload, phase, destination, manned, current_status, flight_recorder_data, failures, comments))
    return jsonify(status='success', launch_id=launch_id)

@app.route('/get_single_flight/<string:launch_id>', methods=['GET'])
def get_single_flight(launch_id):
    flight = db.get_single_flight(launch_id)
    if flight:
        return jsonify(flight=flight)
    else:
        return jsonify(error='Flight not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
