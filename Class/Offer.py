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

    #def mark_completed(self):
    #    self.completed = True

    # toString
    def __str__(self):
        #return f"Bookmaker: {self.bookmaker} Earnings: {self.earning} Budget needed: {self.budget_needed} ROI: {self.roi} Time needed: {self.time_needed} Completed: {self.completed}"
        return f"Bookmaker: {self.bookmaker} Earnings: {self.earning} Budget needed: {self.budget_needed} ROI: {self.roi} Time needed: {self.time_needed}"

    def copy(self):
        return Offer(
            self.bookmaker,
            self.earning,
            self.budget_needed,
            self.roi,
            self.time_needed
        )
    
    def get_budget_needed(self):
        return self.budget_needed
    
    def get_earning(self):
        return self.earning 
    
    def get_name(self):
        return self.bookmaker
    
    def save_to_csv(self, csv_filename):
        with open(csv_filename, 'a', newline='') as csvfile:
            fieldnames = self.__dict__.keys()  # Get the keys of the object's properties
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if csvfile.tell() == 0:  # Write header only if the file is empty
                writer.writeheader()

            writer.writerow(self.__dict__)

    def get_step_num(self):
        return self.step_num
    
    def set_step_num(self, step_num):
        self.step_num = step_num
    