import csv

class Offer:
    """Class representing an offer with its attributes and methods."""

    def __init__(self, name: str, profit: float, budget_needed: float, time_needed: int):
        self.name = name
        self.profit = profit
        self.budget_needed = budget_needed
        self.time_needed = time_needed
        self.roi = (profit / budget_needed) * 100 


    # OVERLOADING METHODS
    # toString
    def __str__(self):
        return f"Name: {self.name}\nProfit: {self.profit}€\nBudget needed:{self.budget_needed}€\nROI: {self.roi}%\nTime needed: {self.time_needed}(days)"

    """ 
    # GETTERS AND SETTERS
    @property
    def bookmaker(self):
        return self.__bookmaker

    @bookmaker.setter
    def bookmaker(self, bookmaker):
        if not isinstance(bookmaker, str):
            raise TypeError("Bookmaker must be a string.")
        if bookmaker == "":
            raise ValueError("Bookmaker cannot be empty.")
        if bookmaker == None:
            raise ValueError("Bookmaker cannot be None.")
        if not bookmaker.isalnum():
            raise ValueError("Bookmaker must be a string.")
        self.__bookmaker = bookmaker



    @property
    def earning(self):
        return self.__earning

    @earning.setter
    def earning(self, earning):
        if not isinstance(earning, (int, float)):
            raise TypeError("Earning must be a float.")
        if isinstance(earning, bool):
            raise TypeError("Earning must be a float.")
        if earning == "":
            raise ValueError("Earning cannot be empty.")
        if earning == None:
            raise ValueError("Earning cannot be None.")
        if earning < 0:
            raise ValueError("Earning cannot be negative.")
        self.__earning = earning



    @property
    def budget_needed(self):
        return self.__budget_needed

    @budget_needed.setter
    def budget_needed(self, budget_needed):
        if not isinstance(budget_needed, (int, float)):
            raise TypeError("Budget needed must be a float.")
        if budget_needed == "":
            raise ValueError("Budget needed cannot be empty.")
        if budget_needed == None:
            raise ValueError("Budget needed cannot be None.")
        if budget_needed < 0:
            raise ValueError("Budget needed cannot be negative.")
        self.__budget_needed = budget_needed



    @property
    def roi(self):
        return self.__roi
    
    @roi.setter
    def roi(self, roi):
        if not isinstance(roi, (int, float)):
            raise TypeError("ROI must be a float.")
        if roi == "":
            raise ValueError("ROI cannot be empty.")
        if roi == None:
            raise ValueError("ROI cannot be None.")
        if roi < 0:
            raise ValueError("ROI cannot be negative.")
        self.__roi = roi

    

    @property
    def time_needed(self):
        return self.__time_needed
    
    @time_needed.setter
    def time_needed(self, time_needed):
        if not isinstance(time_needed, int):
            raise TypeError("Time needed must be an integer.")
        if time_needed == "":
            raise ValueError("Time needed cannot be empty.")
        if time_needed == None:
            raise ValueError("Time needed cannot be None.")
        if time_needed < 0:
            raise ValueError("Time needed cannot be negative.")
        self.__time_needed = time_needed
    


    @property
    def completed(self):
        return self.__completed

    @completed.setter
    def completed(self, completed):
        if not isinstance(completed, bool):
            raise TypeError("Completed must be a boolean.")
        if completed == "":
            raise ValueError("Completed cannot be empty.")
        if completed == None:
            raise ValueError("Completed cannot be None.")
        self.__completed = completed
    


    @property
    def step_num(self):
        return self.__step_num
    
    @step_num.setter
    def step_num(self, step_num):
        if not isinstance(step_num, int):
            raise TypeError("Step number must be an integer.")
        if step_num == "":
            raise ValueError("Step number cannot be empty.")
        if step_num == None:
            raise ValueError("Step number cannot be None.")
        if step_num < 0:
            raise ValueError("Step number cannot be negative.")
        self.__step_num = step_num

    """


    
