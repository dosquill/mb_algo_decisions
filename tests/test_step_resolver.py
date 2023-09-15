import pytest
import copy
from Class.client import Client
from Class.offer import Offer
from func.step_resolver import *
from utils.save_to_json import *
from Class.budget_manager import BudgetManager
from utils.util import *


# TODO step capisce che se un cliente ha fatto un offerte non la deve controllare di nuovo?


# --------------------------------------------------------------- #
################ ONE CLIENT ################
# --------------------------------------------------------------- #

# almeno uno step è stato completato
# lo step si completa quando per dato budget non ci sono più offerte da fare
def test_single_client_step_success():
    offers_source = "db/all_offers.json"
    name = "Pippo"
    id = 1
    surname = "Caio"
    client = Client(name=name, surname=surname, id=id, file_path=offers_source)

    # asserzioni prima di fare l'offerta
    assert len(client.remaining_offers) > 0                                                                             # ci sono offerte da fare
    
    client_list = [client]
    assert len(client_list) > 0

    # condizioni budget manager
    # il budget è necessario almeno per completare uno step
    min_offer = find_min_offer(client_list)
    budget = min_offer.budget_needed + 1
    budget_manager = BudgetManager(budget, client_list)
    assert budget_manager is not None
    assert isinstance(budget_manager, BudgetManager)


    # risoluzione step
    step_num = 1
    data = step_resolver(client_list, budget_manager, step_num=step_num)
    assert data is not None                                                                                             # almeno uno step è stato completato

    assert data['step_num'] == step_num
    assert data['step_profit'] == budget_manager.profit                                                                         # il contatore è uguale al primo step
    assert data['initial_budget'] == budget
    assert data['completed_offers'] == [offer.name for offer in client.completed_offers]                                        # le offerte completate sono il nome di tutte le offerte fatte

    # assert data['step_num'] == 1
    # assert data['step_profit'] == client.profit                                                                          # il contatore è uguale al primo step
    # assert data['num_completed_offers'] == len(client.completed_offers)
    # assert data['initial_budget'] == initial_budget
    # assert data['remaining_budget'] == initial_budget - sum(offer.budget_needed for offer in client.completed_offers)   # il budget rimanente è la somma dei budget delle offerte che hai fatto
    # assert data['completed_offers'] == [offer.name for offer in client.completed_offers]                                        # le offerte completate sono il nome di tutte le offerte fatte




def test_single_client_single_multiple_offers():
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
    # il budget è necessario almeno per completare uno step di due offerte
    min_offer = find_min_offer(client_list)
    # ora trovami l'altra offerta che non sia quella minima
    second_offer_budget = 0
    for offer in client.remaining_offers:
        if offer.budget_needed != min_offer.budget_needed:
            second_offer_budget = offer.budget_needed
            break

    budget = min_offer.budget_needed + second_offer_budget + 1
    budget_manager = BudgetManager(budget, client_list)
    assert budget_manager is not None
    assert isinstance(budget_manager, BudgetManager)


    # risoluzione step
    step_num = 1
    data = step_resolver(client_list, budget_manager, step_num=step_num)
    assert data is not None                                                                                             # almeno uno step è stato completato

    # dovrà aver completato entrambe le offerte in uno step
    assert data['step_num'] == 1
    assert data['step_profit'] == budget_manager.profit                                                                         # il contatore è uguale al primo step
    assert data['initial_budget'] == budget
    #assert data['completed_offers'] == [offer.name for offer in client.completed_offers]                                        # le offerte completate sono il nome di tutte le offerte fatte





# TODO
def test_one_client_multiple_offers():
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
    budget = min_offer.budget_needed + second_min_offer.budget_needed 

    budget_manager = BudgetManager(budget, client_list)
    assert budget_manager is not None



    # risoluzione step
    data = step_resolver(client_list, budget_manager)
    assert data is not None                                                                                             # almeno uno step è stato completato

    # dovrà aver completato entrambe le offerte in uno step
    assert data['step_num'] == 1
    assert data['step_profit'] == budget_manager.profit                                                                         # il contatore è uguale al primo step
    assert data['initial_budget'] == budget
    #assert data['completed_offers'] == [offer.name for offer in client.completed_offers]                                        # le offerte completate sono il nome di tutte le offerte fatte





