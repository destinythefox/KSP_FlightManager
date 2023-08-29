from db.database import FlightDatabase
import random  # Import for generating Launch ID

def generate_launch_id():
    return f"UKSA-{random.randint(1000, 9999)}"

def main():
    db = FlightDatabase('KSP_FlightManager.db')
    
    # Your backend logic here
    # For example, you can call db.get_flights() to get a list of flights
    # Or call db.insert_flight(data) to insert a new flight

    # Close the database connection when done
    db.close()

if __name__ == "__main__":
    main()
from db.database import FlightDatabase
import random  # Import for generating Launch ID

def generate_launch_id():
    return f"UKSA-{random.randint(1000, 9999)}"

def main():
    db = FlightDatabase('KSP_FlightManager.db')
    
    # Your backend logic here
    # For example, you can call db.get_flights() to get a list of flights
    # Or call db.insert_flight(data) to insert a new flight

    # Close the database connection when done
    db.close()

if __name__ == "__main__":
    main()
