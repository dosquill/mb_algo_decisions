# Main file for the project
from Class.Offer import *
from Class.Person import *
from Class.OfferList import *
from Class.Client import *
from Util.util import *
from func.algorithm import *
from func.algorithm import *

# INPUT
total_budget = 3000
total_offer = OfferList('db/all_offers.json')
mario = Person("Mario", "Rossi")
client = Client(mario, total_offer, 1)

algorithm(client, total_budget)

