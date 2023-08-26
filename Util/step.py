from Class.Client import *
from Class.Offer import *
from Class.OfferList import *
from Util.util import *
from Util.step import *


def algo(client, total_offer, total_budget):
    step_num = 1
    list_results = []

    ## STEP
    while (len(total_offer) > 0):
        print(f'STEP {step_num}:')

        ## TOTAL COUNTER
        initial_budget = total_budget
        profit = 0
        num_offers = 0
        completed_offers = OfferList()
        remaining_offer = OfferList()
        
        for offer in total_offer:
            if (total_budget >= offer.budget_needed):
                total_budget -= offer.budget_needed
                profit += offer.earning
                num_offers += 1
                completed_offers.add_item(offer)
            else:
                remaining_offer.add_item(offer)

        inutilized_budget_percentage = round((total_budget / initial_budget) * 100, 2)         # round inutilized_budget_percentage to 2 decimal places

        if (num_offers == 0):
            raise Exception('No offers can be completed with the given budget')

        
        statistics = {
            'step_num': step_num,
            'profit': profit,
            'num_offers': num_offers,
            'inutilized_budget_percentage': inutilized_budget_percentage,
            'remaining_budget': total_budget,
            'initial_budget': initial_budget,
            }
        
        total_offer = remaining_offer
        total_budget = initial_budget + profit
        list_results.append(statistics)
        step_num += 1
       
        print('Completed Offers:') 
        print(completed_offers)
        print(f'{statistics}')
        print('Remaining Offers:')
        print(remaining_offer)
        print('\n')
    ## END STEP

    print_statistics(list_results)

    return list_results


    

def print_statistics(results):
    num_steps = len(results)
    total_profit = sum(result['profit'] for result in results)
    inutilized_budget_percentages = [result['inutilized_budget_percentage'] for result in results]
    profit_for_step = [result['profit'] for result in results]
    step_profits = [result['profit'] for result in results]
    initial_budgets = [result['initial_budget'] for result in results]
    step_profits = [result['profit'] for result in results]

    avg_inutilized_budget_percentage = sum(inutilized_budget_percentages) / num_steps
    avg_profit_for_step = sum(profit_for_step) / num_steps

    max_step_profit = max(step_profits)
    min_step_profit = min(step_profits)
    max_inutilized_budget_percentage = max(inutilized_budget_percentages)
    min_inutilized_budget_percentage = min(inutilized_budget_percentages)
    min_initial_budget = min(initial_budgets)

    print("Statistics:")
    print("Number of steps:", num_steps)
    print("Total profit:", total_profit)
    print("Max step profit:", max_step_profit)
    print("Average profit for step:", avg_profit_for_step)
    print("Min step profit:", min_step_profit)
    print("Max inutilized budget percentage:", max_inutilized_budget_percentage)
    print("Average inutilized budget percentage:", avg_inutilized_budget_percentage)
    print("Min inutilized budget percentage:", min_inutilized_budget_percentage)
    print("Budget started:", min_initial_budget)
    print("Budget now:", min_initial_budget + total_profit)
