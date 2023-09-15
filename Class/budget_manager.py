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

# TODO inutilized budget percentage

class BudgetManager:
    def __init__(self, initial_budget, client_list: list):
        #
        self.client_list = client_list
        self.initial_budget = initial_budget
        self.allocated = 0
        self.num_clients = len(client_list)  
        self.profit = 0

        # 
        self.budget_tracking = {}
        self.profit_tracker = {}
        self.commission_tracker = {}
        for client in client_list:
            self.budget_tracking[client.name] = 0
            self.profit_tracker[client.name] = 0
            self.commission_tracker[client.name] = 0


        self.avg_roi_per_client = {client.name: client.calculate_average_roi() for client in self.client_list}
        self.total_roi = {round(sum(self.avg_roi_per_client.values()), 2)}
        #self.weights = {name: round((roi / self.total_roi), 2) for name, roi in self.avg_roi_per_client.items()}

        # initial allocation
        # self.allocate()



    # OVERRIDE
    def __str__(self) -> str:
        client_name = [client.name for client in self.client_list]
        return (
            f"BudgetManager:\n"
            f"  Initial Budget: {self.initial_budget}€\n"
            f"  Number of Clients: {self.num_clients}\n"
            f"  Client List: {client_name}\n"
            f"  Allocated Budget: {self.allocated}€\n"
            f"  Profit: {self.profit}€\n"
            f"  Budget Tracking: {pformat(self.budget_tracking)}\n"
            #f"  Weights: {pformat(self.weights)}\n"
            f"  Total ROI: {self.total_roi}%\n"
            f"  Average ROI per Client: {pformat(self.avg_roi_per_client)}\n"
            f"  Profit Tracker: {pformat(self.profit_tracker)}\n"
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
            return 


        # If are multiple clients
        # Calculate the average ROI for each client
        self.avg_roi_per_client = {client.name: client.calculate_average_roi() for client in self.client_list}
        
        # Calculate the total ROI
        self.total_roi = round(sum(self.avg_roi_per_client.values()), 2)

        # Calculate the weight for each client
        self.weights = {name: round((roi / self.total_roi), 2) for name, roi in self.avg_roi_per_client.items()}

        # Allocate the initial_budget based on the calculated weight
        self.budget_tracking = {name: round(self.initial * weight, 2) for name, weight in self.weights.items()}
        

        # Se il cliente è stato consigliato, traccia la commissione
        for client in self.client_list:
            if client.referred_by:
                self.commission_tracker[client.name] = self.profit_tracker[client.name] * 0.5 

        









    # TODO il punto è questo, se non si riesce a risolvere un offerta il budget si deve sbilanciare
    # METHOD FOR RESOLVING
    def resolving(self, client: Client, offer: Offer) -> bool:
        if (self.allocated + offer.budget_needed) > self.initial_budget:
            return False
        
        # TODO questo non funziona per adesso perché il budget non tiene conto che c'è n'è altro, se si può fare un offerta non si prende i soldi da un altro cliente ma si termina e basta
        #if (self.budget_tracking[client.name] - offer.budget_needed) < 0:
        #    return None
        
        # aggiungiamo una traccia del profitto del cliente e della sua commissione
        self.budget_tracking[client.name] += offer.budget_needed
        self.profit_tracker[client.name] += offer.profit
        self.allocated += offer.budget_needed
        self.profit += offer.profit
        return True
    



    # TODO da fare un releaser migliore
    def release(self, amount):
        self.initial_budget = amount
        return self.initial_budget
    



    def remaining_budget(self):
        return self.initial_budget - self.allocated        
    










# TODO quando arriva qua dentro, il initial_budget è già stato allocato
def allocate_multiple_new(clients: list, occurence: dict, initial_budget: float) -> dict:
    budget_tracking = {}
    completed_allocation = []
    remaining_budget = initial_budget  # Initialize remaining_budget to initial_budget
    
    # azzerare il initial_budget di tutti i clienti
    for client in clients:
        client.initial_budget = 0

    for offer_name, offer_count in occurence.items():
        # Initialize a counter for each offer
        offer_counter = 0
        
        for client in clients:
            for offer in client.remaining_offers:
                if offer.name == offer_name and offer.budget_needed <= remaining_budget:
                    client.initial_budget += offer.budget_needed
                    
                    budget_tracking[client.name] = client.initial_budget
                    
                    remaining_budget -= offer.budget_needed
                    
                    offer_counter += 1
                    
                    if offer_counter == offer_count:
                        completed_allocation.append(offer_name)
                        break
            
            # Break the outer loop if the offer counter matches the offer_count
            if offer_counter == offer_count:
                completed_allocation.append(offer_name)
                break
                
    print(budget_tracking)

    for names in completed_allocation:
        if names in occurence:
            del occurence[names]

    # se la somma dei initial_budget di ognuno supera quella iniziale allora porco dio che cazzo succede
    if sum(budget_tracking.values()) > initial_budget:
        raise Exception("Porco dio che cazzo succede")

    return {
        'budget_tracking': budget_tracking,
        'remaining_budget': remaining_budget
    }

    


    




        
