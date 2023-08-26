import json
from Class.Offer import *

class OfferList:
    # default file_path for multiple constructor
    def __init__(self, file_path= None):
        self.list = []
        self.file_path = file_path

        if (file_path != None):
            self.load_from_file(file_path)

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

    # sort by roi function
    def sort_by_roi(self):
        self.list.sort(key=lambda x: x.roi, reverse=True)
    
        
    def add_item(self, item):
        if (isinstance(item, Offer) == False):
            raise TypeError("item must be an Offer")
        self.list.append(item)    

    def remove_item(self, item):
        if (isinstance(item, Offer) == False):
            raise TypeError("item must be an Offer")
        self.list.remove(item)

    def remove_by_bookmaker(self, bookmaker_name):
        for offer in self.list:
            if offer.bookmaker == bookmaker_name:
                self.list.remove(offer)
                return  # Exit after removing the first occurrence
    
    def __str__(self):
        result = ""
        for offer in self.list:
            result += str(offer) + "\n"
        return result

    def __iter__(self):
        return iter(self.list)
    
    def __len__(self):
        return len(self.list)
    
    def __getitem__(self, index):
        return self.list[index]
    
    def copy(self):
        if (self.file_path != None):
            copied_list = OfferList(self.file_path)
        else:
            copied_list = OfferList()
        
        return copied_list


    def save_to_csv(self, csv_filename):
        for offer in self.list:
            offer.save_to_csv(csv_filename)
    


    