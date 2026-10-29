import curses

def title_screen(window): # title screen for game
    window.clear()
    window.addstr(10,10,"Welcome to stonks game")  # title
    window.addstr(12,10, "Enter your First name: ")
    window.refresh()
    curses.echo()
    name = window.getstr().decode("utf-8")
    curses.noecho()
    window.clear()
    window.addstr(5, 5, f"Hello, {name}!")
    window.addstr(7, 5, "Press any key to continue...")
    window.refresh()
    return name
