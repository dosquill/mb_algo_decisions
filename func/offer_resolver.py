from pprint import pprint
from Class.client import Client
from Class.offer import Offer
from Class.budget_manager import BudgetManager
from utils.save_to_json import *

# la funzione si deve solo preoccupare di risolvere le offerte
# Qui ti do solo una lista di persone che devono fare l'offerta

# part 1: risoluzione di un offerta
# questo è il componente base. Dato un cliente e un offerta, se questa non è già stata completata la completa, budget permettendo
def offer_resolver(list_clients: list, offer: Offer, budget: float, bm: BudgetManager = None, folder: str = None) -> dict:
    # potrebbe essere passato, se non c'è vuol dire che deve essere nuovo
    if bm is None:
        bm = BudgetManager(budget, list_clients)         # passare una lista di clienti fatta solo da uno
    num_completed = 0
    total_offer_profit = 0

    if list_clients is None:
        raise ValueError("No clients in the list")


    statistics ={
        'initial_budget': bm.initial,
        'offer': {
        'offer_name': offer.name,
        'budget_needed': offer.budget_needed,
        'offer_profit': offer.profit,
        }
    }

    
    for client in list_clients:
        if offer in client.completed_offers:
            return None
        if bm.resolving(client, offer):
            num_completed += 1
            client.completed_offers.append(offer)
            
            total_offer_profit += offer.profit
            statistics[num_completed] = {
                'client_name': client.name,
                'remaining_budget': bm.remaining_budget(),
                'total_profit': bm.profit
            }
        else: 
            return None
        
    statistics['num_completed'] = num_completed
    statistics['total_offer_profit'] = total_offer_profit

    if num_completed == 0:
        return None
    

    # SAVE STATISTICS
    pprint(statistics)  
    save_stats_json(statistics, folder, f'/offers/{offer.name}.json')

    return statistics

    




