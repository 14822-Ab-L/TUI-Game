import curses

def title_screen(window): # title screen for game
    window.clear()
    window.addstr(10,10,"Welcome to stonks game")  # title
    window.addstr(11,10,"Press enter to continue") # prompt for enter key
    window.addstr(12,10, "Enter your First name: ")
    window.refresh()
    curses.echo()
    name = window.getstr().decode("utf-8")
    curses.noecho()
    return name

