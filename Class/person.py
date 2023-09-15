# TODO class person, in futuro 

class Person:
    def __init__(self, nome, cognome, genere, eta, data_nascita, num_telefono, email, indirizzo, citta, cap ):
        self.data_submit = None
        self.nome = nome
        self.cognome = cognome
        self.genere = genere
        self.data_nascita = data_nascita
        self.num_telefono = num_telefono
        self.email = email
        self.registrazione_precedente = False
        self.eta = eta
        self.siti_registrati = None
        self.resizenza_domicilio_coicidono = True
        self.indirizzo = indirizzo
        self.citta = citta
        self.cap = cap
        self.link_documento_fronte = None
        self.link_documento_retro = None
        self.link_secondo_doc_fronte = None
        self.link_secondo_doc_retro = None
        self.carta_utilizzata = None
        self.referred_by = None


    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"