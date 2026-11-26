import stocks
import curses

from timeline import Timeline


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

news_menu = [
    ("Todays news:", 2),
    ("Place holder:", 40),
    ("Logo here?", 100)
]

stories = [
    "News stories will appear here."
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


# Safely draw text within the terminal window.
def draw_text(window, row, column, text):
    height, width = window.getmaxyx()

    if 0 <= row < height and 0 <= column < width - 1:
        available_width = width - column - 1

        window.addnstr(
            row,
            column,
            str(text),
            available_width
        )


# Displays a list of strings in the window.
def stocks(stock_list, window, start_row, start_col):
    for index, string in enumerate(stock_list):
        draw_text(
            window,
            start_row + index,
            start_col,
            string
        )


# Displays the player statistics.
def stats(stats_list, window, start_row, start_col):
    stats_line = " | ".join(stats_list)

    draw_text(
        window,
        start_row,
        start_col,
        stats_line
    )


# Displays the column headings.
def draw_headings(headings, window, row):
    for label, column in headings:
        draw_text(window, row, column, label)


# Displays the buy and sell placeholders.
def stockbuy(stock_buy, window, start_row, start_col):
    for index, string in enumerate(stock_buy):
        draw_text(
            window,
            start_row + index,
            start_col,
            string
        )


# Displays stock names from Stock objects.
def stocknames(stock_list, window, start_row, start_col):
    for index, stock in enumerate(stock_list):
        draw_text(
            window,
            start_row + index,
            start_col,
            stock.stock_name
        )


# Displays the number of shares owned.
def stockown(stock_list, window, start_row, start_col):
    for index, stock in enumerate(stock_list):
        draw_text(
            window,
            start_row + index,
            start_col,
            f": {stock.stock_owned}"
        )


# Displays the average purchase price.
def stockavg(stock_list, window, start_row, start_col):
    for index, stock in enumerate(stock_list):
        draw_text(
            window,
            start_row + index,
            start_col,
            f": ${stock.avg_stock_price:.2f}"
        )


# Displays the current stock price.
def stockcurrent(stock_list, window, start_row, start_col):
    for index, stock in enumerate(stock_list):
        draw_text(
            window,
            start_row + index,
            start_col,
            f": ${stock.current_price:.2f}"
        )


# Displays the price change from the previous turn.
def stocklast(stock_list, window, start_row, start_col):
    for index, stock in enumerate(stock_list):
        draw_text(
            window,
            start_row + index,
            start_col,
            f": {stock.rate_change:+.2f}%"
        )


# Displays the news stories.
def newsstories(stories, window, start_row, start_col):
    for index, string in enumerate(stories):
        draw_text(
            window,
            start_row + index,
            start_col,
            string
        )


# Displays the settings menu.
def settings(settings_list, window, start_row, start_col):
    for index, string in enumerate(settings_list):
        draw_text(
            window,
            start_row + index,
            start_col,
            string
        )


# Displays the end-day button placeholder.
def endgamebutton(end_game_button, window, start_row, start_col):
    for index, string in enumerate(end_game_button):
        draw_text(
            window,
            start_row + index,
            start_col,
            string
        )


def draw_dashboard(
    window,
    market,
    logic,
    selected_stock=0,
    selected_action="buy",
    trade_indicators=None
):
    """Draw the dashboard and highlight the selected control."""

    window.erase()
    window.box()

    stock_list = list(market.stock_list.values())

    # Retrieve the player's current statistics.
    current_stats = [
        f"Name: {logic.player.name}",
        f"Current balance: ${logic.player.balance:,.2f}",
        f"Net Worth: ${logic.net_worth():,.2f}",
        f"Debt: ${logic.player.debt:,.2f}",
        f"Turns left: {logic.player.turns}"
    ]

    stats(current_stats, window, start_row=1, start_col=1)

    # Display stock information.
    stocknames(stock_list, window, start_row=5, start_col=2)
    stockbuy(stock_buy, window, start_row=5, start_col=20)
    stockown(stock_list, window, start_row=5, start_col=40)
    stockavg(stock_list, window, start_row=5, start_col=60)
    stockcurrent(stock_list, window, start_row=5, start_col=80)
    stocklast(stock_list, window, start_row=5, start_col=100)

    # Display the last successful trade indicator.
    if trade_indicators is None:
        trade_indicators = [""] * len(stock_list)

    for index, indicator in enumerate(trade_indicators):
        draw_text(
            window,
            5 + index,
            32,
            indicator
        )

    # Display column headings and news.
    draw_headings(headings, window, row=3)
    draw_headings(news_menu, window, row=13)
    newsstories(stories, window, start_row=15, start_col=2)

    # Display settings and end-day placeholder.
    settings(settings_list, window, start_row=21, start_col=2)

    endgamebutton(
        end_game_button,
        window,
        start_row=22,
        start_col=25
    )
    stocks(meme_logo_list, window, start_row=21, start_col=85)

    # Highlight the selected buy or sell control.
    if selected_stock < len(stock_list):
        row = 5 + selected_stock
        column = 20 if selected_action == "buy" else 25
        label = "+" if selected_action == "buy" else "-"

        height, width = window.getmaxyx()

        if 0 <= row < height - 1 and 0 <= column < width - 1:
            try:
                window.addstr(row, column, label, curses.A_REVERSE)
            except curses.error:
                pass

    # Highlight the End Day button when selected.
    else:
        row = 22
        column = 25
        label = end_game_button[0]

        height, width = window.getmaxyx()

        if 0 <= row < height - 1 and 0 <= column < width - 1:
            try:
                window.addnstr(
                    row,
                    column,
                    label,
                    width - column - 1,
                    curses.A_REVERSE
                )
            except curses.error:
                pass

    window.refresh()


def run_dashboard(window, market, logic):
    """Handle keyboard input and run the trading dashboard."""

    selected_stock = 0
    selected_action = "buy"
    stock_names = list(market.stock_list.keys())

    # End Day is the selection immediately after the last stock.
    end_day_index = len(stock_names)

    # Create the timeline once for the entire game.
    timeline = Timeline(
        total_turns=logic.player.turns,
        current_turn=0
    )

    trade_indicators = [""] * len(stock_names)
    trade_message = ""

    while True:
        draw_dashboard(
            window,
            market,
            logic,
            selected_stock,
            selected_action,
            trade_indicators
        )

        # Display the latest trade result.
        height, width = window.getmaxyx()

        if height > 20 and width > 3:
            window.addnstr(
                19,
                2,
                trade_message.ljust(width - 3),
                width - 3
            )
            window.refresh()

        key = window.getch()

        # Quit the dashboard.
        if key in (ord("q"), ord("Q")):
            break

        # Move selection up.
        elif key == curses.KEY_UP:
            selected_stock = (
                selected_stock - 1
            ) % (len(stock_names) + 1)

        # Move selection down.
        elif key == curses.KEY_DOWN:
            selected_stock = (
                selected_stock + 1
            ) % (len(stock_names) + 1)

        # Select buy.
        elif key == curses.KEY_LEFT:
            selected_action = "buy"

        # Select sell.
        elif key == curses.KEY_RIGHT:
            selected_action = "sell"

        # Execute the selected action.
        elif key in (curses.KEY_ENTER, 10, 13):

            # End Day option selected.
            if selected_stock == end_day_index:

                if timeline.advance_day(logic.player):
                    logic.net_worth()

                    if logic.player.turns == 0:
                        trade_message = (
                            f"Game finished on {logic.player.date}. ""0 turns remaining."
                        )

                    else:
                        trade_message = (
                            f"Advanced to {logic.player.date}. "
                            f"{logic.player.turns} turns remaining."
                        )
                else:
                    trade_message = "No turns remaining."

            # Stock selected.
            else:
                stock_name = stock_names[selected_stock]

                success, message = logic.trade(
                    selected_action,
                    stock_name,
                    1
                )

                trade_message = message

                if success:
                    if selected_action == "buy":
                        trade_indicators[selected_stock] = "↑"
                    else:
                        trade_indicators[selected_stock] = "↓"
