import os
import csv




def save_to_csv(statistics, file_path):
    fieldnames = statistics.keys()

    # se quel file esiste già cancellalo
    if os.path.exists(file_path):
        os.remove(file_path)
    
    with open(file_path, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if csv_file.tell() == 0:  # Check if the file is empty
            writer.writeheader()  # Write header only if the file is empty
        writer.writerow(statistics)
