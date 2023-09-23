# Main file for the project
from Class.client import Client 
from func.clients_resolver import *
from func.offer_resolver import *
from func.step_resolver import *
from func.clients_resolver import *
from utils.util import *

from google_sheet.service import google_service

# mb-algorithm@form-endpoint.iam.gserviceaccount.com

# INPUT
form_sheet = "1Fl8tSpBjKQt4yn2CFlC-i-Lg948PbtCksaRNQW4r9rw"
offerte_sheet = "1-rFtK4AnZ8TPSbGDGwV-UiaPfaUyqDijhe5CDQSzxtQ"


# google_service(form_sheet, "risposte_form", "A:Z", "./prova.json")
google_service(offerte_sheet, "Offerte", "A:Z", "./prova.json")
