class Timeline:
    def __init__ (self, total_turns, current_turn):
        self.total_turns = total_turns
        self.current_turn = current_turn

    def turns_left(self): # Returns the number of turns left for the player
        return self.total_turns - self.current_turn
