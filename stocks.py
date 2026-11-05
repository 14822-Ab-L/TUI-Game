
import random


class Stock:
    """Store information about one stock."""

    def __init__(
        self,
        stock_name,
        avg_stock_price,
        stock_owned,
        rate_change,
        current_price
    ):
        self.stock_name = stock_name
        self.avg_stock_price = avg_stock_price
        self.stock_owned = stock_owned
        self.rate_change = rate_change
        self.current_price = current_price


class Market:
    """Create and store the available stocks."""

    def __init__(self):
        self.stock_list = {
            "Bombs R US": Stock(
                "Bombs R US", 0.0, 0, 0.0,
                float(random.randint(50, 100))
            ),
            "Medicine INC": Stock(
                "Medicine INC", 0.0, 0, 0.0,
                float(random.randint(50, 100))
            ),
            "Fast Cars 4 U": Stock(
                "Fast Cars 4 U", 0.0, 0, 0.0,
                float(random.randint(50, 100))
            ),
            "AI Overlords": Stock(
                "AI Overlords", 0.0, 0, 0.0,
                float(random.randint(50, 100))
            ),
            "Crypto Bros": Stock(
                "Crypto Bros", 0.0, 0, 0.0,
                float(random.randint(50, 100))
            )
        }


class StockLogic:
    """Handle trading, prices, cash and net worth."""

    def __init__(
        self,
        market,
        cash=1000.0,
        debt=0.0,
        overdraft_limit=0.0
    ):
        self.market = market
        self.cash = cash
        self.debt = debt
        self.overdraft_limit = overdraft_limit

    def trade(self, action, stock_name, quantity):
        """Buy or sell a specified number of shares."""

        if stock_name not in self.market.stock_list:
            return False, "Stock not found."

        if not isinstance(quantity, int) or quantity <= 0:
            return False, "Quantity must be a positive whole number."

        stock = self.market.stock_list[stock_name]
        price = stock.current_price

        if action == "buy":
            total_cost = price * quantity

            available_funds = self.cash + self.overdraft_limit

            if total_cost > available_funds:
                return False, "Insufficient funds."

            old_quantity = stock.stock_owned
            new_quantity = old_quantity + quantity

            # Calculate the weighted average purchase price.
            total_cost_basis = (
                old_quantity * stock.avg_stock_price
                + total_cost
            )

            stock.avg_stock_price = (
                total_cost_basis / new_quantity
            )

            stock.stock_owned = new_quantity
            self.cash -= total_cost

            return True, (
                f"Bought {quantity} shares of {stock_name}."
            )

        if action == "sell":
            if quantity > stock.stock_owned:
                return False, "Not enough shares to sell."

            total_sale = price * quantity

            stock.stock_owned -= quantity
            self.cash += total_sale

            # Reset the average price if no shares remain.
            if stock.stock_owned == 0:
                stock.avg_stock_price = 0.0

            return True, (
                f"Sold {quantity} shares of {stock_name}."
            )

        return False, "Invalid action. Use 'buy' or 'sell'."

    def updateStock(self, changes=None):
        """Apply percentage changes to stock prices.

        Example:
            {"Bombs R US": 10} increases that stock by 10%.
        """

        if changes is None:
            changes = {}

        for name, stock in self.market.stock_list.items():
            old_price = stock.current_price
            percentage_change = changes.get(name, 0.0)

            new_price = old_price * (
                1 + percentage_change / 100
            )

            # Temporary minimum stock price.
            stock.current_price = max(0.01, new_price)

            # Calculate the actual percentage change.
            stock.rate_change = self.calcStock(
                old_price,
                stock.current_price
            )

    @staticmethod
    def calcStock(old_price, new_price):
        """Calculate percentage change between two prices."""

        if old_price <= 0:
            return 0.0

        return (
            (new_price - old_price) / old_price
        ) * 100

    def net_worth(self):
        """Calculate cash plus stock value minus debt."""

        holdings_value = sum(
            stock.stock_owned * stock.current_price
            for stock in self.market.stock_list.values()
        )

        return self.cash + holdings_value - self.debt
