class Player:
    def __init__ (self, name, date, balance, networth, debt, turns ):
        self.name = name
        self.date = date
        self.balance = balance
        self.networth = networth
        self.debt = debt
        self.turns = turns

    def get_balance(self): # Returns the player's current balance
        return self.balance

    def get_net_worth(self): # calcuate net worth based on balance and debt
        networth = self.net_worth - self.debt + self.balance
        return networth

    def get_debt(self): # Returns the player's current debt
        return self.debt

    def display_stats(self, window): #take the returned name input from main and prints the stats to the screen.
        window.addstr(1, 1, f"Name: {self.name}")
        window.addstr(1, 20, f"Date: {self.date}")#everything else from here is a WIP
        window.addstr(1, 40, f"Balance: ${self.balance}")
        window.addstr(1, 60, f"Net Worth: ${self.networth}")
        window.addstr(1, 80, f"Debt {self.debt}")
        window.addstr(1, 100, f" Turns Left: {self.turns}")
