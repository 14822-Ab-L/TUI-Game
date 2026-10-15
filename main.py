import curses
import terminal_ui

def main(window: curses.window):
    window.keypad(True) # Turn on keypad mode
    curses.noecho() # Turn off key echoing
    curses.curs_set(0) # Set cursor visibility
    curses.cbreak() # Turn off buffered input


    while 1: # Loop so the game doesn't exit instantly
        window.box()
        terminal_ui.draw_dashboard(window) # Calls the UI
        window.refresh() # Refresh

if __name__ == '__main__':
    curses.wrapper(main) # Initialise and return the window to main()
