from Class.client import Client
from func.offer_resolver import offer_resolver
from func.step_resolver import *
from Class.offer import Offer   
from Class.budget_manager import BudgetManager



# create a real offer
offer = Offer("Bwin", 8.5, 50, 1)



# new client
client1 = Client("Client 1", "Surname", 1, 'db/all_offers.json')
client2 = Client("Client 2", "Surname", 2, 'db/all_offers.json')
client3 = Client("Client 3", "Surname", 3, 'db/all_offers.json')


# bm = BudgetManager(1000, [client1, client2, client3])
bm = BudgetManager(1000, [client1, client2])

print(bm)

step_resolver(bm.client_list, bm.initial, bm, folder ='results')

print(bm)




