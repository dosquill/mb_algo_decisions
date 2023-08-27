from custom.OfferList import *
from custom.Offer import *

# binding Person to OfferList 
class Client:
    # TODO il cliente ha un budget, un guadagno e se è stato consigliato da qualcuno
    def __init__(self, person, offer_list, id, referred_by = None, commission = 0):
        self.person = person
        self.id = id
        self.remaining_offer_list = offer_list
        self.completed_offer_list = OfferList()
        self.referred_by = referred_by
        self.commission = commission


    # Other methods and attributes
    def __str__(self):
        return f"Client {self.id}\nPerson:\n{self.person}\nRemaining offer list:\n{self.remaining_offer_list}\nCompleted list:\n{self.completed_offer_list}"
    

    
    # GETTERS
    def get_remaining_list(self):
        return self.remaining_offer_list
    
    def get_completed_list(self):
        return self.completed_offer_list
    
    def get_name(self):
        return self.person.get_name()
    
    def get_id(self):
        return self.id
    
    def get_referred_by(self):
        return self.referred_by
    
    def get_commission(self):
        return self.commission
    


    # SETTERS
    def set_remaining_list(self, offer_list):
        self.remaining_offer_list = offer_list
    
    def set_referred_by(self, client):
        self.referred_by = client
    
    def set_commission(self, commission):
        self.commission = commission
    
    def set_id(self, id):
        self.id = id

    


    # ADDING
    def add_completed_offer(self, offer: Offer):
        self.completed_offer_list.add_item(offer)


    # OTHER METHODS
    def has_remaining_offer(self):
        if (len(self.remaining_offer_list) > 0):
            return True
        return False
    
    def refresh_remaining_list(self, offer_list: OfferList):
        self.remaining_offer_list = offer_list

