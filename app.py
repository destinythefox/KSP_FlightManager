from flask import Flask, jsonify, request
from db.database import FlightDatabase

app = Flask(__name__)
db = FlightDatabase('KSP_FlightManager.db')

@app.route('/flights', methods=['GET'])
def get_flights():
    flights = db.get_flights()
    return jsonify(flights)

@app.route('/flights', methods=['POST'])
def add_flight():
    data = request.json
    db.insert_flight(data)
    return jsonify({"message": "Flight added"}), 201

@app.route('/flights/<string:launch_id>', methods=['GET'])
def get_single_flight(launch_id):
    flight = db.get_single_flight(launch_id)
    if flight:
        return jsonify(flight)
    else:
        return jsonify({"message": "Flight not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
