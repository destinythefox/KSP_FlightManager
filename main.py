from db.database import FlightDatabase
# from frontend.gui_interface import RetroFlightManager  # Import RetroFlightManager
# import tkinter as tk
import curses

def curses_main(stdscr):
    db = FlightDatabase('KSP_FlightManager.db')
    
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    
    menu_items = ["List Flights", "View Flight", "Exit"]
    current_item = 0
    
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Retro Flight Manager")
        
        for i, item in enumerate(menu_items):
            if i == current_item:
                stdscr.addstr(i + 2, 0, item, curses.A_REVERSE)
            else:
                stdscr.addstr(i + 2, 0, item)
        
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_item > 0:
            current_item -= 1
        elif key == curses.KEY_DOWN and current_item < len(menu_items) - 1:
            current_item += 1
        elif key == 10:  # Enter key
            if current_item == 0:
                flights = db.get_flights()
                stdscr.clear()
                stdscr.addstr(0, 0, "Listing Flights:")
                for i, flight in enumerate(flights):
                    stdscr.addstr(i + 1, 0, str(flight))
                stdscr.addstr(len(flights) + 2, 0, "Press any key to continue.")
                stdscr.getch()
            elif current_item == 1:
                stdscr.clear()
                stdscr.addstr(0, 0, "Enter Launch ID:")
                curses.echo()
                launch_id = stdscr.getstr().decode('utf-8')
                curses.noecho()
                flight = db.get_flights('LaunchID', launch_id)
                stdscr.clear()
                stdscr.addstr(0, 0, f"Details for Launch ID {launch_id}:")
                stdscr.addstr(1, 0, str(flight))
                stdscr.addstr(3, 0, "Press any key to continue.")
                stdscr.getch()
            elif current_item == 2:
                break

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

    # Close database connection
    db.close()

def main():
    # Initialize database connection
    db = FlightDatabase('KSP_FlightManager.db')
    
    # Initialize GUI interface
    # root = tk.Tk()
    # interface = RetroFlightManager(root, db)  # Pass the database object to the GUI
    
    # Start the Tkinter event loop
    # root.mainloop()

    # Close database connection
    db.close()

if __name__ == "__main__":
    # main()
    curses.wrapper(curses_main)
