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





# --------------------------------------------------------------- #
################ ONE CLIENT ################
# --------------------------------------------------------------- #
# @pytest.mark.single_client
def test_one_client():
    client_list = []

    all_offer = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client_list.append(Client(name, surname, id, all_offer))

    budget = 1000
    budget_manager = BudgetManager(budget, client_list)


    client = client_list[0]
    assert isinstance(client, Client)

    # è un offerta derivata dalle offerte rimanenti del cliente
    offer = client.find_by_name("Bwin")
    assert offer in client.remaining_offers
    assert offer not in client.completed_offers   # l'offerta non è già presente nella lista di offerte completate del cliente

    # asserzioni iniziali
    assert budget_manager is not None
    assert isinstance(budget_manager, BudgetManager)

    assert isinstance(offer.budget_needed, (float, int))
    assert offer.budget_needed >= 0

    assert offer.budget_needed >= 0
    assert isinstance(budget_manager.remaining_budget(), (float, int))
    budget_manager.initial_budget = offer.budget_needed + 1



    # conclusione
    data = offer_resolver(list_clients=client_list, offer=offer, bm=budget_manager)
    assert data is not None
    assert isinstance(data, dict)
    assert data['num_completed'] == 1
    assert data['initial_budget'] == budget_manager.initial_budget
    assert data['total_offer_profit'] == budget_manager.profit
    
    assert isinstance(data['offer'], dict)
    assert data['offer']['offer_name'] == offer.name
    assert data['offer']['budget_needed'] == offer.budget_needed
    assert data['offer']['offer_profit'] == offer.profit

    assert isinstance(data[1], dict)
    assert data[1]['remaining_budget'] == budget_manager.remaining_budget()
    assert data[1]['total_profit'] == budget_manager.profit
    assert data[1]['client_name'] == client.name

    assert offer in client.completed_offers    # adesso è nelle offerte completate
    



# @pytest.mark.single_client
def test_one_client_continuous():
    client_list = []

    all_offer = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client_list.append(Client(name, surname, id, all_offer))

    # dammi due offerte nella lista di offerte rimanenti del cliente
    offer1 = client_list[0].remaining_offers[0]
    offer2 = client_list[0].remaining_offers[1]
    assert offer1 is not None
    assert offer2 is not None
    assert offer1 != offer2

    budget = offer1.budget_needed + offer2.budget_needed + 1
    budget_manager = BudgetManager(budget, client_list)

    data1 = offer_resolver(list_clients=client_list, offer=offer1, bm=budget_manager)
    assert data1 is not None

    data2 = offer_resolver(list_clients=client_list, offer=offer2, bm=budget_manager)
    assert data2 is not None

    # conclusioni
    assert data1['num_completed'] + data2['num_completed'] == 2
    assert data1['initial_budget'] == budget_manager.initial_budget
    assert data2['initial_budget'] == budget_manager.initial_budget
    assert data1['total_offer_profit'] + data2['total_offer_profit'] == budget_manager.profit




# client can do one offer but not the other
# @pytest.mark.single_client
def test_one_client_continuous_fail():
    client_list = []

    all_offer = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client_list.append(Client(name, surname, id, all_offer))

    # dammi due offerte nella lista di offerte rimanenti del cliente
    offer1 = client_list[0].remaining_offers[0]
    offer2 = client_list[0].remaining_offers[1]
    assert offer1 is not None
    assert offer2 is not None
    assert offer1 != offer2


    budget = offer1.budget_needed + offer2.budget_needed + -1
    budget_manager = BudgetManager(budget, client_list)

    data1 = offer_resolver(list_clients=client_list, offer=offer1, bm=budget_manager)
    assert data1 is not None

    data2 = offer_resolver(list_clients=client_list, offer=offer2, bm=budget_manager)
    assert data2 is None






# --------------------------------------------------------------- #
############### 2 CLIENTS ###############
# --------------------------------------------------------------- #
# @pytest.mark.two_clients
def test_2clients():
    c1 = Client("Pippo", "Pippo", 1, "db/all_offers.json")
    c2 = Client("Pluto", "Pluto", 2, "db/all_offers.json")
    client_list = []
    client_list.append(c1)
    client_list.append(c2)
    
    assert client_list is not None
    num_clients = len(client_list)
    assert num_clients > 1

    assert client_list[0].remaining_offers is not None
    assert client_list[1].remaining_offers is not None

    # l'offerta è comune ad entrambi, non può essere diversa ovviamente
    offer = client_list[0].remaining_offers[0]
    assert offer is not None
    assert offer in client_list[1].remaining_offers

    # il budget comprende per farne entrambi
    budget_manager = BudgetManager(offer.budget_needed * 2 + 1, client_list)
    assert budget_manager.remaining_budget() >= offer.budget_needed * 2
    assert budget_manager is not None

    # conclusioni
    data = offer_resolver(list_clients=client_list, offer=offer, bm=budget_manager)
    assert data is not None
    assert isinstance(data, dict)
    assert data['num_completed'] == num_clients
    assert data['initial_budget'] == budget_manager.initial_budget
    assert data['total_offer_profit'] == budget_manager.profit
    assert data['offer']['offer_name'] == offer.name                    # mi aspetto l'offerta con sempre lo stesso nome
    assert data['offer']['budget_needed'] == offer.budget_needed        # mi aspetto l'offerta con sempre lo stesso budget
    assert data['offer']['offer_profit'] == offer.profit                # mi aspetto l'offerta con sempre lo stesso profitto



