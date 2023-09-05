from pprint import pprint
from utils.save_to_json import *
from func.step_resolver import step_resolver
from func.client_resolver import client_resolver


# TODO il fatto fondamentale è questo, l'algoritmo adesso va bene, ma deve considerare il fatto che il budget può essere sbilanciato per fare 


def budget_allocation(clients: list, total_budget: float) -> dict:
    # Calculate the average ROI for each client
    avg_roi_per_client = {client.name: client.calculate_average_roi() for client in clients}
    
    # Calculate the total ROI
    total_roi = round(sum(avg_roi_per_client.values()), 2)
    
    # Calculate the weight for each client
    weights = {name: round((roi / total_roi), 2) for name, roi in avg_roi_per_client.items()}
    
    budget_tracking = {}
    # Allocate the budget based on the calculated weight
    for client in clients:
        client.budget = round(total_budget * weights.get(client.name, 0), 2)
        budget_tracking[client.name] = client.budget
    
    return {
        'budget_tracking': budget_tracking,
        'weights': weights,
        'average_roi_per_client': avg_roi_per_client,
        'total_roi': total_roi,
    } 


# TODO quando arriva qua dentro, il budget è già stato allocato
def budget_allocation_new(clients: list, occurence: dict, total_budget: float) -> dict:
    budget_tracking = {}
    completed_allocation = []
    remaining_budget = total_budget  # Initialize remaining_budget to total_budget
    
    # Loop through the sorted dictionary 'occurence'
    for offer_name, offer_count in occurence.items():
        # Initialize a counter for each offer
        offer_counter = 0
        
        # Loop through each client
        for client in clients:
            # Loop through the client's remaining offers
            for offer in client.remaining_offers:
                if offer.name == offer_name and offer.budget_needed <= remaining_budget:
                    # Add the offer.budget_needed to the client's budget
                    client.budget += offer.budget_needed
                    
                    # Update the budget tracking dictionary
                    budget_tracking[client.name] = client.budget
                    
                    # Subtract the allocated budget from the remaining budget
                    remaining_budget -= offer.budget_needed
                    
                    # Increment the offer counter
                    offer_counter += 1
                    
                    # Break if the offer counter matches the offer_count
                    if offer_counter == offer_count:
                        completed_allocation.append(offer_name)
                        break
            
            # Break the outer loop if the offer counter matches the offer_count
            if offer_counter == offer_count:
                completed_allocation.append(offer_name)
                break
                
    print(budget_tracking)
    print(remaining_budget)

    for names in completed_allocation:
        if names in occurence:
            del occurence[names]

    # se la somma dei budget di ognuno supera quella iniziale allora porco dio che cazzo succede
    if sum(budget_tracking.values()) > total_budget:
        print(budget_tracking)
        print(remaining_budget)
        print(total_budget)
        print(sum(budget_tracking.values()))
        raise Exception("Porco dio che cazzo succede")

    return {
        'budget_tracking': budget_tracking,
        'remaining_budget': remaining_budget
    }

    


# Dictionary che conta quante volte, in totale, l'offerta verrà proposta
def offer_occurrences_dict(clients: list) -> dict:
    offer_occurrences = {}  
    for client in clients:
        for offer in client.remaining_offers:
            # Increment the count for this offer name in the dictionary
            offer_name = offer.name  # Assuming the Offer class has a 'name' attribute
            if offer_name in offer_occurrences:
                offer_occurrences[offer_name] += 1
            else:
                offer_occurrences[offer_name] = 1
    return offer_occurrences





# step 4: risolutore di una lista di clienti
# prende una lista di clienti, un budget, alloca il budget per quei clienti e ne risolve uno step
def clients_list_resolver(clients: list, total_budget: float, folder: str = None) -> dict:
    initial_budget = total_budget
    total_offers_num = sum([len(client.remaining_offers) for client in clients])


    # Dictionary to store the count of each offer name
    # TODO assicurati che la lista sia sempre ordinata per roi, nel testing magari
    offer_occurrences = offer_occurrences_dict(clients)
    print(offer_occurrences)
    


    # innanzitutto, controlla quanti clienti ci sono
    num_clients = len(clients)
    if num_clients == 0:
        print("No clients")
        return None
    
    if num_clients == 1:
        print("Only one client")
        return client_resolver(clients[0])    
    

    # prima chiamata a questa funzione per le statistiche iniziali e per l'allocazione del budget
    allocation = budget_allocation_new(clients, offer_occurrences, total_budget)
    
    #allocation = budget_allocation(clients, total_budget)
    #budget_tracking = allocation['budget_tracking']
    #weights = allocation['weights']
    #avg_roi_per_client = allocation['average_roi_per_client']
    #total_roi = allocation['total_roi']
    #expected_profit = total_budget * total_roi



    in_between_data = {}
    global_step_num = 1
    global_results = {}
    total_profit = 0
    # STEP OF CLIENT RESOLVER FUNCTION
    while True: 
        step_profit = 0

        
        for client in clients:
            if len(client.remaining_offers) == 0:
                continue    # skip to the next client if this haven't no more remaining offers
            
            if folder:
                data = step_resolver(client, global_step_num, folder)
            else:  
                data = step_resolver(client, global_step_num)
            
            
            if data is not None:
                in_between_data[global_step_num] = global_results
                step_profit += data['step_profit']
                global_results[client.name] = data  

        total_profit += step_profit
        total_budget += step_profit

        # reallocate the budget
        in_between_data['step_allocation'] = allocation                 # come varia l'allocazione nel tempo?
        #allocation = budget_allocation(clients, total_budget)            # ridistribuiamo il budget che è stato guadagnato
        allocation = budget_allocation_new(clients, offer_occurrences, total_budget)            # ridistribuiamo il budget che è stato guadagnato

        # non è possibile completare nessun offerta più
        if step_profit == 0:
            break

        global_step_num += 1




    # EXITING CODE
    # COMPILE STATISTICS
    statistic = {
        'initial_data': {
        'num_clients': num_clients,
        'initial_budget': initial_budget,
        'total_offers_num': total_offers_num,
        'offer_occurrences': offer_occurrences,  # Dictionary to store the count of each offer name
        #'total_roi': total_roi,
        #'weights': weights,
        #'average_roi_per_client': avg_roi_per_client,
        #'budget_tracking': budget_tracking,
        #'expected_profit': expected_profit,
        },

        # in between data   
        'in_between_data': in_between_data,
        
        # final data
        'final_data': {
        'total_step_num': global_step_num,
        'final_budget': total_budget,
        'total_profit': total_budget - initial_budget,
        },
    }

    # SAVE STATISTICS
    save_stats_json(statistic, folder, filename='results.json')
    
    return statistic




