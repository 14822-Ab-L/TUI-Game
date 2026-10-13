import curses
import stocks

def main(window: curses.window):
    window.keypad(True) # Turn on keypad mode
    curses.noecho() # Turn off key echoing
    curses.curs_set(0) # Set cursor visibility
    curses.cbreak() # Turn off buffered input


    while 1: # Loop so the game doesn't exit instantly
        window.refresh() # Refresh
        curses.newwin(0, 50)
        window.box()
        #treat below here as placeholder UI
        stocks.stats(stocks.stats_list, window, start_row=1, start_col=1)
        stocks.stocks(stocks.stock_list, window, start_row=5, start_col=2)
        stocks.stockbuy(stocks.stock_buy, window, start_row=5, start_col=20)
        stocks.stockown(stocks.stock_own, window, start_row=5, start_col=40)
        stocks.stockavg(stocks.stock_avg, window, start_row=5, start_col=60)
        stocks.stockcurrent(stocks.stock_current, window, start_row=5, start_col=80)
        stocks.stocklast(stocks.stock_last, window, start_row=5, start_col=100)
        stocks.draw_headings(stocks.headings, window, row=3)

if __name__ == '__main__':
    curses.wrapper(main) # Initialise and return the window to main()

