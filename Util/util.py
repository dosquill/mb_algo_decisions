import os
import json


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



def statistics(name, budget, profit, num_offers, completed_offers, remaining_offers, remaining_budget, inutilized_budget_percentage, step_num):
    print(f'{name} statistics:')

    # offer
    print(f'Total offers:\n{remaining_offers}' )
    print(f'Completed list:\n{completed_offers}')

    # statistics
    print(f'Step: {step_num}')
    print(f'Remaining budget: {remaining_budget}€')
    print(f'Initial budget: {budget}€')
    print(f'Profit: {profit}€')
    print(f'Number of offers: {num_offers}')
    print(f'Inutilized budget percentage: {inutilized_budget_percentage}%')

    # create a CSV file
    csv_filename = f'{name}_statistics.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write headers
        csv_writer.writerow(['Statistic', 'Value'])
        
        # Write data
        csv_writer.writerow(['Step', step_num])
        csv_writer.writerow(['Name', name])
        csv_writer.writerow(['Remaining budget (€)', remaining_budget])
        csv_writer.writerow(['Initial budget (€)', budget])
        csv_writer.writerow(['Profit (€)', profit])
        csv_writer.writerow(['Number of offers', num_offers])
        csv_writer.writerow(['Inutilized budget percentage (%)', inutilized_budget_percentage])
