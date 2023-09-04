from pprint import pprint
from Class.client import Client
from utils.util import *
from func.offer_resolver import *
from func.step_resolver import *




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






