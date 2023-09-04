import os
import csv
import json


def basic_operation(folder, filename):
    # se la cartella non esiste, vuol dire che non avevo intenzione di salvare i dati
    if folder is None:
        exit()

    path = f'{folder}/{filename}'

    # se la cartella non esiste, creala
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # se quel file esiste già cancellalo
    if os.path.exists(path):
        os.remove(path)
    
    return path






def save_to_csv(statistics, folder, filename):
    file_path = basic_operation(folder, filename)
    
    fieldnames = statistics.keys()

    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()  # Write header only if the file is empty
        writer.writerow(statistics)







# better way to print
def save_stats(statistic, folder, filename):
    path = basic_operation(folder, filename)
    
    # Crea un dizionario per raccogliere i dati per le colonne Min, Max e Avg
    stats_dict = {}


    # Estrai i dati dal dizionario statistic e riempi il dizionario stats_dict
    for param, value in statistic.items():
        if param.startswith('min_'):
            param_name = param[4:]
            if param_name not in stats_dict:
                stats_dict[param_name] = {'Min': value, 'Max': 'N/A', 'Avg': 'N/A'}
            else:
                stats_dict[param_name]['Min'] = value
        elif param.startswith('max_'):
            param_name = param[4:]
            if param_name not in stats_dict:
                stats_dict[param_name] = {'Min': 'N/A', 'Max': value, 'Avg': 'N/A'}
            else:
                stats_dict[param_name]['Max'] = value
        elif param.startswith('avg_'):
            param_name = param[4:]
            if param_name not in stats_dict:
                stats_dict[param_name] = {'Min': 'N/A', 'Max': 'N/A', 'Avg': value}
            else:
                stats_dict[param_name]['Avg'] = value

    # Crea il file CSV e scrivi i dati
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Scrivi l'intestazione (nomi delle colonne)
        writer.writerow(['Parameter', 'Min', 'Max', 'Avg'])

        # Scrivi i dati
        for param, values in stats_dict.items():
            writer.writerow([param, values['Min'], values['Max'], values['Avg']])







def save_stats_json(statistic, folder, filename):
    path = basic_operation(folder, filename)

    with open(path, 'w') as outfile:
        json.dump(statistic, outfile, indent=4, sort_keys=True)
