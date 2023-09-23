# Main file for the project
import sqlite3
from ..sql.save_sqlite import save_to_sqlite
from ...Class.client import Client
from ...Class.person import Person




def form_converter():
    db_path = "db/form/all_client.db"
    id_sheet = "1Fl8tSpBjKQt4yn2CFlC-i-Lg948PbtCksaRNQW4r9rw"
    nome_sheet = "risposte_form"
    range = "A:Z"

    save_to_sqlite(id_sheet, nome_sheet, range, db_path)




def fetch_all_data_from_form(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path) 
    cursor = conn.cursor()

    # Execute a query to fetch all data from the 'form' table
    cursor.execute("SELECT * FROM form")
    
    # Fetch all rows
    data = cursor.fetchall()

    # Close the connection
    conn.close()

    return data




def get_client(name, surname):
    conn = sqlite3.connect("db/form/data.db")
    c = conn.cursor()

    c.execute(f"SELECT * From risposte_form WHERE Nome = '{name}' AND Cognome = '{surname}")
    data = c.fetchall()

    conn.close()    

    return data



