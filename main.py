# Main file for the project
from pprint import pprint
from Class.client import Client 
from func.clients_list_resolver import *
from func.offer_resolver import *
from func.step_resolver import *
from func.client_resolver import *
from utils.util import *


# testing main algorithm
#budget = 2192
budget = 3000
folder = "results"

# testing algorithm
clients = []


client1 = Client(name="Pippo", surname="Caio", id=1, file_path="db/Pippo.json")
client2 = Client(name="Pluto", surname="Caio", id=2, file_path="db/Pluto.json")
client3 = Client(name="Paperino", surname="Alessio", id=3, file_path="db/all_offers.json")


clients.append(client1)
clients.append(client2)
clients.append(client3)

data = clients_list_resolver(clients, budget, folder) 



