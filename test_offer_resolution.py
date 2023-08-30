import pytest
from offer import Offer
from client import Client
from algorithm import offer_resolution

@pytest.fixture
def offer():
    return Offer('test', 100, 1000, 1)

@pytest.fixture
def client():
    all_offer = "db/all_offers.json"
    return Client('Pippo', 'Caio', 1, file_path=all_offer)


def test_offer_resolution(offer, client):
    client.budget = 3000
    folder = "results"

    step_1 = offer_resolution(client, offer, folder)
    step_2 = offer_resolution(client, offer, folder)

    assert step_1['initial_budget'] > step_2['initial_budget']




