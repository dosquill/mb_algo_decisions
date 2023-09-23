# Main file for the project
from ..Class.client import Client 
from .clients_resolver import *
from .offer_resolver import *
from .step_resolver import *
from .clients_resolver import *
from ..utils.util import *
from ..db.form.converter import *
from ..db.offer.methods import *



def algorithm():
    form_converter()
    offer_converter()

    clients_resolver()
