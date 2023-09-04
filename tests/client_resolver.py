import pytest
from Class.client import Client
from func.client_resolver import *


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
    # c'è almeno un offerta che si può fare
    assert len(client.remaining_offers) > 0

    # se c'è un offerta che si può fare dobbiamo assumere che il budget iniziale sia almeno uguale all'offerta con budget minimo
    if len(client.remaining_offers) == 1:
        min_offert_budget = client.remaining_offers[0].budget_needed
    else:
        min_offert_budget = min([offer.budget_needed for offer in client.remaining_offers])
    client.budget = min_offert_budget


    # allora la funzione può essere eseguita correttamente
    data = client_resolver(client)
    assert data is not None


    # il profitto totale è uguale al profitto di tutte le offerte fatte
    # e il numero di offerte fatte è uguale alla lunghezza della lista delle offerte fatte
    total_profit = 0
    offer_counter = 0
    for p in client.completed_offers:
        total_profit += p.profit
        offer_counter += 1

    assert offer_counter == len(client.completed_offers)
    assert total_profit == client.profit


    # il budget totale è uguale al budget iniziale + il profitto totale
    assert client.budget == data['initial_budget'] + data['total_profit']
    
    



def test_no_offer_fail(client):
    client.remaining_offers = []
    assert client_resolver(client) is None




def test_no_budget_fail(client):
    # se c'è un offerta che si può fare dobbiamo assumere che il budget iniziale sia almeno uguale all'offerta con budget minimo
    assert len(client.remaining_offers) > 0
    
    min_offer_budget = min([offer.budget_needed for offer in client.remaining_offers])
    client.budget = min_offer_budget -1
    
    client_resolver(client) is None
