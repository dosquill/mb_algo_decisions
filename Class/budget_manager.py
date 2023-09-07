from pprint import pformat
from .client import Client
from .offer import Offer

# perché della scelta di un initial_budget manager
# 1. Unica fonte di verità: il initial_budget manager è una classe che gestisce l'allocazione in una sessione
# 2. Più pulita 
# 3. Scalabile
# 4. Più facile da testare
# 5. Più facile da mantenere
# 6. Migliore nel lungo periodo
# Budget manager si deve solo preoccupare di aggiornare, allocare e deallocare il initial_budget

class BudgetManager:
    def __init__(self, initial, client_list: list):
        #
        self.client_list = client_list
        self.initial = initial
        self.allocated = 0
        self.num_clients = 0
        self.profit = 0

        # 
        self.tracking = {}
        self.weights = {}
        self.total_roi = {}
        self.avg_roi_per_client = {}

        # initial allocation
        self.allocate()



    # OVERRIDE
    def __str__(self) -> str:
        client_name = [client.name for client in self.client_list]
        return (
            f"BudgetManager:\n"
            f"  Initial Budget: {self.initial}€\n"
            f"  Number of Clients: {self.num_clients}\n"
            f"  Client List: {client_name}\n"
            f"  Allocated Budget: {self.allocated}€\n"
            f"  Profit: {self.profit}€\n"
            f"  Budget Tracking: {pformat(self.tracking)}\n"
            f"  Weights: {pformat(self.weights)}\n"
            f"  Total ROI: {self.total_roi}%\n"
            f"  Average ROI per Client: {pformat(self.avg_roi_per_client)}"
        )



    # questo è il metodo iniziale che si occupa di allocare budget. Verrà chiamato più volte in futuro
    def allocate(self) -> dict:
        if not isinstance(self.client_list, list):
            raise TypeError("Client list must be a list")

        self.num_clients = len(self.client_list)
        
        if (self.num_clients == 0):
            raise ValueError("No clients in the list")
    
        if (self.num_clients == 1):
            self.num_clients = 1
            client = self.client_list[0]
            self.avg_roi_per_client = {client.name: client.calculate_average_roi()}
            self.weights = {client.name: 1}
            self.total_roi = self.avg_roi_per_client[client.name]
            self.tracking[client.name] = self.initial
            return 


        # If are multiple clients
        # Calculate the average ROI for each client
        self.avg_roi_per_client = {client.name: client.calculate_average_roi() for client in self.client_list}
        
        # Calculate the total ROI
        self.total_roi = round(sum(self.avg_roi_per_client.values()), 2)

        # Calculate the weight for each client
        self.weights = {name: round((roi / self.total_roi), 2) for name, roi in self.avg_roi_per_client.items()}

        # Allocate the initial_budget based on the calculated weight
        self.tracking = {name: round(self.initial * weight, 2) for name, weight in self.weights.items()}
        
        return 






    # METHOD FOR RESOLVING
    def resolving(self, client: Client, offer: Offer) -> bool:
        if (self.allocated + offer.budget_needed) > self.initial:
            return None
        if (self.tracking[client.name] - offer.budget_needed) < 0:
            return None

        self.tracking[client.name] -= offer.budget_needed
        self.allocated += offer.budget_needed
        self.profit += offer.profit
        return True
    


    def release(self, amount):
        self.allocated -= amount
        if self.allocated < 0:
            raise ValueError("Allocated initial_budget cannot be negative")



    def remaining_budget(self):
        return self.initial - self.allocated        
    







    


    




        
