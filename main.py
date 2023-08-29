from db.database import FlightDatabase
from frontend.terminal_interface import TerminalInterface
from utils.csv_parser import CSVParser
import os

def main():
    # Initialize database connection
    db = FlightDatabase('KSP_FlightManager.db')
    
    # Initialize terminal interface
    interface = TerminalInterface(db)

    while True:
        # Display the main menu and get user choice
        user_choice = interface.display_menu()

        if user_choice == '1':
            interface.list_flights()
        elif user_choice == '2':
            launch_id = input("Enter the Launch ID: ")
            interface.view_flight(launch_id)
        elif user_choice == '3':
            interface.add_flight()
        elif user_choice == '4':
            launch_id = input("Enter the Launch ID: ")
            interface.update_flight(launch_id)
        elif user_choice == '5':
            launch_id = input("Enter the Launch ID: ")
            interface.delete_flight(launch_id)
        elif user_choice == '6':
            launch_id = input("Enter the Launch ID: ")
            interface.upload_csv(launch_id)
        elif user_choice.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    # Close database connection
    db.close()

if __name__ == "__main__":
    main()
