import tkinter as tk
from tkinter import ttk, messagebox
import database


class BookingPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        form_frame = ttk.Frame(self, padding="20 10")
        form_frame.pack(expand=True, fill="both")

        header = ttk.Label(form_frame, text="Book a New Flight", font=("Helvetica", 18, "bold"))
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

        submit_button = ttk.Button(button_frame, text="Submit Reservation", command=self.submit_reservation, style="Accent.TButton")
        submit_button.pack(side="left", padx=10)

        back_button = ttk.Button(button_frame, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(side="left", padx=10)

    def submit_reservation(self):
        data = {key: entry.get() for key, entry in self.entries.items()}

        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            database.add_reservation(**data)
            messagebox.showinfo("Success", "Reservation added successfully!")
            self.clear_form()
            self.controller.show_frame("ReservationListPage")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to add reservation: {e}")

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)