import csv
import json
from offer import Offer

class Client:
    # TODO il cliente ha un budget, un guadagno e se è stato consigliato da qualcuno
    def __init__(self, name: str, surname: str, id: int, referred_by = "", commission = 0, file_path = None):
        self.name = name
        self.surname = surname
        self.id = id
        self.referred_by = referred_by
        self.commission = commission
        self.completed_offers = []
        self.file_path = file_path
        self.budget = 0  # allocated budget
        
        if file_path is not None:
            self.remaining_offers = self.load_file()
        else:
            self.remaining_offers = []  
            self.file_path = None




    # OVERLOADING
    # toString
    def __str__(self):
        return f"Client {self.id}\nName: {self.name}\nSurname: {self.surname}\nReferred by: {self.referred_by}\nCommission: {self.commission}\nCompleted offers: {self.completed_offers}\nRemaining offers: {self.remaining_offers}\n"


    # GETTERS AND SETTERS
    """     
    @property 
    def name(self):
        return self.__name

    # NAME
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name of a Client should be only a string")
        if len(value)== 0 :
            raise TypeError("Name can't be empty")
        if not value.isalpha():
            raise ValueError("Name can't be a number")
        self.__name = value.capitalize()

    

    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError("Surname of a Client should be only a string")
        if len(value)== 0 :
            raise TypeError("Surname can't be empty")
        if not value.isalpha():
            raise ValueError("Surname can't be a number")
        self.__surname = value.capitalize()



    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("Id of a Client should be only a number")
        if value < 0:
            raise ValueError("Id can't be negative")
        self.__id = value
        


    
    @property
    def referred_by(self):
        return self.__referred_by

    @referred_by.setter
    def referred_by(self, value):
        if not isinstance(value, str) and value is not None:
            raise TypeError("Referred by of a Client should be only a string or None")
        if not value.isalpha():
            raise ValueError("Referred by can't be a number")
        self.__referred_by = value.capitalize()


    

    @property
    def commission(self):
        return self.__commission
    
    @commission.setter
    def commission(self, value):
        if not isinstance(value, float):
            raise TypeError("Commission of a Client should be only a float")
        if value < 0:
            raise ValueError("Commission can't be negative")
        self.__commission = value
 """



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




