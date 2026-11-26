def dayscreen(window, day_number, day_name):
    window.clear()
    window.addstr(2, 10, f"Day {day_number}: {day_name}")
    window.addstr(4, 10, "Press any key to continue...")
    window.refresh()
    window.getch()  # Wait for user input before proceeding
