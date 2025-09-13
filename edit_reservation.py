import tkinter as tk
from tkinter import ttk, messagebox
import database

class EditReservationPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.reservation_id = None

        form_frame = ttk.Frame(self, padding="20 10")
        form_frame.pack(expand=True, fill="both")
        
        header = ttk.Label(form_frame, text="Edit Flight Reservation", font=("Helvetica", 18, "bold"))
        header.grid(row=0, column=0, columnspan=2, pady=20)

        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = {}
        for i, field in enumerate(fields):
            label = ttk.Label(form_frame, text=f"{field}:")
            label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Entry(form_frame, width=40)
            entry.grid(row=i + 1, column=1, padx=10, pady=5)
            self.entries[field.lower().replace(" ", "_")] = entry

        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=len(fields) + 1, column=0, columnspan=2, pady=20)

        update_button = ttk.Button(button_frame, text="Update Reservation", command=self.update_reservation, style="Accent.TButton")
        update_button.pack(side="left", padx=10)

        back_button = ttk.Button(button_frame, text="Back to List", command=lambda: controller.show_frame("ReservationListPage"))
        back_button.pack(side="left", padx=10)
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def populate_form(self, reservation_id):
        self.reservation_id = reservation_id
        reservation = database.get_reservation_by_id(self.reservation_id)
        
        if reservation:
            self.entries["name"].delete(0, tk.END)
            self.entries["name"].insert(0, reservation["name"])
            self.entries["flight_number"].delete(0, tk.END)
            self.entries["flight_number"].insert(0, reservation["flight_number"])
            self.entries["departure"].delete(0, tk.END)
            self.entries["departure"].insert(0, reservation["departure"])
            self.entries["destination"].delete(0, tk.END)
            self.entries["destination"].insert(0, reservation["destination"])
            self.entries["date"].delete(0, tk.END)
            self.entries["date"].insert(0, reservation["date"])
            self.entries["seat_number"].delete(0, tk.END)
            self.entries["seat_number"].insert(0, reservation["seat_number"])

    def update_reservation(self):
        if self.reservation_id is None:
            messagebox.showerror("Error", "No reservation selected for update.")
            return

        data = {key: entry.get() for key, entry in self.entries.items()}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required.")
            return
            
        try:
            database.update_reservation(self.reservation_id, **data)
            messagebox.showinfo("Success", "Reservation updated successfully!")
            self.controller.show_frame("ReservationListPage")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to update reservation: {e}")

    def on_show_frame(self, event):
        if self.controller.current_frame_data:
            self.populate_form(self.controller.current_frame_data)