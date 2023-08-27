import json
from custom.Offer import *

class OfferList:
    # default file_path for multiple constructor
    def __init__(self, file_path= None):
        self.list = []
        self.file_path = file_path

        if (file_path != None):
            self.load_from_file(file_path)


    # OVERLOADING METHODS
    def __str__(self):
        result = ""
        for offer in self.list:
            result += str(offer) + "\n"
        return result

    def __iter__(self):
        return iter(self.list)
    
    def __len__(self):
        return len(self.list)
    

    # GETTERS
    def get_list(self):
        return self.list
    
    def get_file_path(self):
        return self.file_path


    # SETTERS



    # ADDING 
    def add_item(self, item):
        if (isinstance(item, Offer) == False):
            raise TypeError("item must be an Offer")
        self.list.append(item)    



    # REMOVING 
    def remove_by_bookmaker(self, bookmaker_name):
        for offer in self.list:
            if offer.bookmaker == bookmaker_name:
                self.list.remove(offer)
                return  # Exit after removing the first occurrence
    
    def remove_item(self, item):
        if (isinstance(item, Offer) == False):
            raise TypeError("item must be an Offer")
        self.list.remove(item)



    # SORTING 
    def sort_by_roi(self):
        self.list.sort(key=lambda x: x.roi, reverse=True)
    
    def sort_by_earning(self):
        self.list.sort(key=lambda x: x.earning, reverse=True)
    
    def sort_by_budget_needed(self):
        self.list.sort(key=lambda x: x.budget_needed, reverse=True)
    
    def sort_by_time_needed(self):
        self.list.sort(key=lambda x: x.time_needed, reverse=True)
    
    def sort_by_bookmaker(self):
        self.list.sort(key=lambda x: x.bookmaker, reverse=True)
    
    def sort_by_step_num(self):
        self.list.sort(key=lambda x: x.step_num, reverse=True)
    
    def sort_by_completed(self):
        self.list.sort(key=lambda x: x.completed, reverse=True)
    
    def sort_by_name(self):
        self.list.sort(key=lambda x: x.name, reverse=True)
    
    def sort_by_id(self):
        self.list.sort(key=lambda x: x.id, reverse=True)
    
    
    # OTHER 
    def load_from_file(self, file_path):
        self.file_path = file_path
        with open(file_path, 'r') as json_file:
            offer_data = json.load(json_file)
            i = 0
            
            for offer in offer_data:
                offer = Offer(offer_data[i]['bookmaker'], offer_data[i]['earning'], offer_data[i]['budget_needed'], offer_data[i]['roi'], offer_data[i]['time_needed'])
                self.list.append(offer)
                i+=1

        self.sort_by_roi()
    
    
    def copy(self):
        if (self.file_path != None):
            copied_list = OfferList(self.file_path)
        else:
            copied_list = OfferList()
        
        return copied_list


    def save_to_csv(self, csv_filename):
        for offer in self.list:
            offer.save_to_csv(csv_filename)
    


    