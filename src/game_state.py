class GameState:
    def __init__(self, customers):
        self._state = "MAIN_MENU"
        self._customer_index = 0
        self._reputation = 0
        self._profit_credits = 0
        self._overall_rep = 0
        self._customers = customers

    def get_current_customer(self):
        return self._customers[self._customer_index]

    def get_state(self):
        return self._state

    def get_reputation(self):
        return self._reputation

    def get_profit_credits(self):
        return self._profit_credits

    def get_overall_rep(self):
        return self._overall_rep

    def get_customer_index(self):
        return self._customer_index

    def get_customers_len(self):
        return len(self._customers)

    def set_state(self, state):
        self._state = state

    def set_reputation(self,rep):
        self._reputation = rep

    def next_customer(self):
        self._customer_index = (self._customer_index + 1) % len(self._customers)

    def add_reputation(self, rep):
        self._reputation += rep

    def add_profit(self, prof):
        self._profit_credits += prof

    def add_overall_rep(self, rep):
        self._overall_rep += rep
