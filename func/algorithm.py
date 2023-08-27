from datetime import datetime
from custom.Person import *
from custom.Offer import *
from custom.OfferList import *
from custom.Client import *
from utils.util import *
import os
import copy

folder_name = "target"

def algorithm_step(client, budget_counter, step_num):
    list_step_result = []
    # Define a default folder_name
    folder_name = "results"


    if step_num == 1:
        folder_name = "results"  # Default folder name
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        if not os.path.exists(f'{folder_name}/{client.get_name()}'):
            os.makedirs(f'{folder_name}/{client.get_name()}')


    while (client.has_remaining_offer()):
        initial_budget = budget_counter
        profit = 0
        num_offers = 0
        list_completed_offers_step = OfferList()
        list_offers_lefted_step = OfferList()

        # Before writing to the file, make sure the directory exists
        csv_directory = f'{folder_name}/{client.get_name()}'
        create_directory(csv_directory)  # Ensure the directory structure exists

        for offer in client.get_remaining_list():
            if (budget_counter >= offer.get_budget_needed()):
                budget_counter -= offer.get_budget_needed()
                profit += offer.get_earning()
                num_offers += 1
                list_completed_offers_step.add_item(offer)
                client.add_completed_offer(offer)
                offer.set_step_num(step_num)
                offer.save_to_csv(f'{folder_name}/{client.get_name()}/step_analysis.csv')
            else:
                list_offers_lefted_step.add_item(offer)


        if (num_offers == 0):
            raise Exception('No offers can be completed with the given budget')


        step_result = {
            'step_num': step_num,
            'profit': profit,
            'num_offers': num_offers,
            'inutilized_budget_percentage': round((budget_counter / initial_budget) * 100, 2),
            'remaining_budget': budget_counter,
            'initial_budget': initial_budget,
            'completed_offers': list_completed_offers_step,
            'remaining_offers': list_offers_lefted_step
        }


        # for next step
        client.refresh_remaining_list(list_offers_lefted_step)
        budget_counter = initial_budget + profit
        list_step_result.append(copy.deepcopy(step_result))
        step_num += 1

        print_step_details(step_result) 
        folder_name = "results"  # Update this line to use the correct folder name
        save_step_analysis_to_csv(list_step_result, f'{folder_name}/{client.get_name()}')


    return list_step_result



def client_result(client, total_budget):
    step_num = 1
    list_of_step_results = []

    while (client.has_remaining_offer()):
        step_result = algorithm_step(client, total_budget, step_num)
        list_of_step_results.extend(step_result)
        
    #TODO scrivere qui il guadagno del cliente e il nostro guadagno
    
    print_overall_statistics(list_of_step_results)
    save_step_analysis_to_csv(list_of_step_results, f"results/{client.get_name()}")
    save_overall_statistics_to_csv(list_of_step_results, f"results/{client.get_name()}/overall_statistics.csv")

    return list_of_step_results


# TODO
def algorithm():
    # scrivi fattura, cliente 20%, se è stato raccomandato 5% a chi ha raccomandato
    # scrivi utile e lordo
    
    pass
