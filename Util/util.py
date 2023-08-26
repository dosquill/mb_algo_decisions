import os
import json
import csv


def crea_file_finale(data):
    json_filename = 'resoconto.json'

    # Delete the JSON file if it exists
    if os.path.exists(json_filename):
        os.remove(json_filename)
        print(f"Existing JSON file '{json_filename}' has been deleted.")

    
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print(f"JSON file '{json_filename}' has been created.")



def is_file(path):
    if os.path.isfile(path):
        print(f"{path} is a file.")
    else:
        print(f"{path} is not a file.")


def is_dir(path):
    if os.path.isdir(path):
        print(f"{path} is a directory.")
    else:
        print(f"{path} is not a directory.")




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

    

def print_step_details(step_result):
    print("Step Number:", step_result['step_num'])
    print("Profit:", step_result['profit'])
    print("Number of Offers:", step_result['num_offers'])
    print("Inutilized Budget Percentage:", step_result['inutilized_budget_percentage'])
    print("Remaining Budget:", step_result['remaining_budget'])
    print("Initial Budget:", step_result['initial_budget'])
    print()



def save_steps_results_to_csv(results, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Step Number', 'Profit', 'Number of Offers', 'Inutilized Budget Percentage', 'Remaining Budget', 'Initial Budget']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()

        for result in results:
            writer.writerow({
                'Step Number': result['step_num'],
                'Profit': result['profit'],
                'Number of Offers': result['num_offers'],
                'Inutilized Budget Percentage': result['inutilized_budget_percentage'],
                'Remaining Budget': result['remaining_budget'],
                'Initial Budget': result['initial_budget']
            })


# Define the function to create directories if they don't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)



def save_overall_statistics_to_csv(results, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Statistic', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
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
