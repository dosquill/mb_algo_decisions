import sqlite3
from ..sql.save_sqlite import save_to_sqlite
from ...Class.client import Client


def offer_converter():
    db_path = "db/offer/all_offer.db"
    id_sheet = "1-rFtK4AnZ8TPSbGDGwV-UiaPfaUyqDijhe5CDQSzxtQ"
    nome = "Offerte"
    range = "A:Z"

    save_to_sqlite(id_sheet, nome, range, db_path)



def offer_already_done(client: Client):
    conn = sqlite3.connect("db/offer/all_offer.db")
    c = conn.cursor()

    c.execute(f"SELECT * FROM Offerte WHERE Nome = '{client.name}' AND Cognome = '{client.surname}'")
    data = c.fetchall()

    

    conn.close()

    return data