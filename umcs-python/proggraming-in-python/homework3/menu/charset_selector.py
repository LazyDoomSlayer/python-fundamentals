import curses
import string

from menu.charset_set import CharacterSet


class CharsetSetSelector:
    """
    A class for selecting character sets to simulate, supporting both curses-based
    and text-based fallback menus.
    """

    def __init__(self):
        """
        Initializes the available character sets.
        """
        self.charsets = [charset.value[0] for charset in CharacterSet]

    def curses_menu(self, stdscr) -> str:
        """
        Interactive menu using curses.

        Args:
            stdscr: The curses standard screen object.

        Returns:
            str: The selected character set.
        """
        current_selection = 0

        while True:
            stdscr.clear()
            stdscr.addstr("Select a character set:\n", curses.A_BOLD)
            stdscr.addstr("Use UP/DOWN to navigate and ENTER to select.\n\n")

            for idx, charset in enumerate(self.charsets):
                if idx == current_selection:
                    stdscr.addstr(f"> {charset}\n", curses.A_REVERSE)
                else:
                    stdscr.addstr(f"  {charset}\n")

            stdscr.refresh()

            key = stdscr.getch()
            if key == curses.KEY_UP and current_selection > 0:
                current_selection -= 1
            elif key == curses.KEY_DOWN and current_selection < len(self.charsets) - 1:
                current_selection += 1
            elif key in [curses.KEY_ENTER, 10, 13]:
                return self.charsets[
                    current_selection
                ]

    def fallback_menu(self) -> str:
        """
        Fallback text-based menu for non-interactive environments.

        Returns:
            str: The selected character set.
        """
        print("Curses not supported. Falling back to text-based menu.")
        print("\nSelect a character set:")
        for idx, charset in enumerate(self.charsets, start=1):
            print(f"{idx}) {charset}")
        choice = input("Enter the number of your choice: ").strip()
        return self.charsets[int(choice) - 1]

    def get_selection(self) -> str:
        """
        Displays the character set selection menu, falling back to text-based if curses fails.

        Returns:
            str: The selected character set.
        """
        try:
            selected_option = curses.wrapper(self.curses_menu)
        except curses.error:
            selected_option = self.fallback_menu()

        charset_enum = CharacterSet.get_by_name(selected_option)
        if charset_enum == CharacterSet.CUSTOM:
            return input("Enter your custom character set: ")
        return charset_enum.value[1] if charset_enum else string.digits
