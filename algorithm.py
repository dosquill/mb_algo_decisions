from client import Client
from offer import Offer
from utils import *

# Nota, None è quando non si può farre, Nulla appunto

# part 1 of algorithm: offer resolution
# dato un cliente e un offerta, se questa non è già stata completata la completa, budget permettendo
# ritorna
def offer_resolution(client: Client, offer: Offer, folder: str = None) -> dict:
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

    



# part 2 of algorithm: step resolution
# quest'algoritmo risolve uno step, ovvero risolve una lista di offerte, dato un budget
def step_resolution(client: Client, step_num: int = 1, folder: str = None) -> dict:
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
            data = offer_resolution(client, offer, folder=folder)
        else:
            data = offer_resolution(client, offer)
        
        
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

    print(statistic)
        
    if folder is not None:
        save_to_csv(statistic, f'{folder}/step/{step_num}.csv') 

    return statistic









# TODO
# part 3 of algorithm: client resolution
# crea una serie di step fino a quando non ci sono più offerte da fare
def client_resolution(client: Client, folder: str = None) -> dict:
    initial_budget = client.budget
    step_num = 1
    results = []
    if folder:
        folder += f'/{client.name}'


    while (len(client.remaining_offers) > 0):
        if folder:
            data = step_resolution(client, step_num, folder=folder)
        else:
            data = step_resolution(client, step_num)
        
        if data is None:
            break

        results.append(data)
        step_num += 1


    if len(results) == 0:
        print("No results")
        return None


    # TODO vorrei poter suddividere le colonne che arrivano in min, max, avg
    # molte valori si ripetono quindi li assegno
    step_profits = [data['step_profit'] for data in results]
    remaining_budgets = [data['remaining_budget'] for data in results]
    num_completeds = [data['num_completed_offers'] for data in results]
    inutilized_budgets = [data['inutilized_budget_percentage'] for data in results]
    lenght = len(results)

    # devo aggiungere current budget
    statistic = {
        'total_profit': client.profit,
        'max_step_profit': max(step_profits),
        'avg_profit_for_step': sum(step_profits) / lenght,
        'min_step_profit': min(step_profits),

        'initial_budget': initial_budget,
        'remaining_budget': results[-1]['remaining_budget'],
        'max_remaining_budget': max(remaining_budgets),
        'avg_remaining_budget': round(sum(remaining_budgets) / lenght, 2),
        'min_remaining_budget': min(remaining_budgets),
        
        'num_steps': lenght,
        'num_completed_offers': sum(num_completeds),
        'max_num_offers_per_step': max(num_completeds),
        'avg_num_offers_per_step': sum(num_completeds) / lenght,
        'min_num_offers_per_step': min(num_completeds),

        'max_inutilized_budget_percentage': max(inutilized_budgets),
        'avg_inutilized_budget_percentage': round(sum(inutilized_budgets) / lenght, 2),
        'min_inutilized_budget_percentage': min(inutilized_budgets),

        'max_num_offers_per_step': max(num_completeds),
        'avg_num_offers_per_step': sum(num_completeds) / lenght,
        'min_num_offers_per_step': min(num_completeds),
        
        'commission': round(client.profit * 0.2, 1) ,
    }


    if client.referred_by is not None:
        statistic['referral'] = round(client.profit * 0.05, 1)
        statistic['total_commission'] = statistic['commission'] + statistic['referral']


    print(statistic)
    if folder is not None:
        save_to_csv(statistic, f'{folder}/overall.csv')
        save_stats(statistic, f'{folder}/stats.csv')
    return statistic







# step 4: final algorithm
# prende una lista di clienti, un budget e mi da la tabella di quali offerte fare e quando
def algorithm(clients: list, budget: float, folder: str = None) -> dict:
    results = []
    num_clients = len(clients)

        
    # innanzitutto, controlla quanti clienti ci sono
    if num_clients == 0:
        print("No clients")
        return None
    
    if num_clients == 1:
        print("Only one client")
        return client_resolution(clients[0])
    
    

    # ci sono due clienti, alloca il budget. Vero algoritmo effettivo
    # TODO come si alloca il budget?
    # crea una lista combinata di offerte di tutti i clienti
    # CREAZIONE LISTA COMBINATA
    offers = []
    for client in clients:
        offers += client.remaining_offers


    # crea una tabella di quante occorrenze ci sono per ogni offerta
    # TODO come si crea la tabella?
    offer_occurrences = {}
    for offer in offers:
        if offer.name in offer_occurrences:
            offer_occurrences[offer.name] += 1
        else:
            offer_occurrences[offer.name] = 1


    print(offer_occurrences)
    # ora risolvi i clienti


    statistic = {
        'num_clients': num_clients,
        # budget allocato di ogni cliente
    }

    
    # ringraziamenti
    print(statistic)
    if folder is not None:
        save_to_csv(statistic, f'{folder}/results.csv')
    return statistic
