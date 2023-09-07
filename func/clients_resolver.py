from pprint import pprint
from utils.save_to_json import *
from func.step_resolver import step_resolver
from Class.budget_manager import BudgetManager
from Class.client import Client

# TODO offerte in percentuale
# TODO il fatto fondamentale è questo, l'algoritmo adesso va bene, ma deve considerare il fatto che il budget può essere sbilanciato per fare 


# part 3: risoluzione di un cliente
# Il cliente si risolve quando non ci sono più offerte da fare o quando il budget non è più sufficiente. Lo risolve per step
# step 4: risolutore di una lista di clienti
# prende una lista di clienti, un budget, alloca il budget per quei clienti e ne risolve uno step

def clients_resolver(clients_list: list, budget: float, folder: str = None) -> dict:

    bm = BudgetManager(budget, clients_list)
    initial_budget = bm.initial
    step_num = 1
    results = []

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



    if len(results) == 0:
        print("No results")
        return None







    # EXITING CODE
    # COMPILE STATISTICS
    # TODO vorrei poter suddividere le colonne che arrivano in min, max, avg
    # molte valori si ripetono quindi li assegno
    step_profits = [data['step_profit'] for data in results]
    remaining_budgets = [data['remaining_budget'] for data in results]
    num_completeds = [data['num_completed_offers'] for data in results]
    inutilized_budgets = [data['inutilized_budget_percentage'] for data in results]
    lenght = len(results)

    # devo aggiungere current budget
    statistics = {
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



        'total_profit': client.profit,
        'initial_budget': initial_budget,
        'num_steps': lenght,

        'step_profit': {
            'total': sum(step_profits),
            'max': max(step_profits),
            'avg': round((sum(step_profits) / lenght),2),
            'min': min(step_profits),
        },

        'remaining_budget': {
            'total': results[-1]['remaining_budget'],
            'max': max(remaining_budgets),
            'avg': round(sum(remaining_budgets) / lenght, 2),
            'min': min(remaining_budgets),
        },

        'num_completed_offers': {
            'total': sum(num_completeds),
            'max': max(num_completeds),
            'avg': round((sum(num_completeds) / lenght),2),
            'min': min(num_completeds),
        },

        'inutilized_budget_percentage': {
            'total': results[-1]['inutilized_budget_percentage'],
            'max': max(inutilized_budgets),
            'avg': round(sum(inutilized_budgets) / lenght, 2),
            'min': min(inutilized_budgets),
        },

        'num_offers_per_step':{
            'max': max(num_completeds),
            'avg': round((sum(num_completeds) / lenght),2),
            'min': min(num_completeds),

        },
        
        # TODO
        'commission': round(client.profit * 0.2, 1) ,
    }



    if client.referred_by is not None:
        statistics['referral'] = round(client.profit * 0.05, 1)
        statistics['total_commission'] = statistics['commission'] + statistics['referral']



    # SAVE STATISTICS
    pprint(statistics)
    save_stats_json(statistics, folder, filename=f'/stats.json')

    return statistics






