import sqlite3
import json

# Initialize SQLite database
conn = sqlite3.connect('db/form_data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS form_data (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  submission_date TEXT,
                  first_name TEXT,
                  last_name TEXT,
                  gender TEXT,
                  dob TEXT,
                  phone TEXT,
                  email TEXT,
                  registered_betting_site TEXT,
                  betting_sites TEXT,
                  residence_domicile_same TEXT,
                  address1 TEXT,
                  address2 TEXT,
                  city1 TEXT,
                  province1 TEXT,
                  postal_code1 TEXT,
                  country1 TEXT,
                  address3 TEXT,
                  address4 TEXT,
                  city2 TEXT,
                  province2 TEXT,
                  postal_code2 TEXT,
                  country2 TEXT,
                  id_front TEXT,
                  id_back TEXT,
                  health_card_front TEXT,
                  health_card_back TEXT)''')



# Read data from JSON file
with open('db/form_values.json', 'r') as f:
    form_values = json.load(f)
    



# Insert data into table
for row in form_values[1:]:  # Skip the header row
    cursor.execute('''INSERT INTO form_data (
                      submission_date, first_name, last_name, gender, dob, phone, email,
                      registered_betting_site, betting_sites, residence_domicile_same,
                      address1, address2, city1, province1, postal_code1, country1,
                      address3, address4, city2, province2, postal_code2, country2,
                      id_front, id_back, health_card_front, health_card_back)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data has been successfully inserted into the SQLite database.")