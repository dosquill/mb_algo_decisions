import pytest
from Class.offer import Offer
from Class.client import Client
from func.offer_resolver import *


@pytest.fixture
def offer():
    name = "test"
    profit = 100
    budget_needed = 1000
    time_needed = 1
    return Offer(name=name, budget_needed=budget_needed, profit=profit, time_needed=time_needed)

@pytest.fixture
def client():
    all_offer = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    return Client(name=name, surname=surname, id=id, file_path=all_offer)



# single offer resolution
def test_offer_resolution(offer, client):
    offer.budget_needed = 100
    client.budget = 1000

    # asserzioni iniziali
    assert client.budget >= offer.budget_needed
    assert client.budget >= 0
    assert offer.budget_needed >= 0
    assert offer not in client.completed_offers   # l'offerta non è già presente nella lista di offerte completate del cliente

    # conclusione
    data = offer_resolver(client, offer)
    assert data is not None
    assert isinstance(data, dict)
    assert data['initial_budget'] == data['remaining_budget'] + data['budget_needed']
    assert data['total_profit'] == client.profit
    assert offer in client.completed_offers    # adesso è nelle offerte completate
    




# test di integrità dei dati tra due funzioni di risoluzione una dopo l'altra
def test_2offer_resolution(offer, client):
    offer2 = Offer(name='test2', profit=100, budget_needed=1000, time_needed=1)
    client.budget = offer.budget_needed + offer2.budget_needed

    data_1 = offer_resolver(client, offer)
    assert data_1 is not None
    counter_1 = len(client.completed_offers)

    data_2 = offer_resolver(client, offer2)
    assert data_2 is not None
    counter_2 = len(client.completed_offers)

    assert data_1['initial_budget'] > data_2['initial_budget']
    assert data_1['total_profit'] < data_2['total_profit']
    assert data_1['remaining_budget'] > data_2['remaining_budget']
    assert counter_1 < counter_2



# quando deve fallire
def test_fails_budget_insufficient(offer, client):
    client.budget = 100
    offer.budget_needed = 1000

    assert client.budget < offer.budget_needed
    assert offer_resolver(client, offer) == None


# quando deve fallire
def test_fails_offer_already_done(offer, client):
    client.completed_offers.append(offer)

    assert offer in client.completed_offers
    assert offer_resolver(client, offer) == None



