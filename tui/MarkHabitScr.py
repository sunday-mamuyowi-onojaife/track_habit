from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Input,Header,Footer,Static
from textual.containers import Horizontal,ScrollableContainer

from tui.all_daily_habit import AllTrackedDailyHabit
from tui.all_weekly_habit import AllTrackedWeeklylyHabit
from tui.currently_tracked_habit import CurrentlyTrackedHabit
from tui.marker import Marker
from tui.streak import Streak
from user import User
from tui.habit_table import TableApp




class UserDisplay(Static):
    """A widget to display elapsed time."""

class MarkHabitScreen(Screen):
    CSS_PATH = "screen.tcss"

    def __init__(self,u,apii):
        super().__init__()
        self.userList=u
        self.hapi=apii

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        #yield UserDisplay(self.userList[2])
        cat = "Mark An Habit As Done"
        yield ScrollableContainer(UserDisplay(cat),
                                  Marker(self.userList,self.hapi)

                                  )






        yield Footer()

