class Timeline:
    def __init__(self, total_turns, current_turn=0):
        self.total_turns = total_turns
        self.current_turn = current_turn

    def turns_left(self):
        """Return the number of turns remaining."""
        return self.total_turns - self.current_turn

    def advance_day(self, player):
        """Advance the day and consume the remaining turns."""

        if self.turns_left() <= 0:
            return False

        self.current_turn += 1
        player.turns = self.turns_left()

        if self.current_turn < self.total_turns:
            player.date = f"Day {self.current_turn + 1}"
        else:
            player.date = f"Day {self.total_turns}"

        return True