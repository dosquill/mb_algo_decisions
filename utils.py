import os
import csv


def save_to_csv(statistics, file_path):
    fieldnames = statistics.keys()

    # se la cartella non esiste creala
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # se quel file esiste già cancellalo
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()  # Write header only if the file is empty
        writer.writerow(statistics)

