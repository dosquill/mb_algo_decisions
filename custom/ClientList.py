from custom.Client import *

# define a class of list of clients
class ClientList:
    def __init__(self):
        self.list = []

    # FIXME
    # OVERLOADING 
    def __str__(self) -> str:   
        result = ""
        for client in self.list:
            result += str(client) + "\n"  
        return result


    # SORTING
    def sort_by_name(self):
        self.list.sort(key=lambda x: x.get_name())
    
    def sort_by_id(self):
        self.list.sort(key=lambda x: x.id)
    

    # GETTERS
    def get_list(self):
        return self.list

    def get_client_by_id(self, client_id):
        for client in self.clients:
            if client.id == client_id:
                return client
        return None

    def get_client_by_name(self, name):
        for client in self.list:
            if (client.get_name() == name):
                return client
        return None



    # SETTERS
    def set_list(self, list):
        self.list = list
    

    # ADDING 
    def add_item(self, client: Client):
        if (client not in self.list and client is not None):
            self.list.append(client)

    # REMOVING
    def remove_item(self, client: Client):
        if (client in self.list):
            self.list.remove(client)
    
    def remove_item_by_id(self, client_id):
        for client in self.list:
            if (client.id == client_id):
                self.list.remove(client)
                return True
        return False
    
    def remove_item_by_name(self, name):
        for client in self.list:
            if (client.get_name() == name):
                self.list.remove(client)
                return True
        return False
    