# quando solo uno dei due può fare l'offerta
# @pytest.mark.two_clients
def test_2clients_only_one_can():
    c1 = Client("Pippo", "Pippo", 1, "db/all_offers.json")
    c2 = Client("Pluto", "Pluto", 2, "db/all_offers.json")
    client_list = []
    client_list.append(c1)
    client_list.append(c2)
    
    assert client_list is not None
    num_clients = len(client_list)
    assert num_clients > 1

    assert client_list[0].remaining_offers is not None
    assert client_list[1].remaining_offers is not None

    # l'offerta è comune ad entrambi, non può essere diversa ovviamente
    offer = client_list[0].remaining_offers[0]
    assert offer is not None
    assert offer in client_list[1].remaining_offers

    # il budget permette di fare SOLO una
    budget_manager = BudgetManager(offer.budget_needed * 2 -1, client_list)
    assert budget_manager.remaining_budget() < offer.budget_needed * 2
    assert budget_manager is not None

    # conclusioni, che mi deve dare?
    data = offer_resolver(list_clients=client_list, offer=offer, bm=budget_manager)
    assert data is not None

    assert isinstance(data, dict)
    assert data['num_completed'] == 1   
    assert data['initial_budget'] == budget_manager.initial_budget
    assert data['total_offer_profit'] == budget_manager.profit
    assert data['offer']['budget_needed'] == offer.budget_needed        # mi aspetto l'offerta con sempre lo stesso budget
    assert data['offer']['offer_profit'] == offer.profit                # mi aspetto l'offerta con sempre lo stesso profitto
    assert data[1]['client_name'] == client_list[0].name                # mi aspetto che sia il primo client a farla
    assert not data[1]['client_name'] == client_list[1].name            # mi aspetto che non sia il secondo client a farla






# test di integrità dei dati tra due funzioni di risoluzione una dopo l'altra
# @pytest.mark.two_clients
def test_2clients_continuous():
    c1 = Client("Pippo", "Pippo", 1, "db/all_offers.json")
    c2 = Client("Pluto", "Pluto", 2, "db/all_offers.json")
    client_list = []
    client_list.append(c1)
    client_list.append(c2)
    
    assert client_list is not None
    num_clients = len(client_list)
    assert num_clients > 1

    assert client_list[0].remaining_offers is not None
    assert client_list[1].remaining_offers is not None


    # dammi due offerte nella lista di offerte rimanenti del primo cliente che siano anche nel secondo
    offer1 = client_list[0].remaining_offers[0]
    offer2 = client_list[0].remaining_offers[1]
    assert offer1 is not None
    assert offer2 is not None
    assert offer1 != offer2
    assert offer1 in client_list[1].remaining_offers
    assert offer2 in client_list[1].remaining_offers
    num_offers = 2
    
    # il budget permette di fare Entrambe le offerte di entrambi i clienti
    budget = (offer1.budget_needed *2) + (offer2.budget_needed *2) + 1
    budget_manager = BudgetManager(budget, client_list)
    assert budget_manager is not None

    # conclusioni
    data1 = offer_resolver(list_clients=client_list, offer=offer1, bm=budget_manager)
    assert data1 is not None

    data2 = offer_resolver(list_clients=client_list, offer=offer2, bm=budget_manager)
    assert data2 is not None

    # comparison
    assert data1['num_completed'] + data2['num_completed'] == num_clients * num_offers
    assert data1['total_offer_profit'] + data2['total_offer_profit'] == budget_manager.profit
    assert data1[1]['client_name'] == client_list[0].name
    assert data1[2]['client_name'] == client_list[1].name
    assert data2[1]['client_name'] == client_list[0].name
    assert data2[2]['client_name'] == client_list[1].name
    assert data1[1]['remaining_budget'] == budget_manager.initial_budget - offer1.budget_needed
    assert data1[2]['remaining_budget'] == budget_manager.initial_budget - offer1.budget_needed *2
    assert data2[1]['remaining_budget'] == budget_manager.initial_budget - offer1.budget_needed *2 - offer2.budget_needed
    assert data2[2]['remaining_budget'] == budget_manager.initial_budget - offer1.budget_needed *2 - offer2.budget_needed *2






