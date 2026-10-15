import curses

class Player:
    def __init__ (self, stdscr, balance):
        self.name = stdscr
        self.balance = balance

#Subclass
class Money(Player): # Currently used for adjusting balance, net worth and debt.
    def __init__ (self, balance,net_worth,debt):
        self.balance_a = balance
        self.net_worth = net_worth
        self.debt = debt

#calculates total networth and returns it to the player
def getnetworth(self,balance,net_worth, debt):
    net_worth = net_worth + balance - debt
    return self.net_worth

#method for tracking player name:
def getname(self, stdscr):
    stdscr.addstr(2, 2, "Enter your First name: ")
    stdscr.refresh()

    curses.echo #toggles user display

    name_bytes = stdscr.getstr(2, 26, 20)
    user_name = name_bytes.decode('utf-8')

    curses.noecho() #Turns off user display


