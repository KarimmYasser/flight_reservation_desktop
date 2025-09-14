# Simple Flight Reservation Desktop App

This is a basic desktop application for managing flight reservations, built with Python, Tkinter for the GUI, and SQLite for the database.

## Features

- **Book Flights**: Add new reservations with passenger details.
- **View Reservations**: See all current bookings in a clear list.
- **Update Reservations**: Modify details of existing bookings.
- **Delete Reservations**: Remove bookings from the system.

## Tools and Libraries

- **Python 3**
- **Tkinter** (standard library)
- **SQLite 3** (standard library)
- **PyInstaller** (for creating the executable)

## Getting Started

### Prerequisites

- Python 3.6 or newer.

### Installation & Running the App

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/KarimmYasser/flight_reservation_desktop](https://github.com/KarimmYasser/flight_reservation_desktop)
    cd flight-reservation-app
    ```

2.  **Run the application:**
    No external libraries are required. Simply run the main script.
    ```bash
    python main.py
    ```
    The application window should appear. The `flights.db` database file will be created automatically in the project directory if it doesn't exist.

### Running the Executable

Navigate to the `dist/` folder and run the `main.exe` file. No installation is required.

## Building the Executable

To create your own standalone executable (`.exe`) for Windows:

1.  **Install PyInstaller:**

    ```bash
    pip install pyinstaller
    ```

2.  **Run the build command:**
    Open your terminal in the project's root directory and run the following command. The `--onefile` flag bundles everything into a single executable, and `--windowed` prevents a console window from appearing.

    ```bash
    pyinstaller --onefile --windowed --name="FlightReservations" main.py
    ```

    _Optional: To add a custom icon, use the `--icon` flag:_

    ```bash
    pyinstaller --onefile --windowed --name="FlightReservations" --icon="icon.ico" main.py
    ```

3.  **Find the executable:**
    The final `.exe` file will be located in the `dist` folder.
