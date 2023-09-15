# Main file for the project
from Class.client import Client 
from func.clients_resolver import *
from func.offer_resolver import *
from func.step_resolver import *
from func.clients_resolver import *
from utils.util import *


# testing main algorithm
budget = 2192
folder = "results"

# testing algorithm
clients = [
    Client(name="Pippo", surname="Caio", id=1, file_path="db/all_offers.json"),
    Client(name="Pluto", surname="Caio", id=2, file_path="db/all_offers.json")
]


data = clients_resolver(clients, budget, folder) 