# la prima offerta è fattibile per entrambi, la seconda no
# @pytest.mark.two_clients
def test_2clients_continuous_fail():
    c1 = Client("Pippo", "Pippo", 1, "db/all_offers.json")
    c2 = Client("Pluto", "Pluto", 2, "db/all_offers.json")
    client_list = []
    client_list.append(c1)
    client_list.append(c2)
    
    assert client_list is not None
    num_clients = len(client_list)
    assert num_clients > 1

    assert client_list[0].remaining_offers is not None
    assert client_list[1].remaining_offers is not None


    # dammi due offerte nella lista di offerte rimanenti del primo cliente che siano anche nel secondo
    offer1 = client_list[0].remaining_offers[0]
    offer2 = client_list[0].remaining_offers[1]
    assert offer1 is not None
    assert offer2 is not None
    assert offer1 != offer2
    assert offer1 in client_list[1].remaining_offers
    assert offer2 in client_list[1].remaining_offers
    num_offers = 2


    # il budget permette di fare la prima sequenza di offerte, non la seconda
    budget = (offer1.budget_needed *2) + 1
    budget_manager = BudgetManager(budget, client_list)
    assert budget_manager is not None

    # conclusioni
    data1 = offer_resolver(list_clients=client_list, offer=offer1, bm=budget_manager)
    assert data1 is not None

    data2 = offer_resolver(list_clients=client_list, offer=offer2, bm=budget_manager)
    assert data2 is None















# --------------------------------------------------------------- #
############### LIST OF CLIENTS ###############
# --------------------------------------------------------------- #

@pytest.fixture
def multiple_clients():
    all_offer = "db/all_offers.json"
    clients = [
        Client("Alice", "Smith", 1, all_offer),
        Client("Bob", "Johnson", 2, all_offer),
        Client("Charlie", "Williams", 3, all_offer)
    ]
    return clients




## @pytest.mark.multiple
def test_multiple_clients(offer, multiple_clients):
    num_clients = len(multiple_clients)
    budget_manager = BudgetManager((offer.budget_needed * num_clients), multiple_clients)
    
    assert budget_manager is not None

    result = offer_resolver(list_clients=multiple_clients, offer=offer, bm=budget_manager)
    assert result is not None




def test_multiple_clients_insufficient_budget(offer, multiple_clients):
    budget = offer.budget_needed -1
    budget_manager = BudgetManager(budget, multiple_clients)
    
    result = offer_resolver(list_clients=multiple_clients, offer=offer, bm=budget_manager) 
    assert result is None





def test_multiple_clients_no_budget_manager(offer, multiple_clients):
    budget_manager = None
    
    pytest.raises(Exception, offer_resolver, multiple_clients, offer, budget_manager)













# --------------------------------------------------------------- #
################ GENERAL FAILS ###############
# --------------------------------------------------------------- #
def test_not_in_remaining_offers():
    client_list = []

    all_offer = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client_list.append(Client(name, surname, id, all_offer))

    budget = 1000
    budget_manager = BudgetManager(budget, client_list)


    # Remove the offer from the list of remaining offers for the client
    client = client_list[0]
    assert client.remaining_offers is not None
    offer = client.remaining_offers[0]
    assert offer is not None
    client.remaining_offers.remove(offer)
    
    # Set budget_manager initial and remaining budget so that it cannot afford the offer
    budget_manager.initial_budget = offer.budget_needed - 1
    
    assert offer not in client.remaining_offers
    
    # Try to resolve the offer
    result = offer_resolver(list_clients=client_list, offer=offer, bm=budget_manager)
    
    # Check the output
    assert result is None  




def test_no_budget_manager():
    client_list = []

    all_offer = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client_list.append(Client(name, surname, id, all_offer))

    budget_manager = None

    pytest.raises(Exception, offer_resolver, client_list, offer, budget_manager)




def test_budget_insufficient(offer):
    client_list = []

    all_offer = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client_list.append(Client(name, surname, id, all_offer))

    budget = 1000
    budget_manager = BudgetManager(budget, client_list)

    assert offer.budget_needed > 0
    budget_manager.initial_budget = offer.budget_needed - 1

    assert offer_resolver(list_clients=client_list, offer=offer, bm = budget_manager) is None




def test_offer_already_done(offer):
    client_list = []

    all_offer = "db/all_offers.json"
    name = "Pippo"
    surname = "Caio"
    id = 1
    client_list.append(Client(name, surname, id, all_offer))

    budget = 1000
    budget_manager = BudgetManager(budget, client_list)

    client = client_list[0]
    client.completed_offers.append(offer)

    assert offer in client.completed_offers
    assert offer_resolver(list_clients=client_list, offer=offer, bm = budget_manager) is None



