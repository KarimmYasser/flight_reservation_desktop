import tkinter as tk
from tkinter import ttk, messagebox
import database

class ReservationListPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        header = ttk.Label(self, text="All Flight Reservations", font=("Helvetica", 18, "bold"))
        header.pack(pady=20)

        columns = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Passenger Name")
        self.tree.heading("flight_number", text="Flight No.")
        self.tree.heading("departure", text="Departure")
        self.tree.heading("destination", text="Destination")
        self.tree.heading("date", text="Date")
        self.tree.heading("seat_number", text="Seat")

        self.tree.column("id", width=40, anchor="center")
        self.tree.column("name", width=150)
        self.tree.column("flight_number", width=80, anchor="center")
        self.tree.column("departure", width=120)
        self.tree.column("destination", width=120)
        self.tree.column("date", width=100, anchor="center")
        self.tree.column("seat_number", width=60, anchor="center")

        self.tree.pack(expand=True, fill="both", padx=20, pady=10)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10, fill="x", padx=20)

        edit_button = ttk.Button(button_frame, text="Edit Selected", command=self.edit_selected)
        edit_button.pack(side="left", padx=5)

        delete_button = ttk.Button(button_frame, text="Delete Selected", command=self.delete_selected, style="Danger.TButton")
        delete_button.pack(side="left", padx=5)

        back_button = ttk.Button(button_frame, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(side="right", padx=5)

        self.bind("<<ShowFrame>>", self.on_show_frame)

    def load_reservations(self):
        
        for item in self.tree.get_children():
            self.tree.delete(item)

        reservations = database.get_all_reservations()
        for reservation in reservations:
            self.tree.insert("", "end", values=tuple(reservation))

    def edit_selected(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a reservation to edit.")
            return

        item_values = self.tree.item(selected_item, "values")
        reservation_id = item_values[0]

        self.controller.show_frame("EditReservationPage", reservation_id)

    def delete_selected(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a reservation to delete.")
            return

        item_values = self.tree.item(selected_item, "values")
        reservation_id = item_values[0]

        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete reservation ID {reservation_id}?"):
            try:
                database.delete_reservation(reservation_id)
                messagebox.showinfo("Success", "Reservation deleted successfully.")
                self.load_reservations()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete reservation: {e}")

    def on_show_frame(self, event):
        self.load_reservations()