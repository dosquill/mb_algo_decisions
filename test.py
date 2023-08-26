# Main file for the project
from Class.Offer import *
from Class.Client import *
from Class.OfferList import *
from Util.util import *
from Util.step import *
from Util.step import *


total_offer = OfferList('db/table.json')
print(total_offer)

identical_list = total_offer.copy()
identical_list.remove_by_bookmaker('Bwin')
identical_list.remove_by_bookmaker('Williamhill')

identical_list2 = identical_list.copy()
print(identical_list)
