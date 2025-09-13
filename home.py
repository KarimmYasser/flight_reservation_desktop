import tkinter as tk
from tkinter import ttk

class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        content = ttk.Frame(self, padding=20)
        content.pack(expand=True, fill="both")

        header_label = ttk.Label(
            content,
            text="Flight Reservation System",
            font=("Helvetica", 24, "bold")
        )
        header_label.pack(pady=30)

        book_button = ttk.Button(
            content,
            text="Book a Flight",
            command=lambda: controller.show_frame("BookingPage"),
            width=25,
            style="Accent.TButton"
        )
        book_button.pack(pady=10)

        view_button = ttk.Button(
            content,
            text="View All Reservations",
            command=lambda: controller.show_frame("ReservationListPage"),
            width=25
        )
        view_button.pack(pady=10)
