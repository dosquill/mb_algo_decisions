from pprint import pprint
import json
from Class.client import Client
from Class.offer import Offer
from utils.util import *


# Nota, None è quando non si può farre, Nulla appunto


# part 1: risoluzione di un offerta
# questo è il componente base. Dato un cliente e un offerta, se questa non è già stata completata la completa, budget permettendo
def offer_resolver(client: Client, offer: Offer, folder: str = None) -> dict:
    initial_budget = client.budget

    # se l'offerta è già stata fatta oppure
    # se l'offerta non si può fare per via del budget, finisci l'algoritmo
    if offer in client.completed_offers or client.budget < offer.budget_needed:
        return None
    
    # tutto normale, completa l'offerta
    client.completed_offers.append(offer)
    client.budget -= offer.budget_needed
    client.profit += offer.profit

    statistics = {
        'client_name': client.name,
        'offer_name': offer.name,
        'initial_budget': initial_budget,
        'budget_needed': offer.budget_needed,
        'remaining_budget': client.budget,
        'offer_profit': offer.profit,
        'total_profit': client.profit
    }

    # 
    # print(statistics)

    if folder is not None:
        # TODO da testare 
        save_to_csv(statistics, f'{folder}/offers/{offer.name}.csv')

    return statistics

    

