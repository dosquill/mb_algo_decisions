# Main file for the project
from client import Client 
from offer import Offer
from algorithm import *

client = Client(name="Pippo", surname="Caio", id=1, file_path="db/all_offers.json", budget=3000)
data = client_resolution(client, folder="results")