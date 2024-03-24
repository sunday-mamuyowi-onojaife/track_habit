import random

from rich.console import RenderableType, ConsoleRenderable
from textual.app import ComposeResult
from textual.widgets import DataTable
from textual.widgets import Static,Label
from itertools import cycle
from textual import on
from textual.reactive import reactive
from textual.widget import Widget
from tui.progress_table import *

class ZeroDisplay(Static):
    """A widget to display elapsed time."""
class Header1(Static):
    """A widget to display elapsed time."""


class CurrentlyTrackedHabit(Static):

    def __init__(self,u,apii):
        super().__init__()
        self.userList = u
        self.hapi = apii
        self.headertuple=("Habit ID","Task","Frequency","Period","Status","Start Date")
        self.rows = []
        self.rows.append(self.headertuple)
        self.list_of_habitid = self.hapi.list_of_a_user_habits(self.userList[0])
        self.listLen=len(self.list_of_habitid)
        self.table = DataTable(id='currently_tracked_habit')






        for habit in self.list_of_habitid:
            thistuple = tuple((habit['habit_id'], habit['task'], habit['frequency'],habit['period'],habit['status'],habit['start_date']))
            self.rows.append(thistuple)




    def compose(self) -> ComposeResult:
        if self.listLen==0:
            yield ZeroDisplay("No habit registered yet")
        else:
            #self.myVal=self.query_one(Who2).who2
            yield Header1('ALL CURRENTLY TRACKED HABITS')
            yield self.table


    #def render(self) -> RenderableType:

    def on_mount(self) -> None:
        if self.listLen == 0:
            pass
        else:

            table = self.query_one('#currently_tracked_habit')
            table.add_columns(*self.rows[0])
            table.add_rows(self.rows[1:])
            table.cursor_type = 'row'
            table.zebra_stripes = True



