# Main file for the project
from Class.Offer import *
from Class.Person import *
from Class.OfferList import *
from Class.Client import *
from Util.util import *
from Util.step import *
from Util.step import *


total_budget = 3000
total_offer = OfferList('db/all_offers.json')
mario = Person("Mario", "Rossi")

client = Client(mario, total_offer, 1)

results = algo(client, total_budget)

