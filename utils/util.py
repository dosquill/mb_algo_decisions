import os

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