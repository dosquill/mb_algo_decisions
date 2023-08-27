# Main file for the project
from custom.Offer import *
from custom.Person import *
from custom.OfferList import *
from custom.Client import *
from custom.ClientList import *
from utils.util import *
from func.algorithm import *
from func.algorithm import *



# INPUT
total_budget = 3000

total_offer = OfferList('db/all_offers.json')

mario = Person("Mario", "Rossi")
pippo = Person("Pippo", "Verdi")

client1 = Client(mario, total_offer, 1)
client2 = Client(pippo, total_offer, 2)

client_list = ClientList()
client_list.add_item(client1)
client_list.add_item(client2)

print(client_list)

client_result(client1, total_budget)

