from Class.Person import *
from Class.Offer import *
from Class.OfferList import *
from Class.Client import *
from Util.util import *
import copy

def algorithm_step(client, budget_counter, step_num):
    step_results = []

    while (client.has_remaining_offer()):
        initial_budget = budget_counter
        profit = 0
        num_offers = 0
        list_completed_offers_step = OfferList()
        list_offers_lefted_step = OfferList()

        for offer in client.get_remaining_list():
            if (budget_counter >= offer.get_budget_needed()):
                budget_counter -= offer.get_budget_needed()
                profit += offer.get_earning()
                num_offers += 1
                list_completed_offers_step.add_item(offer)
                client.add_completed_offer(offer)
            else:
                list_offers_lefted_step.add_item(offer)

        inutilized_budget_percentage = round((budget_counter / initial_budget) * 100, 2)

        if (num_offers == 0):
            raise Exception('No offers can be completed with the given budget')

        step_result = {
            'step_num': step_num,
            'profit': profit,
            'num_offers': num_offers,
            'inutilized_budget_percentage': inutilized_budget_percentage,
            'remaining_budget': budget_counter,
            'initial_budget': initial_budget,
            'completed_offers': list_completed_offers_step,
            'remaining_offers': list_offers_lefted_step
        }

        print_step_details(step_result) 


        client.refresh_remaining_list(list_offers_lefted_step)
        budget_counter = initial_budget + profit
        step_results.append(copy.deepcopy(step_result))
        step_num += 1

    ### Save step results to CSV
    client_folder = f"results/{client.get_name()}"  # Modify this to get the client's name
    create_directory(client_folder)  # Create the client's folder if it doesn't exist

    step_filename = f"{client_folder}/step_results.csv"
    save_steps_results_to_csv(step_results, step_filename)
    ### 

    return step_results



def algorithm(client, total_budget):
    step_num = 1
    list_of_step_results = []

    while (client.has_remaining_offer()):
        step_results = algorithm_step(client, total_budget, step_num)
        list_of_step_results.extend(step_results)
        
    print_overall_statistics(list_of_step_results)
    save_overall_statistics_to_csv(list_of_step_results, f"results/{client.get_name()}/overall_statistics.csv")

    return list_of_step_results

