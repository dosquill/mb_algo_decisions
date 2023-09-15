from pprint import pprint
from utils.save_to_json import *
from func.step_resolver import step_resolver
from utils.util import *
from Class.budget_manager import BudgetManager

# TODO offerte in percentuale
# TODO expected_profit = total_budget * total_roi
# dati iniziali quanti ce ne sono di offerte totali, dati finali di quante ne sono state fatte in totale

# step 3: risolutore di una lista di clienti
# Il cliente si risolve quando non ci sono più offerte da fare o quando il budget non è più sufficiente. Lo risolve per step
# prende una lista di clienti, un budget, alloca il budget per quei clienti e ne risolve uno step

def clients_resolver(clients_list: list, budget: float, folder: str = None) -> dict:
    # PRINCIPAL CHECKS
    # innanzitutto, controlla quanti clienti ci sono
    num_clients = len(clients_list)
    if num_clients == 0:
        print("No clients")
        return None



    # INITIAL DATA
    bm = BudgetManager(budget, clients_list)
    initial_budget = bm.initial_budget
    total_offers_num = sum([len(client.remaining_offers) for client in clients_list])
    offer_occurrences = offer_occurrences_dict(clients_list)
    pprint(offer_occurrences)
    
    # counter
    global_step_num = 1
    total_profit = 0
    total_budget = 0
    num_offers = 0

    # 
    results = []
    in_between_data = {}
    global_results = {}



    # ALGORITHM
    # finché non è step resolver mi da qualcosa
    while num_offers < total_offers_num: 
        step_profit = 0
        
        if folder:
            data = step_resolver(clients_list=clients_list, bm=bm, step_num=global_step_num, folder=folder)
        else:  
            data = step_resolver(clients_list=clients_list, bm=bm, step_num=global_step_num)
        
        if data is not None:
            results.append(data)
            in_between_data[global_step_num] = global_results
            step_profit += data['step_profit']
            # global_results[client.name] = data  

        total_profit += step_profit
        total_budget += step_profit

        # TODO come varia l'allocazione nel tempo?
        # reallocate the budget for the next step
        # in_between_data['step_allocation'] = allocation                 
        #bm.allocate()

        # non è possibile completare nessun offerta più
        if step_profit == 0:
            break

        global_step_num += 1



    if len(results) == 0:
        print("No results")
        return None



    # EXITING CODE
    # COMPILE STATISTICS
    step_profits = [data['step_profit'] for data in results]
    # TODO remaining_budgets = [data['remaining_budget'] for data in results]
    num_completeds = [data['num_completed_offers'] for data in results]
    inutilized_budgets = [data['inutilized_budget_percentage'] for data in results]
    lenght = len(results)

    # TODO devo aggiungere current budget
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



        'in_between_data': {
            'step_profit': {
                'total': sum(step_profits),
                'max': max(step_profits),
                'avg': round((sum(step_profits) / lenght),2),
                'min': min(step_profits),
            },

            # TODO
            #'remaining_budget': {
            #    'total': results[-1]['remaining_budget'],
                #'max': max(remaining_budgets),
                #'avg': round(sum(remaining_budgets) / lenght, 2),
                #'min': min(remaining_budgets),
            #},

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
        },


        
        'final_data': {
            'total_step_num': global_step_num,
            'final_budget': total_budget,
            'total_profit': total_budget - initial_budget,
            'total_profit': total_budget,
            'initial_budget': initial_budget,
            'num_steps': lenght,
            'total_offers_done': sum(num_completeds),
            # TODO occurrence per offers done
            # TODO per cliente quindi client1 = tot , client2 tot
            #'commission': round(client.profit * 0.2, 1) ,
            },
    }


    # TODO
    # calcola qui le commissioni
    # if client.referred_by is not None:
    #     statistics['referral'] = round(client.profit * 0.05, 1)
    #     statistics['total_commission'] = statistics['commission'] + statistics['referral']


    # SAVE STATISTICS
    pprint(statistics)
    save_stats_json(statistics, folder, filename=f'/stats.json')

    return statistics






