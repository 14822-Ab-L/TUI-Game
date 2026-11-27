import curses


DEFAULT_NOTICES = [
    "Market opens cautiously after overnight trading",
    "Bombs R Us announces a surprise product launch",
    "Local cat rescued from tree; shares remain unchanged",
    "Analysts recommend watching the medical sector",
    "Cows go moo",
]


class NewsBanner:
    """A reusable news ticker"""

    def __init__(self, notices=None, row=13, left=1, right=1,
                 title="TODAY'S NEWS", live=True, scroll_speed=1):
        self.notices = list(notices) if notices is not None else list(DEFAULT_NOTICES)
        self.row = row
        self.left = left
        self.right = right
        self.title = title
        self.live = live
        self.current_pos = 0
        self.scroll_speed = scroll_speed

    def set_notices(self, notices):
        self.notices = list(notices)

    def add_notice(self, notice):
        self.notices.append(str(notice))

    def ticker_text(self):
        return "  ||  ".join(
            f"{index + 1}. {notice}"
            for index, notice in enumerate(self.notices)
        )

    @staticmethod
    def ticker_loop_text(notices):
        """Return text with a separator for seamless looping."""
        result = "  ||  ".join(
            f"{index + 1}. {notice}"
            for index, notice in enumerate(notices)
        )
        return result + "   ***   "

    def update(self):
        """Advance the scroll position with seamless wrapping."""
        full_text = self.ticker_loop_text(self.notices)
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

        loop_text = self.ticker_loop_text(self.notices)
        full_stream = loop_text * 3
        start = min(self.current_pos % len(loop_text), len(loop_text) - content_width)
        display_text = full_stream[start:start + content_width]
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

