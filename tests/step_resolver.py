import pytest
import copy
from Class.client import Client
from func.step_resolver import *



@pytest.fixture
def client():
    offers_source = "db/all_offers.json"
    name = "Pippo"
    id = 1
    surname = "Caio"
    client = Client(name=name, surname=surname, id=id, file_path=offers_source)
    return client





# SINGLE TEST
# success
def test_step_success(client):
    client.budget = 3000
    initial_budget = client.budget
    step_num = 1

    # asserzioni prima di fare l'offerta
    assert client.profit == 0                                                                                            # cliente appena stato inizializzato
    assert len(client.completed_offers) == 0                                                                        # nessuna offerta completata
    assert len(client.remaining_offers) > 0                                                                             # ci sono offerte da fare

    # risoluzione offerta
    data = step_resolver(client, step_num=step_num)
    assert data is not None                                                                                             # almeno uno step è stato completato

    assert data['step_num'] == 1
    assert data['step_profit'] == client.profit                                                                          # il contatore è uguale al primo step
    assert data['num_completed_offers'] == len(client.completed_offers)
    assert data['initial_budget'] == initial_budget
    assert data['remaining_budget'] == initial_budget - sum(offer.budget_needed for offer in client.completed_offers)   # il budget rimanente è la somma dei budget delle offerte che hai fatto
    assert data['completed_offers'] == [offer.name for offer in client.completed_offers]                                        # le offerte completate sono il nome di tutte le offerte fatte


def test_no_offers_failures(client):
    # caso 1: non ci sono offerte
    client.remaining_offers = []
    assert step_resolver(client) == None


def test_no_budget_failure(client):
    # TODO non è corretto
    # caso 2: non ci sono abbastanza soldi
    client.budget = 0
    assert step_resolver(client, step_num=1) == None





# TODO
def test_one_client_runs_out_of_budget():
    pass





# TODO
def test_one_client_complete_all_offer():
    pass




# MULTIPLE TESTS
# success
# test continuità dei dati
def test_2step_success(client):
    total_budget_all_offers = sum(offer.budget_needed for offer in client.remaining_offers)
    initial_budget = client.budget = 3000
    
    # asserzioni prima di fare l'offerta
    # ammesso che non è possibile completare tutte le offerte in un singolo step
    assert client.budget < total_budget_all_offers


    # ammesso che sia possibile completare almeno due step
    # presa una lista, la somma del budget necessario deve essere uguale almeno alla somma delle minori due
    assert len(client.remaining_offers) >= 2 
    copia_lista = copy.deepcopy(client.remaining_offers)   
    copia_lista.sort(key=lambda x: x.budget_needed, reverse=False)                                           # ordina per budget necessario
    assert client.budget >= sum(offer.budget_needed for offer in copia_lista[:2])                           # vengono estratti i primi due valori della lista ordinata


    # risoluzione offerta 1
    data1 = step_resolver(client, step_num=1)
    assert data1 is not None  
    assert data1['num_completed_offers'] >= 1
    assert data1['initial_budget'] == initial_budget


    # risoluzione offerta 2
    # assumiamo che abbiamo ancora offerte da fare
    assert len(client.remaining_offers) > 0
    data2 = step_resolver(client, step_num=2)
    assert data2 is not None
    assert data2['num_completed_offers'] >= 1


    # allora
    assert data1['step_num'] < data2['step_num']
    assert client.profit == data2['step_profit'] + data1['step_profit']
    assert data2['initial_budget'] > data1['initial_budget']


# TODO
# failure
def test_2step_failures(client):
    pass


    


