import curses
import random


DEFAULT_NOTICES = [
    "Market opens cautiously after overnight trading",
    "Bombs R Us announces a surprise product launch",
    "Local cat rescued from tree; shares remain unchanged",
    "Analysts recommend watching the medical sector",
    "Cows go moo",
]


class NewsBanner:
    """Display one randomly selected story as a scrolling ticker."""

    def __init__(self, notices=None, row=13, left=1, right=1,
                 title="TODAY'S NEWS", live=True, scroll_speed=1):
        source = DEFAULT_NOTICES if notices is None else notices
        self.notices = list(source)
        self.row = row
        self.left = left
        self.right = right
        self.title = title
        self.live = live
        self.current_pos = 0
        self.scroll_speed = scroll_speed
        self.current_story = random.choice(self.notices) if self.notices else ""

    def set_notices(self, notices):
        """Replace the available stories and choose a new story."""
        self.notices = list(notices)
        self.pick_random_story()

    def add_notice(self, notice):
        """Add a story and choose a new story."""
        self.notices.append(str(notice))
        self.pick_random_story()

    def pick_random_story(self):
        """Choose one notice at random, avoiding an immediate repeat."""
        if not self.notices:
            self.current_story = ""
            return
        if len(self.notices) == 1:
            self.current_story = self.notices[0]
            return
        choices = [n for n in self.notices if n != self.current_story]
        self.current_story = random.choice(choices)
        self.current_pos = 0

    def ticker_text(self):
        """Return the selected story with spacing for continuous scrolling."""
        if not self.current_story:
            return ""
        return f"{self.current_story}   ***   "

    @staticmethod
    def ticker_loop_text(notices):
        """Return text with a separator for seamless looping."""
        result = "  ||  ".join(f"{index + 1}. {notice}" for index, notice in enumerate(notices))
        return result + "   ***   "

    def update(self):
        """Advance the scroll position with seamless wrapping."""
        full_text = self.ticker_text()
        if full_text:
            self.current_pos = (self.current_pos + self.scroll_speed) % len(full_text)

    @staticmethod
    def _safe_addnstr(window, row, column, text, width, attributes=0):
        """Write text without allowing curses to draw outside the window."""
        height, window_width = window.getmaxyx()
        if row < 0 or row >= height or column < 0 or column >= window_width - 1:
            return

        width = min(width, window_width - column - 1)
        if width > 0:
            try:
                window.addnstr(row, column, str(text), width, attributes)
            except curses.error:
                pass

    def draw(self, window):
        """Draw the title, separator, and ticker line."""
        height, width = window.getmaxyx()
        content_width = width - self.left - self.right - 1
        if content_width < 8 or self.row < 0 or self.row + 2 >= height:
            return

        self._safe_addnstr(window, self.row, self.left, self.title, content_width)

        if self.live:
            live_label = "[LIVE]"
            self._safe_addnstr(
                window, self.row,
                self.left + max(0, content_width - len(live_label)),
                live_label, len(live_label)
            )

        try:
            window.hline(self.row + 1, self.left, curses.ACS_HLINE, content_width)
        except curses.error:
            pass

        text = self.ticker_text()
        if text:
            width = len(text)
            scroll_stream = text * 2
            start = self.current_pos % width
            display_text = scroll_stream[start:start + content_width]
            if display_text:
                self._safe_addnstr(
                    window, self.row + 2, self.left,
                    display_text, content_width
                )
        else:
            self._safe_addnstr(
                window, self.row + 2, self.left,
                "", content_width
            )


def newsstories(stories, window, start_row, start_col):
    """Backward-compatible helper for drawing individual news lines."""
    for index, story in enumerate(stories):
        NewsBanner._safe_addnstr(
            window, start_row + index, start_col, story,
            window.getmaxyx()[1] - start_col - 1
        )

