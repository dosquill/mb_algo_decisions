from pprint import pprint
from Class.budget_manager import BudgetManager
from utils.save_to_json import *
from utils.util import *
from func.offer_resolver import offer_resolver


# part 2: risoluzione di uno step
# Aggiungiamo un altro layer, lo step. Lo step è una lista di offerte fattibili dato un budget. Quest'algoritmo lo risolve lo risolve.
def step_resolver(clients_list: list, bm: BudgetManager = None, step_num: int = 1, folder: str = None) -> dict:
    if bm is None:
        raise Exception("BudgetManager must be provided")
    

    initial_budget = bm.initial
    completed_offers = []
    inutilize_budget_percentage = 0
    num_completed = 0
    step_profit = 0

    offer_occurrence = offer_occurrences_dict(clients_list)
    pprint(offer_occurrence)

    # TODO
    # client.remaining_offers.sort(key=lambda x: x.roi, reverse=True)

    min_offer = find_minimum_budget_required(clients_list)
    print(min_offer)

    # TODO devo iterare per il numero di offerte del dizionario in ordine di roi

    for key, value in offer_occurrence.items():
        offer_count = 0
        for client in clients_list:

            # continua ad iterare
            if bm.remaining_budget() < min_offer:
                print(f'Client {client.name} has not enough budget to complete any offer')
                break
            

            offer = found_offer_by_name(client, key)

            if offer is None:
                print(f'Client {client.name} don\' have {offer.name}')
                continue

            if folder:
                data = offer_resolver([client], offer, bm.initial, bm, folder=folder)
            else:
                data = offer_resolver([client], offer, bm.initial, bm)
            
            # è importante che non rompa il ciclo perché non è detto che se no può fare un offerta non ne possa fare un altra più piccola
            if data is None:
                print(f'Client {client.name} has not enough budget to complete {offer.name}')
                continue

            num_completed += 1
            offer_count += 1
            step_profit += offer.profit
            completed_offers.append(offer)
            # TODO il budget rimanente è a dipendenza del client
            #remaining_budget[client.name] = data['remaining_budget']
            #inutilize_budget_percentage = round((remaining_budget / initial_budget) * 100, 3)
            
            if offer_count == value:
                offer_count = 0
                break


    # se in questa fase non sono state completate offerte, allora il budget non più sufficiente
    if num_completed == 0:  
        return None


    # budget allocato venga restituito e che il prossimo step tenga conto dei guadagni di prima
    bm.release(initial_budget + step_profit)


    statistic = {
        'step_num': step_num,
        'step_profit': step_profit,
        'num_completed_offers': num_completed,
        'inutilized_budget_percentage': inutilize_budget_percentage,
        'initial_budget': initial_budget,
        #'remaining_budget': remaining_budget,
        'completed_offers': [offer.name for offer in completed_offers],    # aggiungi solo una lista di nomi
    }
    

    # SAVE STATISTICS
    print(statistic)
    save_stats_json(statistic, folder, filename=f'/step/{step_num}.json') 

    return statistic





