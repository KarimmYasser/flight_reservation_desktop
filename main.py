import tkinter as tk
from tkinter import ttk
from home import HomePage
from booking import BookingPage
from reservations import ReservationListPage
from edit_reservation import EditReservationPage


class FlightApp(tk.Tk):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    style = ttk.Style(self)
    self.tk.call("source", "azure.tcl")
    self.tk.call("set_theme", "light")
    style.configure("Accent.TButton", foreground="white")
    style.configure("Danger.TButton", foreground="#dc3545")
    style.configure("Icon.TButton", padding=0)
    self.configure(bg="#ffffff")

    self.title("Flight Reservation System")
    self.geometry("800x600")
    self.resizable(True, True)

    topbar = ttk.Frame(self)
    topbar.pack(side="top", fill="x")
    self.theme_mode = tk.StringVar(value="light")

    icon_box = ttk.Frame(topbar, width=50, height=50)
    icon_box.pack(side="right", padx=10, pady=6)
    icon_box.pack_propagate(False)

    self.theme_btn = ttk.Button(
      icon_box,
      text="🌙",
      style="Icon.TButton",
      command=self.toggle_theme,
    )
    self.theme_btn.pack(expand=True, fill="both")

    container = ttk.Frame(self)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.frames = {}
    self.current_frame_data = None

    for F in (HomePage, BookingPage, ReservationListPage, EditReservationPage):
      frame = F(parent=container, controller=self)
      self.frames[F.__name__] = frame
      frame.grid(row=0, column=0, sticky="nsew")

    self.show_frame("HomePage")

  def show_frame(self, page_name, data=None):
    self.current_frame_data = data
    frame = self.frames[page_name]
    frame.tkraise()
    frame.event_generate("<<ShowFrame>>")

  def toggle_theme(self):
    current = self.theme_mode.get()
    next_mode = "dark" if current == "light" else "light"
    self.tk.call("set_theme", next_mode)
    self.theme_mode.set(next_mode)
    if next_mode == "dark":
      self.theme_btn.configure(text="☀")
      self.configure(bg="#333333")
    else:
      self.theme_btn.configure(text="🌙")
      self.configure(bg="#ffffff")


if __name__ == "__main__":
    app = FlightApp()
    app.mainloop()
