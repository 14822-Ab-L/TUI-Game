import curses
import terminal_ui
from stocks import Market, StockLogic

def main(window: curses.window):
    """Run the TamaTUI application."""

    window.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    curses.cbreak()

    market = Market()
    logic = StockLogic(market)

    terminal_ui.run_dashboard(window, market, logic)


if __name__ == "__main__":
    curses.wrapper(main)