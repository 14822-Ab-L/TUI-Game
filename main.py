import curses
import terminal_ui
import titlescreen
import playerstats

def main(window: curses.window):
    window.keypad(True) # Turn on keypad mode
    curses.noecho() # Turn off key echoing
    curses.curs_set(0) # Set cursor visibility
    curses.cbreak() # Turn off buffered input
    name = titlescreen.title_screen(window) #name catches the input given in the title screen
    window.clear() #You need clear after a window is finshed, not after player. lost 1 hour learning this the hard way.
    player = playerstats.Player(name, 1/10/2026, 1000,-10000,10000,9) # starting starts after retrieving name input.
    #(name, date, balance, net_worth, debt, turns)


    while 1: # Loop so the game doesn't exit instantly
        window.box()

        player.display_stats(window)
        terminal_ui.draw_dashboard(window) # Calls the UI
        window.refresh() # Refresh

if __name__ == '__main__':
    curses.wrapper(main) # Initialise and return the window to main()
