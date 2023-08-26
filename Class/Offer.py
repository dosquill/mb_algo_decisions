class Offer:
    def __init__(self, bookmaker, earning, budget_needed, roi, time_needed):
        self.bookmaker = bookmaker
        self.earning = earning
        self.budget_needed = budget_needed
        self.roi = roi
        self.time_needed = time_needed
        self.completed = False

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