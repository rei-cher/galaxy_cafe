"""
Game State modulo

Keeps track of game states values
"""
class GameState:
    """
    Game state clsas

    Requires:
        custoemrs: list[Customer]
    """
    def __init__(self, customers: list[Customer]):
        """
        Object initializator

        Pre populates default satates and 
        customers with list of Customer objects
        """
        self._state = "MAIN_MENU"
        self._customer_index = 0
        self._reputation = 0
        self._profit_credits = 0
        self._overall_rep = 0
        self._customers = customers

    def get_current_customer(self) -> Customer:
        """
        Returns Customer object of the current customer
        """
        return self._customers[self._customer_index]

    def get_state(self):
        """
        Returns game state
        """
        return self._state

    def get_reputation(self):
        """
        Returns local reputation
        Covers only the result of serving the dish to the customer
        """
        return self._reputation

    def get_profit_credits(self):
        """
        Returns profit earned
        """
        return self._profit_credits

    def get_overall_rep(self):
        """
        Returns global reputation
        
        Conbined reputation of all servings
        """
        return self._overall_rep

    def get_customer_index(self):
        """
        Returns the index of the customer

        For tracking purposes
        """
        return self._customer_index

    def get_customers_len(self):
        """
        Return the number of customers in the list
        """
        return len(self._customers)

    def set_state(self, state):
        """
        Setting the state of the game for the menu screen tracking
        """
        self._state = state

    def set_reputation(self,rep):
        """
        Setting the local reputation

        Only for the current serving
        """
        self._reputation = rep

    def next_customer(self):
        """
        Goes to the next customer by incrementing index by one

        Overflow mitigation: index os moduled by the len of the customers list
        Never exceeds the lenght
        """
        self._customer_index = (self._customer_index + 1) % len(self._customers)

    def add_reputation(self, rep: int):
        """
        Modifies the reputation for specific serving based on the argument
        """
        self._reputation += rep

    def add_profit(self, prof: int):
        """
        Modifies profit credits tracker by adding the argument
        """
        self._profit_credits += prof

    def add_overall_rep(self, rep: int):
        """
        Modifies overall reputation by adding the argument
        """
        self._overall_rep += rep
