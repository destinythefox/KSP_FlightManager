import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class FlightDatabase:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Flights (
                LaunchID TEXT PRIMARY KEY,
                LVName TEXT,
                Payload TEXT,
                Phase TEXT,
                Destination TEXT,
                Manned BOOLEAN,
                CurrentStatus TEXT,
                FlightRecorderData TEXT,
                Failures TEXT,
                Comments TEXT
            )
        ''')
        self.connection.commit()

    def insert_flight(self, data):
        self.cursor.execute('''
            INSERT INTO Flights (LaunchID, LVName, Payload, Phase, Destination, Manned, CurrentStatus, FlightRecorderData, Failures, Comments)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        self.connection.commit()


    def get_single_flight(self, launch_id):
        query = "SELECT * FROM Flights WHERE LaunchID = ?"
        self.cursor.execute(query, (launch_id,))
        return self.cursor.fetchone()

    def get_flights(self, criteria=None, value=None):
        if criteria and value:
            query = f"SELECT * FROM Flights WHERE {criteria} = ?"
            self.cursor.execute(query, (value,))
        else:
            query = "SELECT * FROM Flights"
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_flight(self, launch_id, updated_data=None, flight_recorder_data=None):
        if flight_recorder_data:
            query = '''
            UPDATE Flights
            SET FlightRecorderData = ?
            WHERE LaunchID = ?
            '''
            self.cursor.execute(query, (flight_recorder_data, launch_id))
        elif updated_data:
            query = '''
            UPDATE Flights
            SET LVName = ?, Payload = ?, Phase = ?, Destination = ?, Manned = ?, CurrentStatus = ?, FlightRecorderData = ?, Failures = ?, Comments = ?
            WHERE LaunchID = ?
            '''
            self.cursor.execute(query, (*updated_data, launch_id))
            self.connection.commit()

    def delete_flight(self, launch_id):
        query = "DELETE FROM Flights WHERE LaunchID = ?"
        self.cursor.execute(query, (launch_id,))
        self.connection.commit()

    def update_flight_recorder_data(self, launch_id, file_path):
        parser = CSVParser(file_path)
        headers, data = parser.parse()
        table_str = f"Headers: {headers}\nData: {data}"
        self.update_flight(launch_id, flight_recorder_data=table_str)

    def close(self):
        self.connection.close()
