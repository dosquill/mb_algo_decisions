from pprint import pprint
from Class.client import Client
from utils.saving_stats import *
from func.offer_resolver import *







# part 2: risoluzione di uno step
# Aggiungiamo un altro layer, lo step. Lo step è una lista di offerte fattibili dato un budget. Quest'algoritmo lo risolve lo risolve.
def step_resolver(client: Client, step_num: int = 1, folder: str = None) -> dict:
    initial_budget = client.budget
    profit = 0
    completed_offers = []
    remaining_budget = 0
    inutilize_budget_percentage = 0
    num_completed = 0

    # la lista deve essere sempre ordinata per roi
    client.remaining_offers.sort(key=lambda x: x.roi, reverse=True)

    minimum_budget_required = min([offer.budget_needed for offer in client.remaining_offers])

    # TODO
    for offer in client.remaining_offers:
        if client.budget < minimum_budget_required:
            break
        
        if folder:
            data = offer_resolver(client, offer, folder=folder)
        else:
            data = offer_resolver(client, offer)
        
        
        if data is not None:
            num_completed += 1
            profit += data['offer_profit']
            completed_offers.append(offer)
            remaining_budget = data['remaining_budget']
            inutilize_budget_percentage = round((remaining_budget / initial_budget) * 100, 3)
        


    # se in questa fase non sono state completate offerte, allora il budget non più sufficiente
    if num_completed == 0:  
        return None


    # budget allocato venga restituito e che il prossimo step tenga conto dei guadagni di prima
    client.budget = initial_budget + profit
    # aggiornamento nuova lista
    client.remaining_offers = [offer for offer in client.remaining_offers if offer not in client.completed_offers]


    statistic = {
        'step_num': step_num,
        'step_profit': profit,
        'num_completed_offers': num_completed,
        'inutilized_budget_percentage': inutilize_budget_percentage,
        'initial_budget': initial_budget,
        'remaining_budget': remaining_budget,
        'completed_offers': [offer.name for offer in completed_offers],    # aggiungi solo una lista di nomi
    }
    

    # SAVE STATISTICS
    # print(statistic)
    # save_to_csv(statistic, folder, filename=f'/step/{step_num}.csv') 
    # save_stats_json(statistic, folder, filename=f'{client.name}/step/{step_num}.json') 

    return statistic





