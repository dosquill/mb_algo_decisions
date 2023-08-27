import csv


class Offer:
    def __init__(self, bookmaker, earning, budget_needed, roi, time_needed):
        self.bookmaker = bookmaker
        self.earning = earning
        self.budget_needed = budget_needed
        self.roi = roi
        self.time_needed = time_needed
        self.completed = False
        self.step_num = None

    csv_fieldnames = ['bookmaker', 'earning', 'budget_needed', 'roi', 'time_needed', 'completed', 'step_num']


    # OVERLOADING METHODS
    # toString
    def __str__(self):
        #return f"Bookmaker: {self.bookmaker} Earnings: {self.earning} Budget needed: {self.budget_needed} ROI: {self.roi} Time needed: {self.time_needed} Completed: {self.completed}"
        return f"Bookmaker: {self.bookmaker} Earnings: {self.earning} Budget needed: {self.budget_needed} ROI: {self.roi} Time needed: {self.time_needed}"

    
    # GETTERS
    def get_budget_needed(self):
        return self.budget_needed
    
    def get_earning(self):
        return self.earning 
    
    def get_name(self):
        return self.bookmaker
    
    def get_roi(self):
        return self.roi
    
    def get_time_needed(self):
        return self.time_needed
    
    def get_completed(self):
        return self.completed
    
    def get_step_num(self):
        return self.step_num
    
    def get_step_num(self):
        return self.step_num
    
    def set_step_num(self, step_num):
        self.step_num = step_num
    

    # SETTERS
    def set_budget_needed(self, budget_needed):
        self.budget_needed = budget_needed

    def set_earning(self, earning):
        self.earning = earning

    def set_name(self, bookmaker):
        self.bookmaker = bookmaker
    
    def set_roi(self, roi):
        self.roi = roi

    def set_time_needed(self, time_needed):
        self.time_needed = time_needed
    
    def set_completed(self, completed):
        self.completed = completed


    # OTHER METHODS
    def copy(self):
        return Offer(
            self.bookmaker,
            self.earning,
            self.budget_needed,
            self.roi,
            self.time_needed
        )
    
    def save_to_csv(self, csv_filename):
        with open(csv_filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=Offer.csv_fieldnames)
            
            if csvfile.tell() == 0:  # Write header only if the file is empty
                writer.writeheader()

            # Create a dictionary with the object's properties
            offer_dict = {
                'bookmaker': self.bookmaker,
                'earning': self.earning,
                'budget_needed': self.budget_needed,
                'roi': self.roi,
                'time_needed': self.time_needed,
                'completed': self.completed,
                'step_num': self.step_num
            }

            writer.writerow(offer_dict)