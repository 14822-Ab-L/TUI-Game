import curses
import terminal_ui
import titlescreen
import playerstats
from dayscreens import dayscreen
from stocks import Market, StockLogic
from playerstats import Player

def main(window: curses.window):
    """Run the TamaTUI application."""

    window.keypad(True) # Turn on keypad mode
    curses.noecho() # Turn off key echoing
    curses.curs_set(0) # Set cursor visibility
    curses.cbreak() # Turn off buffered input

    name = titlescreen.title_screen(window) #name catches the input given in the title screen
    window.clear() #You need clear after a window is finshed, not after player. lost 1 hour learning this the hard way.
    player = playerstats.Player(name, "1/10/2026", 1000,-10000,10000,9) # starting starts after retrieving name input.
    #(name, date, balance, net_worth, debt, turns)

    market = Market()


    logic = StockLogic(market, player)

    terminal_ui.run_dashboard(window, market, logic)
    dayscreen(window, 1, "The Beginning")  # Display the day screen for Day 1


if __name__ == "__main__":
    curses.wrapper(main)
