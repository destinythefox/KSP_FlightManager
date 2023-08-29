import tkinter as tk
from tkinter import ttk
from db.database import FlightDatabase

class RetroFlightManager:
    def __init__(self, master, flight_database):
        self.master = master
        self.flight_database = flight_database
        self.master.title("Retro Flight Manager")
        self.master.geometry("800x600")
        
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=1, fill="both")
        
        # Create frames for each tab
        self.view_flight_frame = ttk.Frame(self.notebook)
        
        # Add frames to notebook
        self.notebook.add(self.view_flight_frame, text="View Flight")
        
        # Populate View Flight Frame
        self.populate_view_flight_frame()

    def populate_view_flight_frame(self):
        ttk.Label(self.view_flight_frame, text="Enter Launch ID:").grid(row=0, column=0)
        self.launch_id_entry = ttk.Entry(self.view_flight_frame)
        self.launch_id_entry.grid(row=0, column=1)
        
        ttk.Button(self.view_flight_frame, text="View", command=self.view_flight).grid(row=0, column=2)

        self.info_labels = {}
        self.info_text = {}
        fields = ['LaunchID', 'LVName', 'Payload', 'Phase', 'Destination', 'Manned', 'CurrentStatus', 'Failures', 'Comments']
        
        for i, field in enumerate(fields):
            self.info_labels[field] = ttk.Label(self.view_flight_frame, text=f"{field}:")
            self.info_labels[field].grid(row=i+2, column=0, sticky="e")
            
            self.info_text[field] = ttk.Label(self.view_flight_frame, text="")
            self.info_text[field].grid(row=i+2, column=1, columnspan=2, sticky="w")

    def view_flight(self):
        launch_id = self.launch_id_entry.get()
        flight = self.flight_database.get_flights('LaunchID', launch_id)
        
        if not flight:
            print("Flight not found.")
            return

        for i, (key, label) in enumerate(self.info_labels.items()):
            label['text'] = f"{key}: {flight[0][i]}"

if __name__ == "__main__":
    root = tk.Tk()
    db = FlightDatabase('KSP_FlightManager.db')
    app = RetroFlightManager(root, db)
    root.mainloop()
