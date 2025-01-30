import sqlite3
from fonction import Employee

def create_database(db_name='employees.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            monthly_salary REAL NOT NULL,
            is_commercial BOOLEAN NOT NULL
        )
    ''')
    
    conn.commit()
    return conn

def insert_employee(conn, employee):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (first_name, last_name, monthly_salary, is_commercial)
        VALUES (?, ?, ?, ?)
    ''', (employee.first_name, employee.last_name, employee.monthly_salary, employee.is_commercial))
    
    conn.commit()

def save_employees_to_db(factory, db_name='employees.db'):
    conn = create_database(db_name)
    for emp in factory.employees:
        insert_employee(conn, emp)
    
    conn.close()
    print("Les employés ont été enregistrés dans la base de données.")
