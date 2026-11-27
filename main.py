import curses
import terminal_ui
from stocks import Market, StockLogic
from playerstats import Player

def main(window: curses.window):
    """Run the TamaTUI application."""

    window.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    curses.cbreak()

    market = Market()

    player = Player(
    "Player 1",
    "Day 1",
    1000.0,
    1000.0,
    0.0,
    10
    )

    logic = StockLogic(market, player)
    
    terminal_ui.run_dashboard(window, market, logic)


if __name__ == "__main__":
    curses.wrapper(main)
