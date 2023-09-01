# Main file for the project
from client import Client 
from algorithm import *

# testing main algorithm
budget = 5000
folder = "results"
""" clients = []


client1 = Client(name="Pippo", surname="Caio", id=1, file_path="db/all_offers.json")
client2 = Client(name="Pluto", surname="Caio", id=2, file_path="db/all_offers.json")

clients.append(client1)
clients.append(client2)

data = algorithm(clients, budget) """

client = Client(name="Pippo", surname="Caio", id=1, budget=budget, file_path="db/all_offers.json")
data = client_resolution(client, folder)