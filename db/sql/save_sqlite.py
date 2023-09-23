import sqlite3
from ..google_sheet.service import google_service


def create_table(cursor, table_name, columns):
    # Create a table with the provided columns, wrapping names in square brackets
    cursor.execute(f"CREATE TABLE IF NOT EXISTS [{table_name}] ({', '.join([f'[{col}]' for col in columns])})")


def insert_data(cursor, table_name, data):
    # Insert the provided data into the table
    placeholders = ', '.join(['?'] * len(data[0]))
    cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", data)


def save_to_sqlite(spreadsheet_id, sheet_name, cell_range, db_path):
    # Fetch data from Google Sheets
    result = google_service(spreadsheet_id, sheet_name, cell_range, return_values=True)
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Assuming the first row of the result contains column headers
    columns = result[0]
    data = result[1:]
    
    # Create table and insert data
    create_table(cursor, sheet_name, columns)
    insert_data(cursor, sheet_name, data)
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
