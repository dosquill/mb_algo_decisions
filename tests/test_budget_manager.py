import pytest
from Class.offer import Offer
from Class.client import Client
from Class.budget_manager import BudgetManager


# TODO da fare



# Test initialization of BudgetManager
def test_init():
    all_offers = "db/all_offers.json"
    client1 = Client("John", "Doe", 1, all_offers)
    client2 = Client("Jane", "Doe", 2, all_offers)
    client_list = [client1, client2]
    initial_budget = 1000

    bm = BudgetManager(initial_budget, client_list)
    assert bm.initial_budget == 1000
    assert bm.allocated == 0
    assert bm.num_clients == 2
    assert bm.profit == 0


""" 
# Test allocation method
def test_allocate(setup_data):
    client_list, initial_budget = setup_data
    bm = BudgetManager(initial_budget, client_list)
    bm.allocate()
    assert bm.budget_tracking['John'] > 0  # Replace with expected value
    assert bm.budget_tracking['Jane'] > 0  # Replace with expected value

"""



# Test resolving method
def test_resolving():
    all_offers = "db/all_offers.json"
    client1 = Client("John", "Doe", 1, all_offers)
    client_list = [client1]
    initial_budget = 1000

    bm = BudgetManager(initial_budget, client_list)
    offer = Offer("Offer1", 10, 100, 1)
    
    assert bm.resolving(client_list[0], offer) == True
    assert bm.allocated == 100
    assert bm.profit == 10



""" 
# Test remaining_budget method
def test_remaining_budget(setup_data):
    client_list, initial_budget = setup_data
    bm = BudgetManager(initial_budget, client_list)
    bm.allocate()
    assert bm.remaining_budget() == initial_budget - bm.allocated  # Replace with expected value





# Test best_offer method
def test_best_offer(setup_data):
    client_list, initial_budget = setup_data
    bm = BudgetManager(initial_budget, client_list)
    best = bm.best_offer(client_list[0])
    assert best.name == "Offer2"





# Test for exceeding the budget
def test_budget_exceeded(setup_data):
    client_list, initial_budget = setup_data
    client1 = Client("Mark", "Smith", 3, "file_path3")
    client1.remaining_offers = [Offer("Offer4", 50, 1100, 3)]
    client_list.append(client1)
    bm = BudgetManager(initial_budget, client_list)
    bm.allocate()
    assert bm.resolving(client1, Offer("Offer4", 50, 1100, 3)) == False
    assert bm.remaining_budget() >= 0




# Test allocate method when no clients are present
def test_allocate_no_clients():
    client_list = []
    initial_budget = 1000
    bm = BudgetManager(initial_budget, client_list)
    bm.allocate()
    assert bm.remaining_budget() == initial_budget




# Test resolving method when no offers are available for a client
def test_resolving_no_offers(setup_data):
    client_list, initial_budget = setup_data
    bm = BudgetManager(initial_budget, client_list)
    client_list[0].remaining_offers = []
    assert bm.resolving(client_list[0], Offer("Offer5", 10, 100, 1)) == False




# Test if the class can handle negative budget
def test_negative_budget():
    client_list = []
    initial_budget = -100
    bm = BudgetManager(initial_budget, client_list)
    assert bm.remaining_budget() == initial_budget

 """