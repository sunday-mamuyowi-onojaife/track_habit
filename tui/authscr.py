from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Input,Header,Footer,Static
from textual.containers import Horizontal,ScrollableContainer
from user import User
from tui.habit_table import TableApp




class UserDisplay(Static):
    """A widget to display elapsed time."""

class AuthScreen(Screen):
    CSS_PATH = "screen.tcss"

    def __init__(self,u,apii):
        super().__init__()
        self.userList=u
        self.hapi=apii

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        #yield UserDisplay(self.userList[2])
        cat = self.userList[2]+ '[' +self.userList[1]+']'
        yield ScrollableContainer(UserDisplay(cat),
                                  TableApp(self.userList,self.hapi)

                                  )






        yield Footer()

