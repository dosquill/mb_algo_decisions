from ..sql.save_sqlite import save_to_sqlite


def offer_converter():
    db_path = "db/offer/data.db"
    id_sheet = "1-rFtK4AnZ8TPSbGDGwV-UiaPfaUyqDijhe5CDQSzxtQ"
    nome = "Offerte"
    range = "A:Z"

    save_to_sqlite(id_sheet, nome, range, db_path)