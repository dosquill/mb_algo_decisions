import pytest
from client import Client
from algorithm import step_resolution, offer_resolution, client_resolution


@pytest.fixture
def client():
    offers_source = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client = Client(name=name, surname=surname, id=id, file_path=offers_source)
    return client


# TODO
def test_success(client):
    # dobbiamo assumere che il budget iniziale sia almeno uguale all'offerta con budget minimo

    client.budget = 3000
    
    data = client_resolution(client)
    assert data is not None

    # il profitto totale è uguale al profitto di tutte le offerte fatte

    # il budget totale è uguale al budget iniziale + il profitto totale
    # 
    # il numero di offerte fatte è uguale al numero di offerte totali
    
    # se il budget è maggiore o uguale alla somma di tutti i  la lunghezza delle offerte fatte è uguale alla lunghezza delle offerte totali


# TODO
def test_fails():
    pass