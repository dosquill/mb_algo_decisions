from pprint import pprint
from Class.client import Client
from utils.saving_stats import *
from func.offer_resolver import *
from func.step_resolver import *




# part 3: risoluzione di un cliente
# Il cliente si risolve quando non ci sono più offerte da fare o quando il budget non è più sufficiente. Lo risolve per step
def client_resolver(client: Client, folder: str = None) -> dict:
    initial_budget = client.budget
    step_num = 1
    results = []


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
        
        'commission': round(client.profit * 0.2, 1) ,
    }


    if client.referred_by is not None:
        statistic['referral'] = round(client.profit * 0.05, 1)
        statistic['total_commission'] = statistic['commission'] + statistic['referral']


    # print(statistic)
    #save_to_csv(statistic, folder, filename='/overall.csv')
    save_stats_json(statistic, folder, filename=f'/{client.name}/stats.json')

    return statistic






