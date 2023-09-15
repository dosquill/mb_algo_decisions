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


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Offer):
            return False
        return (self.name == other.name and
                self.profit == other.profit and
                self.budget_needed == other.budget_needed and
                self.time_needed == other.time_needed)



    # GETTERS AND SETTERS
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Bookmaker must be a string.")
        if value == '':
            raise Exception("Bookmaker cannot be empty.")
        if value == None:
            raise Exception("Bookmaker cannot be None.")
        self.__name = value.capitalize()





    @property
    def profit(self):
        return self.__profit

    @profit.setter
    def profit(self, value):
        value_name = "Profit"
        if not isinstance(value, (int, float)):
            raise Exception(f"{value_name} must be a float.")
        if isinstance(value, bool):
            raise Exception(f"{value_name} cannot be a boolean.")
        if value == "":
            raise Exception(f"{value_name} cannot be empty.")
        if value == None:
            raise Exception(f"{value_name} cannot be None.")
        if value < 0:
            raise Exception(f"{value_name} cannot be negative.")
        self.__profit = value





    @property
    def budget_needed(self):
        return self.__budget_needed

    @budget_needed.setter
    def budget_needed(self, value):
        value_name = "Budget needed"
        if not isinstance(value, (int, float)):
            raise Exception(f"{value_name} must be a float.")
        if isinstance(value, bool):
            raise Exception(f"{value_name} cannot be a boolean.")
        if value == "":
            raise Exception(f"{value_name} cannot be empty.")
        if value == None:
            raise Exception(f"{value_name} cannot be None.")
        if value < 0:
            raise Exception(f"{value_name} cannot be negative.")
        self.__budget_needed = value




    
    @property
    def time_needed(self):
        return self.__time_needed
    
    @time_needed.setter
    def time_needed(self, value):
        value_name = "Time needed"
        if not isinstance(value, int):
            raise Exception(f"{value_name} must be a float.")
        if isinstance(value, bool):
            raise Exception(f"{value_name} cannot be a boolean.")
        if value == "":
            raise Exception(f"{value_name} cannot be empty.")
        if value == None:
            raise Exception(f"{value_name} cannot be None.")
        if value < 0:
            raise Exception(f"{value_name} cannot be negative.")
        self.__time_needed = value
    

    
