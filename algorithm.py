from client import Client
from offer import Offer
from utils import *


# part 1 of algorithm: offer resolution
def offer_resolution(client: Client, offer: Offer, folder: str) -> bool:
    initial_budget = client.budget

    if not client.budget >= offer.budget_needed:
        client.remaining_offers.append(offer)
        return None
    
    client.completed_offers.append(offer)
    client.budget -= offer.budget_needed

    statistics = {
        'client_name': client.name,
        'offer_name': offer.name,
        'initial_budget': initial_budget,
        'budget_needed': offer.budget_needed,
        'remaining_budget': client.budget,
        'profit': offer.profit,
    }

    print(statistics)
    #save_to_csv(statistics, f'{folder}/{offer.name}statistics.csv')

    return statistics

    





""" 
# part 2 of algorithm: step resolution
def step_resolution(client: Client, offer: Offer, budget: float, current_step_num: int = 1, folder: str = None) -> dict:
    offer_resolutions = []
    initial_budget = budget
    profit = 0
    num_completed_offers = 0
    csv_file = f'{folder}/step_{current_step_num}.csv'

    for offer in client.remaining_list():
        offer_resolution(client, offer, folder)

    if num_completed_offers == 0:
        raise Exception('No offers can be completed with the given budget')

    budget = total_profit

    statistic = {
        'step_num': current_step_num,
        'total_profit': total_profit,
        'num_completed_offers': num_completed_offers,
        'inutilized_budget_percentage': round((budget / initial_budget) * 100, 2),
        'remaining_budget': budget,
        'initial_budget': initial_budget,
        'completed_offers': completed_offers,
        'remaining_offers': remaining_offers
    }


    #    print("Step Number:", results['step_num'])
    #    print("Total Profit:", results['total_profit'])
    #    print("Number of Completed Offers:", results['num_completed_offers'])
    #    print("Inutilized Budget Percentage:", results['inutilized_budget_percentage'])
    #    print("Remaining Budget:", results['remaining_budget'])
    #    print("Initial Budget:", results['initial_budget'])
    #    print() 

    print(statistic)
    save_to_csv(statistic, csv_file) 

    return statistic


 """




""" 

# part 3 of algorithm: client resolution
def client_resolution(client, budget):
    initial_budget = budget
    step_num = 1
    step_results = []

    folder = f'results/{client.get_name()}/'
    csv_file = f'{folder}/overall.csv'


    while (client.has_remaining_offer()):
        step_result = step_resolution(client, initial_budget, step_num, folder)
        step_results.append(step_result)
        step_num += 1



    statistics = {
        'total_profit': sum(result['total_profit'] for result in step_results),
        'inutilized_budget_percentage': sum(result['inutilized_budget_percentage'] for result in step_results) / len(step_results),
        'initial_budget': initial_budget,
        'remaining_budget': step_results[-1]['remaining_budget'],
        'num_steps': len(step_results),
        'num_completed_offers': sum(result['num_completed_offers'] for result in step_results),
        'num_offers_per_step': [result['num_completed_offers'] for result in step_results],
        'remaining_offers': step_results[-1]['remaining_offers'],
        'completed_offers': step_results[-1]['completed_offers']
    }


    # cosa voglio printare

    #    print("Overall Statistics:")
    #    print("Number of steps:", num_steps)
    #    print("Total profit:", total_profit)
    #    print("Max step profit:", max_step_profit)
    #    print("Average profit for step:", avg_profit_for_step)
    #    print("Min step profit:", min_step_profit)
    #    print("Max inutilized budget percentage:", max_inutilized_budget_percentage)
    #    print("Average inutilized budget percentage:", avg_inutilized_budget_percentage)
    #    print("Min inutilized budget percentage:", min_inutilized_budget_percentage)
    #    print("Max number of offers in a step:", max_num_offers_per_step)
    #    print("Average number of offers per step:", avg_num_offers_per_step)
    #    print("Min number of offers in a step:", min_num_offers_per_step)
    #    print("Max remaining budget:", max_remaining_budget)
    #    print("Average remaining budget:", avg_remaining_budget)
    #    print("Min remaining budget:", min_remaining_budget)




    #TODO scrivere qui il guadagno del cliente e il nostro guadagno
    # scrivi fattura, cliente 20%, se è stato raccomandato 5% a chi ha raccomandato
    # scrivi utile e lordo

    print(step_results)
    save_to_csv(statistics, csv_file)

    return step_results




 """





""" 
# final algorithm
# prende una lista di clienti, un budget e mi da la tabella di quali offerte fare e quando
# TODO

def algorithm(clients, budget) -> dict:
    pass
 """