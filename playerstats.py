import curses

class Player:
    def __init__ (self, name, date, balance, net_worth, debt, turns ):
        self.name = name
        self.date = date
        self.balance = balance
        self.networth = net_worth
        self.debt = debt
        self.turns = turns

    def display_stats(self, window): #take the returned name input from main and prints the stats to the screen.
        window.addstr(1, 1, f"Name: {self.name}")
        window.addstr(1, 20, f"Date: {self.date}")#everything else from here is a WIP
        window.addstr(1, 40, f"Balance: ${self.balance}")
        window.addstr(1, 60, f"Net Worth: ${self.networth}")
        window.addstr(1, 80, f"Debt {self.debt}")
        window.addstr(1, 100, f" Turns Left: {self.turns}")

#calculates total networth and returns it to the player
#def getnetworth(self,balance,net_worth, debt):
    #net_worth = net_worth + balance - debt
    #return self.net_worth
