from pprint import pprint
import json
from Class.client import Client
from Class.offer import Offer
from utils.saving_stats import *
from func.offer_resolver import *
from func.step_resolver import *
from func.client_resolver import *







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



    # SAVE STATISTICS
    save_stats_json(statistic, folder, filename='results.json')
    # save_to_csv(statistic, f'{folder}/results.csv')

    return statistic




