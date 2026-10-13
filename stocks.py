import curses

stock_list = [
    "Bombs R US",
    "Medicine INC",
    "Fast Cars 4 U",
    "AI Overlords",
    "Crypto Bros"
]

stats_list = [
    "Name:Albert S "
    "Date: 13/10/2026 "
    "Current balance: 1000$"
    "Net Worth: -33000$ "
    "debt: 34000 "
    "turns left: 9 "
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
    "Bombs R US: + || -",
    "Medicine INC + || -",
    "Fast Cars 4 U + || -",
    "AI Overlords + || -",
    "Crypto Bros + || -"
]
stock_own = [
    "Bombs R US: 0",
    "Medicine INC: 11",
    "Fast Cars 4 U: 123",
    "AI Overlords:7",
    "Crypto Bros: 212"
]
stock_avg = [
    "Bombs R US: 93$",
    "Medicine INC: 122$",
    "Fast Cars 4 U: 10$",
    "AI Overlords: 72:",
    "Crypto Bros: 31$"
]
stock_current = [
    "Bombs R US: 100$",
    "Medicine INC: 100$",
    "Fast Cars 4 U: 100$",
    "AI Overlords: 100$",
    "Crypto Bros: 100$"
]
stock_last = [
    "Bombs R US: 11%",
    "Medicine INC: -11%",
    "Fast Cars 4 U: -12%",
    "AI Overlords: 122%",
    "Crypto Bros: 1000%"
]


#basic stocks list function, cycles through the list and prints it to the window.
def stocks(stock_list, window, start_row, start_col):
    for index, string in enumerate(stock_list):
        window.addstr(start_row + index, start_col, string)
# start_row = Y axis, start_col = X axis.

#Everything below here is placeholder for UI purposes.

#Stealing from above to print out stats for UI purposes.
def stats(stats_list, window, start_row, start_col):
    for index, string in enumerate(stats_list):
        window.addstr(start_row + index, start_col, string)

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

