from pprint import pprint
import json
from client import Client
from offer import Offer
from utils import *


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

    #print(statistic)
        
    if folder is not None:
        save_to_csv(statistic, f'{folder}/step/{step_num}.csv') 

    return statistic












# part 3: risoluzione di un cliente
# Il cliente si risolve quando non ci sono più offerte da fare o quando il budget non è più sufficiente. Lo risolve per step
def client_resolver(client: Client, folder: str = None) -> dict:
    initial_budget = client.budget
    step_num = 1
    results = []
    if folder:
        folder += f'/{client.name}'


    while (len(client.remaining_offers) > 0):
        if folder:
            data = step_resolver(client, step_num, folder=folder)
        else:
            data = step_resolver(client, step_num)
        
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














# step 4: risolutore di una lista di clienti
# prende una lista di clienti, un budget, alloca il budget per quei clienti e ne risolve uno step
def clients_list_resolver(clients: list, total_budget: float, folder: str = None) -> dict:
    initial_budget = total_budget
    num_clients = len(clients)
    total_offers_num = sum([len(client.remaining_offers) for client in clients])

    in_between_data = {}

    # Dictionary to store the count of each offer name
    offer_occurrences = {}  
    for client in clients:
        # Loop through each remaining offer for this client
        for offer in client.remaining_offers:
            # Increment the count for this offer name in the dictionary
            offer_name = offer.name  # Assuming the Offer class has a 'name' attribute
            if offer_name in offer_occurrences:
                offer_occurrences[offer_name] += 1
            else:
                offer_occurrences[offer_name] = 1



    # innanzitutto, controlla quanti clienti ci sono
    if num_clients == 0:
        print("No clients")
        return None
    
    
    if num_clients == 1:
        print("Only one client")
        return client_resolver(clients[0])
    
    
    # BUDGET ALLOCATION (kept within the main function)
    def budget_allocation():
        # Calculate the average ROI for each client
        avg_roi_per_client = {client.name: client.calculate_average_roi() for client in clients}
        
        # Calculate the total ROI
        total_roi = round(sum(avg_roi_per_client.values()), 2)
        
        # Calculate the weight for each client
        weights = {name: round((roi / total_roi), 2) for name, roi in avg_roi_per_client.items()}
        
        various_budget = {}
        # Allocate the budget based on the calculated weight
        for client in clients:
            client.budget = round(total_budget * weights.get(client.name, 0), 2)
            various_budget[client.name] = client.budget
        
        return various_budget, weights, avg_roi_per_client, total_roi


    various_budget, weights, average_roi_per_client, total_roi = budget_allocation()
    allocation = {
        'various_budget': various_budget,
        'weights': weights,
        'average_roi_per_client': average_roi_per_client,
        'total_roi': total_roi,
    }


    global_step_num = 1
    global_results = {}
    total_profit = 0
    # STEP OF CLIENT RESOLVER
    while True: 
        step_profit = 0

        
        for client in clients:
            if len(client.remaining_offers) == 0:
                continue    # skip to the next client if this haven't no more remaining offers

            data = step_resolver(client, global_step_num)
            in_between_data['step_allocation'] = allocation
            
            if data is not None:
                in_between_data[global_step_num] = global_results
                step_profit += data['step_profit']
                global_results[client.name] = data

        total_profit += step_profit
        total_budget += step_profit

        # reallocate the budget
        # come varia l'allocazione nel tempo?        
        various_budget, weights, average_roi_per_client, total_roi = budget_allocation()

        if step_profit == 0:
            break

        global_step_num += 1




    # EXITING CODE
    # JSON FORMATTING DATA
    initial_data = {
        'num_clients': num_clients,
        'initial_budget': initial_budget,
        'total_offers_num': total_offers_num,
        'offer_occurrences': offer_occurrences,  # Dictionary to store the count of each offer name
        'total_roi': total_roi,
    }

    final_data = {
        'total_step_num': global_step_num,
        'final_budget': total_budget,
        'total_profit': total_budget - initial_budget,
    }




    # COMPILE STATISTICS
    statistic = {
        'initial_data': initial_data,

        # in between data   
        'in_between_data': in_between_data,
        
        # final data
        'final_data': final_data,
    }




    ## PRINTING
    if folder is not None:
        # if file already exists, delete it
        if os.path.exists(f'{folder}/results.json'):
            os.remove(f'{folder}/results.json')
        json.dump(statistic, open(f'{folder}/results.json', 'w'), indent=4)
        # save_to_csv(statistic, f'{folder}/results.csv')
    return statistic




