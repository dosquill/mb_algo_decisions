import pytest
from Class.client import Client
from func.clients_list_resolver import *


@pytest.fixture
def clients():
    clients = []
    client1 = Client(name="Pippo", surname="Caio", id=1, file_path="db/Pippo.json")
    client2 = Client(name="Pluto", surname="Caio", id=2, file_path="db/Pluto.json")
    client3 = Client(name="Paperino", surname="Alessio", id=3, file_path="db/all_offers.json")

    clients.append(client1)
    clients.append(client2)
    clients.append(client3)

    return clients

def test_success(clients):
    pass    
    






