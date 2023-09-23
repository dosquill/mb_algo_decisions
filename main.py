# Main file for the project
from Class.client import Client 
from func.clients_resolver import *
from func.offer_resolver import *
from func.step_resolver import *
from func.clients_resolver import *
from utils.util import *


from db.form.converter import form_converter
from db.offer.converter import offer_converter

import sqlite3


# form_converter()
offer_converter()


""" conn = sqlite3.connect("db/form/data.db")
cursor = conn.cursor()

query = "SELECT * FROM risposte_form"
cursor.execute(query)
result = cursor.fetchall()
print(result)

conn.close()
 """

