import os
from Class.offer import Offer
from Class.client import Client

def basic_operation(folder, filename):
    # se la cartella non esiste, vuol dire che non avevo intenzione di salvare i dati
    if folder is None:
        return None

    path = f'{folder}/{filename}'

    # se la cartella non esiste, creala
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # se quel file esiste già cancellalo
    if os.path.exists(path):
        os.remove(path)
    
    return path




# TODO non si avvale di stampare le statistiche di client resolver
# Dictionary che conta quante volte, in totale, l'offerta verrà proposta
def offer_occurrences_dict(clients: list) -> dict:
    offer_occurrences = {}  
    for client in clients:
        for offer in client.remaining_offers:
            # Increment the count for this offer name in the dictionary
            offer_name = offer.name  # Assuming the Offer class has a 'name' attribute
            if offer_name in offer_occurrences:
                offer_occurrences[offer_name] += 1
            else:
                offer_occurrences[offer_name] = 1
    return offer_occurrences



def find_minimum_budget_required(clients: list) -> float:
    min_budget = float('inf')  # Initialize with infinity
    
    for client in clients:
        for offer in client.remaining_offers:
            if offer.budget_needed < min_budget:
                min_budget = offer.budget_needed
    
    return min_budget if min_budget != float('inf') else 0  # Return 0 if no offers are found





def found_offer_by_name(client: Client, offer_name: str) -> Offer:
    for offer in client.remaining_offers:
        if offer.name == offer_name:
            return offer
    return None




def collect_python_files_to_txt(starting_directory, output_filename):
    with open(output_filename, 'w') as output_file:
        for root, dirs, files in os.walk(starting_directory):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r') as py_file:
                        output_file.write(f"===== {filepath} =====\n")
                        output_file.write(py_file.read())
                        output_file.write("\n\n")



if __name__ == "__main__":
    starting_directory = "."  # la directory di partenza è la directory corrente
    output_filename = "all_python_files.txt"
    
    collect_python_files_to_txt(starting_directory, output_filename)