from ..sql.save_sqlite import save_to_sqlite


def form_converter():
    db_path = "db/form/data.db"
    id_sheet = "1Fl8tSpBjKQt4yn2CFlC-i-Lg948PbtCksaRNQW4r9rw"
    nome_sheet = "risposte_form"
    range = "A:Z"

    save_to_sqlite(id_sheet, nome_sheet, range, db_path)