import pytest
from Class.offer import Offer
from Class.client import Client
from Class.budget_manager import BudgetManager
from func.offer_resolver import *


@pytest.fixture
def offer():
    # metti valori reali
    name = "Bwin"           
    profit = 8.5
    budget_needed = 50
    time_needed = 1
    return Offer(name=name, budget_needed=budget_needed, profit=profit, time_needed=time_needed)


@pytest.fixture
def client_list():
    client_list = []
    
    all_offer = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client_list.append(Client(name, surname, id, all_offer))

    return client_list


@pytest.fixture
def budget_manager(client_list):
    budget = 1000
    return BudgetManager(budget, client_list)


# single offer resolution
def test_offer_resolver(client_list, offer, budget_manager):
    client = client_list[0]

    # asserzioni iniziali
    assert client.budget >= 0
    assert client.budget >= offer.budget_needed
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
def test_2offer_resolver(offer, client):
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


def test_fails_no_bm(offer, cliet_list):
    
    pass



# quando deve fallire
def test_fails_budget_insufficient(offer, client_list):
    client.budget = 100
    offer.budget_needed = 1000

    assert client.budget < offer.budget_needed
    assert offer_resolver(client, offer) == None


# quando deve fallire
def test_fails_offer_already_done(offer, client):
    client.completed_offers.append(offer)

    assert offer in client.completed_offers
    assert offer_resolver(client, offer) == None



