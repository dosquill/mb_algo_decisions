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

