import curses

curses.noecho() # Turn off key echoing
curses.cbreak() # Turn off buffered input
curses.curs_set(0) # Set cursor visibility to off
stdscr.keypadmode(True) # Turn on keypad mode
