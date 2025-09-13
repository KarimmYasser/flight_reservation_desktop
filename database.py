import sqlite3


def get_db_connection():
    conn = sqlite3.connect('flights.db')
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def add_reservation(name, flight_number, departure, destination, date, seat_number):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()


def get_all_reservations():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservations ORDER BY id DESC')
    reservations = cursor.fetchall()
    conn.close()
    return reservations


def get_reservation_by_id(reservation_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservations WHERE id = ?', (reservation_id,))
    reservation = cursor.fetchone()
    conn.close()
    return reservation


def update_reservation(reservation_id, name, flight_number, departure, destination, date, seat_number):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reservations
        SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
        WHERE id = ?
    ''', (name, flight_number, departure, destination, date, seat_number, reservation_id))
    conn.commit()
    conn.close()


def delete_reservation(reservation_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM reservations WHERE id = ?', (reservation_id,))
    conn.commit()
    conn.close()


create_table()