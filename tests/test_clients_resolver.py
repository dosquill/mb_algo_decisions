import pytest
from Class.client import Client
from func.clients_resolver import *







# --------------------------------------------------------------- #
################ ONE CLIENT ################
# --------------------------------------------------------------- #

# FIXME
# test di minimo successo
def test_min_success():
    offers_source = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client = Client(name=name, surname=surname, id=id, file_path=offers_source)


    # c'è almeno un offerta che si può fare
    assert len(client.remaining_offers) > 0


    # se c'è un offerta che si può fare dobbiamo assumere che il budget iniziale sia almeno uguale all'offerta con budget minimo
    if len(client.remaining_offers) == 1:
        min_offert_budget = client.remaining_offers[0].budget_needed
    else:
        min_offert_budget = min([offer.budget_needed for offer in client.remaining_offers])


    # allora la funzione può essere eseguita correttamente
    data = clients_resolver([client], min_offert_budget)
    assert data is not None


    assert data['final_data']['num_steps'] == 1
    assert data['initial_data']['num_clients'] == 1
    assert data['final_data']['initial_budget'] == min_offert_budget

    
    




def test_no_offer_fail():
    offers_source = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client = Client(name=name, surname=surname, id=id, file_path=offers_source)
    client.remaining_offers = []

    assert clients_resolver([client], 1000.0) is None





def test_no_budget_fail():
    offers_source = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client = Client(name=name, surname=surname, id=id, file_path=offers_source)

    # se c'è un offerta che si può fare dobbiamo assumere che il budget iniziale sia almeno uguale all'offerta con budget minimo
    assert len(client.remaining_offers) > 0
    
    min_offer_budget = min([offer.budget_needed for offer in client.remaining_offers])
    
    assert clients_resolver([client], min_offer_budget -1) is None




# non può finire tutto in un solo step ma può in due
def test_one_client_multiple_step():
    offers_source = "db/all_offers.json"
    name = "Pippo"
    id = 1
    surname = "Caio"
    client = Client(name=name, surname=surname, id=id, file_path=offers_source)

    # asserzioni prima di fare l'offerta
    assert len(client.remaining_offers) >= 2                                                                             # ci sono offerte da fare
    
    client_list = [client]
    assert len(client_list) > 0


    # condizioni budget manager
    # questa volta il budget necessario è sufficiente per completare la minima offferta
    min_offer = find_min_offer(client_list)

    # ora trovami l'altra offerta che non sia quella minima
    second_min_offer = find_second_min_offer(client_list)

    # ma non abbastanza per completare la seconda minima
    budget = min_offer.budget_needed + second_min_offer.budget_needed -1


    # risoluzione 
    data = clients_resolver(client_list, budget)
    assert data is not None                                                                                             # almeno uno step è stato completato


    # dovrà aver completato entrambe le offerte in due step
    assert data['final_data']['num_steps'] == 2
    assert data['initial_data']['num_clients'] == len(client_list)                                                                           # il profitto totale è uguale al profitto del cliente
    #assert data['final_data']['total_profit'] == client_list[0].profit                                                                           # il profitto totale è uguale al profitto del cliente
    #assert data['final_data']['initial_budget'] == budget
    #assert data['completed_offers'] == [offer.name for offer in client.completed_offers]                                        # le offerte completate sono il nome di tutte le offerte fatte

    # TODO altri controlli






# il cliente può completare tutte le offerte in più step
def test_one_client_complete_all_offer_multiple_step():

    offers_source = "db/all_offers.json"
    name = "Francesco"
    id = 1
    surname = "Totti"
    client = Client(name=name, surname=surname, id=id, file_path=offers_source)

    # asserzioni prima di fare l'offerta
    assert len(client.remaining_offers) >= 2                                                                             # ci sono offerte da fare
    
    client_list = [client]
    assert len(client_list) > 0


    # per testarlo si deve trovare il budget che non è sufficiente per completare tutte le offerte se non con il profitto delle offerte stesse
    budget = 0
    profit = 0
    for offer in client.remaining_offers:
        budget += offer.budget_needed
        profit += offer.profit

    budget -= (profit/2)


    # risoluzione 
    data = clients_resolver(client_list, budget)
    assert data is not None                                                                                             # almeno uno step è stato completato

    # tutte le offerte sono state completate
    assert len(client.completed_offers) == data['initial_data']['total_offers_num']












# TODO
# --------------------------------------------------------------- #
################ MULTIPLE CLIENTS ################
# --------------------------------------------------------------- #

# se io ti do il necessario per fare la minima offerta * 3, deve ritorarmi un dizionario contenente esattamente la risoluzione della minima offerta
def test_success():
    client1 = Client(name="Pippo", surname="Stronzo", id=1, file_path="db/Pippo.json")
    client2 = Client(name="Pluto", surname="Caio", id=2, file_path="db/Pluto.json")
    client3 = Client(name="Paperino", surname="Alessio", id=3, file_path="db/all_offers.json")

    clients = [client1, client2, client3]

    min_offer = find_min_offer(clients)

    budget = min_offer.budget_needed * 3

    data = clients_resolver(clients, budget)
    assert data is not None

    assert data['initial_data']['num_clients'] == len(clients)
    assert data['initial_data']['initial_budget'] == budget
    assert data['final_data']['num_steps'] == 1

    # TODO altri test
    # TODO la somma del budget allocate di tutti e tre i clienti è esattamente budget



