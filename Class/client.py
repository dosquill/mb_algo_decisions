import json
from .offer import Offer

# non esiste un cliente senza una lista di offerte da completare. La lista può essere vuota, ma esiste
class Client:
    def __init__(self, name: str, surname: str, id: int, file_path: str, referred_by = ""):
        # mandatory parameters
        self.name = name
        self.surname = surname
        self.id = id
        self.file_path = file_path
        
        # optional parameters
        self.referred_by = referred_by
        self.completed_offers = []
        self.remaining_offers = self.load_offers_from_file()
        self.commission = 0




    # OVERLOADING
    # toString
    def __str__(self):
        return f"Client {self.id}\nName: {self.name}\nSurname: {self.surname}\nReferred by: {self.referred_by}\nCommission: {self.commission}\nBudget: {self.budget}\nProfit: {self.profit}\n"


        # Make the class iterable over its remaining_offers
    def __iter__(self):
        self._iter_idx = 0  # Initialize an index for iteration
        return self
    

    def __next__(self):
        if self._iter_idx < len(self.remaining_offers):
            offer = self.remaining_offers[self._iter_idx]  # Fetch the current offer
            self._iter_idx += 1  # Increment the index
            return offer
        else:
            raise StopIteration  # Stop the iteration when we've gone through all remaining_offers



    # GETTERS AND SETTERS
    @property 
    def name(self):
        return self.__name

    # NAME
    @name.setter
    def name(self, value):
        value_name = 'Name'
        if not isinstance(value, str):
            raise Exception(f"{value_name} must be a string.")
        if value == '':
            raise Exception(f"{value_name} be empty.")
        if value == None:
            raise Exception(f"{value_name} cannot be None.")
        self.__name = value.capitalize()

    
    
    # SURNAME
    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, value):
        value_name = 'Surname'
        if not isinstance(value, str):
            raise Exception(f"{value_name} must be a string.")
        if value == '':
            raise Exception(f"{value_name} be empty.")
        if value == None:
            raise Exception(f"{value_name} cannot be None.")
        self.__surname = value.capitalize()




    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        value_name = 'Id'
        if not isinstance(value, int):
            raise Exception(f"{value_name} of a Client should be only a number")
        if isinstance(value, bool):
            raise Exception(f"{value_name} of a Client should be only a boolean")
        if value == None:
            raise Exception(f"{value_name} of a Client should not be None")
        if value < 0:
            raise Exception(f"{value_name} can't be negative")
        self.__id = value



    

    # OTHER METHODS
    def load_offers_from_file(self) -> list:
        list_offer = []
        with open(self.file_path, 'r') as json_file:
            data = json.load(json_file)
            i = 0
            
            for offer in data:
                offer = Offer(data[i]['bookmaker'], data[i]['earning'], data[i]['budget_needed'], data[i]['time_needed'])
                list_offer.append(offer)
                i+=1

        #sort list by roi
        list_offer.sort(key=lambda x: x.roi, reverse=True)

        return list_offer        
    

    
    def calculate_average_roi(self):
        total_roi = sum(offer.roi for offer in self.remaining_offers)
        return round(total_roi / len(self.remaining_offers), 2) if len(self.remaining_offers) != 0 else 0



    def check_offer(self, offer: Offer) -> bool:
        if offer in self.remaining_offers:
            return True
        return False


    def find_by_name(self, name: str) -> Offer:
        for offer in self.remaining_offers:
            if offer.name == name:
                return offer
        return None