# il cliente può completare almeno uno step, al secondo il budget, sommato al profitto del primo già non è più sufficiente
# se il cliente non ha più budget, dimmi quelle che si possono fare
# ma non ritornare Null
def test_one_client_runs_out_of_budget():
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

    budget_manager = BudgetManager(budget, client_list)
    assert budget_manager is not None



    # risoluzione step
    data = step_resolver(client_list, budget_manager)
    assert data is not None                                                                                             # almeno uno step è stato completato

    # dovrà aver completato entrambe le offerte in uno step
    assert data['step_num'] == 1
    assert data['step_profit'] == budget_manager.profit                                                                         # il contatore è uguale al primo step
    assert data['initial_budget'] == budget
    #assert data['completed_offers'] == [offer.name for offer in client.completed_offers]                                        # le offerte completate sono il nome di tutte le offerte fatte
    assert data['completed_offers'] == [min_offer.name]                                        # le offerte completate sono il nome di tutte le offerte fatte







# il cliente può completare tutte le offerte in un solo step
def test_one_client_complete_all_offer():
    offers_source = "db/all_offers.json"
    name = "Pippo"
    id = 1
    surname = "Caio"
    client = Client(name=name, surname=surname, id=id, file_path=offers_source)

    # asserzioni prima di fare l'offerta
    assert len(client.remaining_offers) >= 1                                                                             # ci sono offerte da fare
    
    client_list = [client]
    assert len(client_list) > 0


    # condizioni budget manager
    # ma non abbastanza per completare la seconda minima
    # il budget è la somma di tutte le offerte
    budget = sum(offer.budget_needed for offer in client.remaining_offers)

    budget_manager = BudgetManager(budget, client_list)
    assert budget_manager is not None


    # risoluzione step
    data = step_resolver(client_list, budget_manager)
    assert data is not None                                                                                             # almeno uno step è stato completato

    # dovrà aver completato entrambe le offerte in uno step
    assert data['step_num'] == 1
    assert data['step_profit'] == budget_manager.profit                                                                         # il contatore è uguale al primo step
    assert data['initial_budget'] == budget
    assert data['completed_offers'] == [offer.name for offer in client.completed_offers]                                        # le offerte completate sono il nome di tutte le offerte fatte






# il cliente non può completare nessuna offerta
def test_one_client_complete_no_offer():
    offers_source = "db/all_offers.json"
    name = "Pippo"
    id = 1
    surname = "Caio"
    client = Client(name=name, surname=surname, id=id, file_path=offers_source)

    # asserzioni prima di fare l'offerta
    assert len(client.remaining_offers) >= 1                                                                             # ci sono offerte da fare
    
    client_list = [client]
    assert len(client_list) > 0


    # condizioni budget manager
    # ma non abbastanza per completare la seconda minima
    # il budget è la somma di tutte le offerte
    budget = find_min_offer(client_list).budget_needed - 1

    budget_manager = BudgetManager(budget, client_list)
    assert budget_manager is not None


    # risoluzione step
    data = step_resolver(client_list, budget_manager)
    assert data is None                                                                                             # almeno uno step è stato completato

    # dovrà aver completato entrambe le offerte in uno step
    # assert data['step_num'] == 1
    # assert data['step_profit'] == budget_manager.profit                                                                         # il contatore è uguale al primo step
    # assert data['initial_budget'] == budget
    # assert data['completed_offers'] == [offer.name for offer in client.completed_offers]                                        # le offerte completate sono il nome di tutte le offerte fatte







# TODO
# se faccio step offer di nuovo con lo stesso budget manager, non deve fare nulla










# TODO
# --------------------------------------------------------------- #
################ TWO CLIENTS ################
# --------------------------------------------------------------- #

















# --------------------------------------------------------------- #
################ MULTIPLE CLIENTS ################
# --------------------------------------------------------------- #

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
def test_2step_failures(client):
    pass











# --------------------------------------------------------------- #
################ GENERAL TESTING ################
# --------------------------------------------------------------- #

# caso 2: non ci sono abbastanza soldi
def test_no_budget_manager():
    pytest.raises(Exception, step_resolver, [Client("Pippo", "Paperino", 1, "db/all_offers.json")], None, 1, "db/") 




def test_no_offers_failures():
    # caso 1: non ci sono offerte
    client = Client("Pippo", "Paperino", 1, "db/all_offers.json")
    client.remaining_offers = []

    clients = [client]
    bm = BudgetManager(1000, clients)

    assert step_resolver(clients, bm) is None




# TODO
# caso 2: non ci sono abbastanza soldi
def test_no_budget_failure():
    client = Client("Pippo", "Paperino", 1, "db/all_offers.json")

    clients = [client]

    offers = [offer.budget_needed for offer in client.remaining_offers]
    min_offer = min(offers)

    bm = BudgetManager(min_offer -1, clients)

    assert bm is not None
    assert min_offer > bm.remaining_budget()
    assert step_resolver(client, bm) is None


