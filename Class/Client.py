from Class.OfferList import *
from Class.Offer import *

class Client:
    def __init__(self, person, offer_list, id):
        self.person = person
        self.id = id
        self.remaining_offer_list = offer_list
        self.completed_offer_list = OfferList()


    # Other methods and attributes
    def __str__(self):
        return f"Client {self.id}\nPerson:\n{self.person}\nRemaining offer list:\n{self.remaining_offer_list}\nCompleted list:\n{self.completed_offer_list}"
    
    def add_completed_offer(self, offer: Offer):
        self.completed_offer_list.add_item(offer)

    def has_remaining_offer(self):
        if (len(self.remaining_offer_list) > 0):
            return True
        return False
    
    def refresh_remaining_list(self, offer_list: OfferList):
        self.remaining_offer_list = offer_list

    def get_remaining_list(self):
        return self.remaining_offer_list