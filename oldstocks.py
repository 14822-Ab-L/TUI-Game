import random

stock_buy = [
    "+ || -",
    "+ || -",
    "+ || -",
    "+ || -",
    "+ || -"
]

class Stock:
    def __init__(self, stock_name, avg_stock_price, stock_owned, rate_change, current_price):
        self.stock_name = stock_name
        self.avg_stock_price = avg_stock_price
        self.stock_owned = stock_owned
        self.rate_change = rate_change
        self.current_price = current_price


class Market:
    def __init__(self):
        self.stock_list = {
            "Bombs R US": Stock("Bombs R US", 0, 0, 0, random.randint(50, 100)), 
            "Medicine INC": Stock("Medicine INC", 0, 0, 0, random.randint(50, 100)),
            "Fast Cars 4 U": Stock("Fast Cars 4 U", 0, 0, 0, random.randint(50, 100)),
            "AI Overlords": Stock("AI Overlords", 0, 0, 0, random.randint(50, 100)),
            "Crypto Bros": Stock("Crypto Bros",0, 0, 0, random.randint(50, 100))
        }

class StockLogic:
    def trade(self):
        # Buy and Sell stock function here
        pass

    def updateStock(self):
        # Update Avg Stock 
        # Update prices and calculate daily changes
        # Update the percentage change in the stock (%)
        pass

    def calcStock():
        # Calculate percentage change from the old price.
        pass

    