import curses

def main(window: curses.window):
    window.keypad(True) # Turn on keypad mode
    curses.noecho() # Turn off key echoing
    curses.curs_set(0) # Set cursor visibility
    curses.cbreak() # Turn off buffered input

    #stock example
    stock_list = ["--------------------------",
                  "|      Stock  1          |",
                  "|      Stock  2          |",
                  "|      Stock  3          |",
                  "|      stock  4          |",
                  "|      stock  5          |",
                  "--------------------------"]

    for index, string in enumerate(stock_list):
        window.addstr(index, 0, string)

    #Buy/sell option
    BuySell_list = ["--------------------------",
                  "|     Stock 1  +  -      |",
                  "|     Stock 2  +  -      |",
                  "|     Stock 3  +  -      |",
                  "|     Stock 4  +  -      |",
                  "|     Stock 5  +  -      |",
                  "--------------------------"]
    for index, string in enumerate(BuySell_list):
        window.addstr(index, 26, string)
    #your stock count
    StockCount_list = ["--------------------------",
                       "|     You have :         |",
                       "|     You have :         |",
                       "|     You have :         |",
                       "|     You have :         |",
                       "|     You have :         |",
                       "--------------------------"]
    for index, string in enumerate(StockCount_list):
            window.addstr(index, 52, string)

    #News
    window.addstr(7, 0, "------------------------------------------------------------------------------")
    window.addstr(8, 0, "|      This weeks news                                                       |")
    window.addstr(9, 0, "|                                                                            |")
    window.addstr(10, 0,"|                                                                            |")
    window.addstr(11, 0,"|                                                                            |")
    window.addstr(12, 0,"------------------------------------------------------------------------------")
    while 1: # Loop so the game doesn't exit instantly
        window.refresh() # Refresh

if __name__ == '__main__':
    curses.wrapper(main) # Initialise and return the window to main()

