# Main file for the project
from Class.Offer import *
from Class.Client import *
from Class.OfferList import *
from Util.util import *
from Util.step import *
from Util.step import *


total_budget = 3000
total_offer = OfferList('db/table.json')
client = Client("Mario", "Rossi")

results = algo(client, total_offer, total_budget)

