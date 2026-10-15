import curses

stock_list = [
    "Bombs R US",
    "Medicine INC",
    "Fast Cars 4 U",
    "AI Overlords",
    "Crypto Bros"
]

stats_list = [
    "Name: Albert S",
    "Date: 13/10/2026",
    "Current balance: 1000$",
    "Net Worth: -33000$",
    "Debt: 34000",
    "Turns left: 9"
]
headings = [
    ("Stocks", 2),
    ("Buy/Sell", 20),
    ("Owned", 40),
    ("Average buy price", 60),
    ("Current price", 80),
    ("Change last turn", 100)
]
stock_buy = [
    "+ || -",
    "+ || -",
    "+ || -",
    "+ || -",
    "+ || -"
]
stock_own = [
    ": 0",
    ": 11",
    ": 123",
    ": 7",
    ": 212"
]
stock_avg = [
    ": 93$",
    ": 122$",
    ": 10$",
    ": 72:",
    ": 31$"
]
stock_current = [
    ": 100$",
    ": 100$",
    ": 100$",
    ": 100$",
    ": 100$"
]
stock_last = [
    ": 11%",
    ": -11%",
    ": -12%",
    ": 122%",
    ": 1000%"
]
news_menu = [
    ("Todays news:", 2),
    ("Place holder:", 40),
    ("Logo here?", 100)
]
stories = [
    ("blah blah blah"),
    ("test test test")
]

settings_list = [
    "Settings",
    "Save Game",
    "Load Game",
    "Exit Game"
]

end_game_button = [
    "END DAY HERE BUTTON"
]

meme_logo_list = [
    "ASCII LOGO HERE"
]

#basic stocks list function, cycles through the list and prints it to the window.
def stocks(stock_list, window, start_row, start_col):
    for index, string in enumerate(stock_list):
        window.addstr(start_row + index, start_col, string)
# start_row = Y axis, start_col = X axis.

#Everything below here is placeholder for UI purposes.

#Stealing from above to print out stats for UI purposes.
def stats(stats_list, window, start_row, start_col):
    stats_line = " | ".join(stats_list)
    window.addstr(start_row, start_col, stats_line)

def draw_headings(headings, window, row):
    for label, column in headings:
        window.addstr(row, column, label)

def stockbuy(stock_buy, window, start_row, start_col):
    for index, string in enumerate(stock_buy):
        window.addstr(start_row + index, start_col, string)

def stockown(stock_own, window, start_row, start_col):
    for index, string in enumerate(stock_own):
        window.addstr(start_row + index, start_col, string)

def stockavg(stock_avg, window, start_row, start_col):
    for index, string in enumerate(stock_avg):
        window.addstr(start_row + index, start_col, string)

def stockcurrent(stock_current, window, start_row, start_col):
    for index, string in enumerate(stock_current):
        window.addstr(start_row + index, start_col, string)

def stocklast(stock_last, window, start_row, start_col):
    for index, string in enumerate(stock_last):
        window.addstr(start_row + index, start_col, string)

def newsmenu(news_menu , window, start_row, start_col):
    for index, string in enumerate(news_menu):
        window.addstr(start_row + index, start_col, string)

def newsstories(stories , window, start_row, start_col):
    for index, string in enumerate(stories):
        window.addstr(start_row + index, start_col, string)

def settings(settings_list , window, start_row, start_col):
    for index, string in enumerate(settings_list):
        window.addstr(start_row + index, start_col, string)

def endgamebutton(end_game_button , window, start_row, start_col):
    for index, string in enumerate(end_game_button):
        window.addstr(start_row + index, start_col, string)

def draw_dashboard(window):
    window.box()

    stats(stats_list, window, start_row=1, start_col=1)
    stocks(stock_list, window, start_row=5, start_col=2)
    stockbuy(stock_buy, window, start_row=5, start_col=20)
    stockown(stock_own, window, start_row=5, start_col=40)
    stockavg(stock_avg, window, start_row=5, start_col=60)
    stockcurrent(stock_current, window, start_row=5, start_col=80)
    stocklast(stock_last, window, start_row=5, start_col=100)

    draw_headings(headings, window, row=3)
    draw_headings(news_menu, window, row=13)

    settings(settings_list, window, start_row=21, start_col=2)
    endgamebutton(end_game_button, window, start_row=22, start_col=25)
    stocks(meme_logo_list, window, start_row=21, start_col=85)

    newsstories(stories, window, start_row=15, start_col=2)