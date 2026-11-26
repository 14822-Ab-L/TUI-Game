import curses

TITLE_ART = r'''
+--------------------------------------------------------------+
|  0.560  ^    1.286  ^    2.286  v    1.456  ^    0.168  ^   |
|                                                             |
|          .-""""""-.                              ########## |
|        .'          '.                              ######## |
|       /              \                            ######### |
|      |       _    _   |                          ####  #### |
|      |      (.)  (.)  |                        ####    #### |
|      |          >     |                      ####           |
|      |       .---.    |                    ####             |
|       \              /                   ####               |
|        '._        _.'                  ####                 |
|          /'------'\                  ####                   |
|     ____/ \      / \____           ####                     |
|   .'       \    /       '.       ####                       |
|  /          \  /          \    ####                         |
| /     |      \/      |     \ ####                           |
| |     |      /\      |     |###                             |
| |     \      ||      /     |                                |
| |      \____________/      |   ____ _____ ___  _   _ _  __ |
| |       ____________       |  / ___|_   _/ _ \| \ | | |/ / |
| |______/            \______|  \___ \ | || | | |  \| | ' /  |
|  |                         |   ___) || || |_| | |\  | . \  |
|  |                         |  |____/ |_| \___/|_| \_|_|\_\ ||
| |                         |                                 |
| 0.234 ^    0.1204 v    0.1902 ^    1.0287 ^    999.99 ^     |
+--------------------------------------------------------------+
'''.strip('\n')

def title_screen(window): # title screen for game
    window.clear()
    window.addstr(2, 10, "Welcome to the Stonks Game!")  # title
    rows, columns = window.getmaxyx()
    art_lines = TITLE_ART.splitlines()
    art_column = min(10, max(0, columns - max(map(len, art_lines))))
    visible_lines = art_lines[:max(0, rows - 13)]
    for row, line in enumerate(visible_lines, start=4):
        window.addnstr(row, art_column, line, columns - art_column)
    prompt = "Enter your First name: "
    prompt_row = 5 + len(visible_lines)
    window.addstr(prompt_row, 10, prompt)
    window.addstr(12 + len(visible_lines), 10, "By Tyren, Albert & Cale.")
    window.refresh()
    curses.echo()
    name = window.getstr(prompt_row, 10 + len(prompt)).decode("utf-8")
    curses.noecho()
    window.clear()
    window.refresh()
    window.addstr(5, 5, f"Hello, {name}!")
    window.addstr(7, 5, "Press any key to continue...")
    window.refresh()
    window.getch()  # Wait for user input before proceeding
    return name
