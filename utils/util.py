import os
import csv



# TODO cancellare tutta la cartella invece che i singoli file
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)



def print_step_details(step_result):
    print("Step Number:", step_result['step_num'])
    print("Profit:", step_result['profit'])
    print("Number of Offers:", step_result['num_offers'])
    print("Inutilized Budget Percentage:", step_result['inutilized_budget_percentage'])
    print("Remaining Budget:", step_result['remaining_budget'])
    print("Initial Budget:", step_result['initial_budget'])
    print()





def save_step_analysis_to_csv(step_results, csv_filename):
    if os.path.exists(csv_filename):
        existing_results = []
        with open(csv_filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_results = [row for row in reader]

        # Extract the completed offers from step_results
        completed_offers = step_results[0]['completed_offers'].get_list()  # Assuming step_results is a list of dictionaries

        # Compare the new results with existing data and append only unique results
        completed_offers = [offer for offer in completed_offers if offer not in existing_results]

    else:
        # If the CSV file doesn't exist, initialize completed_offers as an empty list
        completed_offers = []

    # Determine fieldnames based on whether there are completed offers or not
    fieldnames = completed_offers[0].keys() if completed_offers else []

    # Append new results to the existing data (if any)
    with open(csv_filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not os.path.exists(csv_filename):
            # Write header only if the file is empty
            writer.writeheader()

        for offer in completed_offers:
            writer.writerow(offer)




def save_step_analysis_to_csv(step_results, csv_directory):
    for step_num, step_result in enumerate(step_results, start=1):
        step_csv_filename = os.path.join(csv_directory, f"step_{step_num}_results.csv")

        if os.path.exists(step_csv_filename):
            existing_results = []
            with open(step_csv_filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                existing_results = [row for row in reader]

            completed_offers = step_result['completed_offers'].get_list()

            new_offers = []
            for offer in completed_offers:
                offer_dict = {
                    'bookmaker': offer.get_name(),
                    'earning': offer.get_earning(),
                    'budget_needed': offer.get_budget_needed(),
                    'roi': offer.get_roi(),
                    'time_needed': offer.get_time_needed(),
                    'completed': offer.get_completed(),
                    'step_num': offer.get_step_num()
                }
                new_offers.append(offer_dict)

            completed_offers = [offer for offer in new_offers if offer not in existing_results]
        else:
            completed_offers = []

        fieldnames = completed_offers[0].keys() if completed_offers else []

        with open(step_csv_filename, 'a', newline='') as csvfile:
            if not os.path.exists(step_csv_filename):
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for offer in completed_offers:
                writer.writerow(offer)



def save_overall_statistics_to_csv(results, csv_filename):
    csv_directory = os.path.dirname(csv_filename)
    create_directory(csv_directory)  # Create the directory if it doesn't exist

    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Statistic', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # FIXME come up with a better way to write the header
        writer.writeheader()

        num_steps = len(results)
        total_profit = sum(result['profit'] for result in results)
        inutilized_budget_percentages = [result['inutilized_budget_percentage'] for result in results]
        initial_budgets = [result['initial_budget'] for result in results]
        step_profits = [result['profit'] for result in results]
        num_offers_per_step = [result['num_offers'] for result in results]
        remaining_budgets = [result['remaining_budget'] for result in results]

        avg_inutilized_budget_percentage = sum(inutilized_budget_percentages) / num_steps
        avg_profit_for_step = sum(step_profits) / num_steps
        avg_num_offers_per_step = sum(num_offers_per_step) / num_steps
        avg_remaining_budget = sum(remaining_budgets) / num_steps

        max_step_profit = max(step_profits)
        min_step_profit = min(step_profits)
        max_inutilized_budget_percentage = max(inutilized_budget_percentages)
        min_inutilized_budget_percentage = min(inutilized_budget_percentages)
        max_num_offers_per_step = max(num_offers_per_step)
        min_num_offers_per_step = min(num_offers_per_step)
        max_remaining_budget = max(remaining_budgets)
        min_remaining_budget = min(remaining_budgets)

        statistics = [
            ('Number of steps', num_steps),
            ('Total profit', total_profit),
            ('Max step profit', max_step_profit),
            ('Average profit for step', avg_profit_for_step),
            ('Min step profit', min_step_profit),
            ('Max inutilized budget percentage', max_inutilized_budget_percentage),
            ('Average inutilized budget percentage', avg_inutilized_budget_percentage),
            ('Min inutilized budget percentage', min_inutilized_budget_percentage),
            ('Max number of offers in a step', max_num_offers_per_step),
            ('Average number of offers per step', avg_num_offers_per_step),
            ('Min number of offers in a step', min_num_offers_per_step),
            ('Max remaining budget', max_remaining_budget),
            ('Average remaining budget', avg_remaining_budget),
            ('Min remaining budget', min_remaining_budget)
        ]

        for stat_name, stat_value in statistics:
            writer.writerow({
                'Statistic': stat_name,
                'Value': stat_value
            })



def print_overall_statistics(results):
    num_steps = len(results)
    total_profit = sum(result['profit'] for result in results)
    inutilized_budget_percentages = [result['inutilized_budget_percentage'] for result in results]
    initial_budgets = [result['initial_budget'] for result in results]
    step_profits = [result['profit'] for result in results]
    num_offers_per_step = [result['num_offers'] for result in results]
    remaining_budgets = [result['remaining_budget'] for result in results]

    avg_inutilized_budget_percentage = sum(inutilized_budget_percentages) / num_steps
    avg_profit_for_step = sum(step_profits) / num_steps
    avg_num_offers_per_step = sum(num_offers_per_step) / num_steps
    avg_remaining_budget = sum(remaining_budgets) / num_steps

    max_step_profit = max(step_profits)
    min_step_profit = min(step_profits)
    max_inutilized_budget_percentage = max(inutilized_budget_percentages)
    min_inutilized_budget_percentage = min(inutilized_budget_percentages)
    max_num_offers_per_step = max(num_offers_per_step)
    min_num_offers_per_step = min(num_offers_per_step)
    max_remaining_budget = max(remaining_budgets)
    min_remaining_budget = min(remaining_budgets)

    print("Overall Statistics:")
    print("Number of steps:", num_steps)
    print("Total profit:", total_profit)
    print("Max step profit:", max_step_profit)
    print("Average profit for step:", avg_profit_for_step)
    print("Min step profit:", min_step_profit)
    print("Max inutilized budget percentage:", max_inutilized_budget_percentage)
    print("Average inutilized budget percentage:", avg_inutilized_budget_percentage)
    print("Min inutilized budget percentage:", min_inutilized_budget_percentage)
    print("Max number of offers in a step:", max_num_offers_per_step)
    print("Average number of offers per step:", avg_num_offers_per_step)
    print("Min number of offers in a step:", min_num_offers_per_step)
    print("Max remaining budget:", max_remaining_budget)
    print("Average remaining budget:", avg_remaining_budget)
    print("Min remaining budget:", min_remaining_budget)

    








""" def print_statistics(data, is_step_details=True):
    if is_step_details:
        print("Step Number:", data['step_num'])
        print("Profit:", data['profit'])
        print("Number of Offers:", data['num_offers'])
        print("Inutilized Budget Percentage:", data['inutilized_budget_percentage'])
        print("Remaining Budget:", data['remaining_budget'])
        print("Initial Budget:", data['initial_budget'])
    else:
        num_steps = len(data)
        total_profit = sum(result['profit'] for result in data)
        inutilized_budget_percentages = [result['inutilized_budget_percentage'] for result in data]
        # ... rest of the calculations ...

        print("Overall Statistics:")
        print("Number of steps:", num_steps)
        print("Total profit:", total_profit)
        # ... print other statistics ...

# Example usage for step details
step_result = {
    'step_num': 1,
    'profit': 100,
    'num_offers': 5,
    'inutilized_budget_percentage': 20,
    'remaining_budget': 500,
    'initial_budget': 600
}
print_statistics(step_result, is_step_details=True)

# Example usage for overall statistics
list_of_step_results = [step_result1, step_result2, step_result3]  # Your actual data
print_statistics(list_of_step_results, is_step_details=False)
 """