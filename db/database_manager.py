import sqlite3

def initialize_db():
    conn = sqlite3.connect('db/form_data.db')
    cursor = conn.cursor()

    # Create table

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS clients (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      email TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS offers (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      client_id INTEGER,
                      amount REAL,
                      FOREIGN KEY(client_id) REFERENCES clients(id))''')

    conn.commit()
    conn.close()



# CRUD operations
# Add a new client
def add_client(name, email):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()



# Get all clients
def get_clients():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    conn.close()
    return clients



# Add a new offer
def add_offer(client_id, amount):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO offers (client_id, amount) VALUES (?, ?)", (client_id, amount))
    conn.commit()
    conn.close()



# Get all offers for a client
def get_offers(client_id):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM offers WHERE client_id = ?", (client_id,))
    offers = cursor.fetchall()
    conn.close()
    return offers



if __name__ == '__main__':
    # Initialize the database
    initialize_db()

    # Add a client
    add_client('John Doe', 'john@example.com')

    # Get and print all clients
    clients = get_clients()
    print("Clients:", clients)

    # Add an offer for a client
    add_offer(1, 100.50)

    # Get and print all offers for a client
    offers = get_offers(1)
    print("Offers:", offers)