# frontend/terminal_interface.py
from utils.csv_parser import CSVParser
import os

class TerminalInterface:
    def __init__(self, flight_database):
        self.flight_database = flight_database

    def display_menu(self):
        print("1. List all flights")
        print("2. View a specific flight")
        print("3. Add a new flight")
        print("4. Update an existing flight")
        print("5. Delete a flight")
        print("6. Upload CSV data for a flight")
        print("Q. Quit")
        choice = input("Enter your choice: ")
        return choice

    def list_flights(self):
        flights = self.flight_database.get_flights()
        for flight in flights:
            print(flight)

    def view_flight(self, launch_id):
        flight = self.flight_database.get_flights('LaunchID', launch_id)
        print(flight)

    def add_flight(self):
        launch_id = input("Enter Launch ID: ")
        lv_name = input("Enter LV Name: ")
        payload = input("Enter Payload: ")
        phase = input("Enter Phase: ")
        destination = input("Enter Destination: ")
        manned = input("Is the flight Manned? (True/False): ")
        current_status = input("Enter Current Status: ")
        flight_recorder_data = input("Enter Flight Recorder Data: ")
        failures = input("Enter Failures: ")
        comments = input("Enter Comments: ")

        new_flight_data = (launch_id, lv_name, payload, phase, destination, bool(manned), current_status, flight_recorder_data, failures, comments)
        self.flight_database.insert_flight(new_flight_data)

    def update_flight(self, launch_id):
        existing_flight = self.flight_database.get_flights('LaunchID', launch_id)
        if not existing_flight:
            print("Flight not found.")
            return

        print("Enter new data (leave blank to keep existing data):")
        lv_name = input(f"Enter new LV Name (Current: {existing_flight[0][1]}): ") or existing_flight[0][1]
        payload = input(f"Enter new Payload (Current: {existing_flight[0][2]}): ") or existing_flight[0][2]
        phase = input(f"Enter new Phase (Current: {existing_flight[0][3]}): ") or existing_flight[0][3]
        destination = input(f"Enter new Destination (Current: {existing_flight[0][4]}): ") or existing_flight[0][4]
        manned = input(f"Is the flight Manned? (Current: {existing_flight[0][5]}): ") or existing_flight[0][5]
        current_status = input(f"Enter new Current Status (Current: {existing_flight[0][6]}): ") or existing_flight[0][6]
        flight_recorder_data = input(f"Enter new Flight Recorder Data (Current: {existing_flight[0][7]}): ") or existing_flight[0][7]
        failures = input(f"Enter new Failures (Current: {existing_flight[0][8]}): ") or existing_flight[0][8]
        comments = input(f"Enter new Comments (Current: {existing_flight[0][9]}): ") or existing_flight[0][9]

        updated_data = (lv_name, payload, phase, destination, bool(manned), current_status, flight_recorder_data, failures, comments)
        self.flight_database.update_flight(launch_id, updated_data)

    def delete_flight(self, launch_id):
        self.flight_database.delete_flight(launch_id)

    def upload_csv(self, launch_id):
        csv_file_path = input("Enter the path to the CSV file: ")
        parser = CSVParser(csv_file_path)
        headers, data = parser.parse()
        table_str = f"Headers: {headers}\nData: {data}"
        self.flight_database.update_flight(launch_id, flight_recorder_data=table_str)
        os.remove(csv_file_path)
