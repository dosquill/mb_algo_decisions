import csv
import json
from offer import Offer

class Client:
    def __init__(self, name: str, surname: str, id: int, file_path: str, referred_by = "", budget = 0, profit = 0, commission = 0):
        # mandatory parameters
        self.name = name
        self.surname = surname
        self.id = id
        self.file_path = file_path
        
        # optional parameters
        self.referred_by = referred_by
        self.budget = budget                        # allocated budget
        self.profit = profit                             # profit counter
        self.completed_offers = []
        self.remaining_offers = self.load_file()
        self.commission = commission




    # OVERLOADING
    # toString
    def __str__(self):
        return f"Client {self.id}\nName: {self.name}\nSurname: {self.surname}\nReferred by: {self.referred_by}\nCommission: {self.commission}\n"


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



    
    

    # @property
    # def commission(self):
    #     return self.__commission
    # 
    # @commission.setter
    # def commission(self, value):
    #     if not isinstance(value, float):
    #         raise TypeError("Commission of a Client should be only a float")
    #     if value < 0:
    #         raise ValueError("Commission can't be negative")
    #     self.__commission = value
    # 



    # OTHER METHODS
    def load_file(self) -> list:
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


