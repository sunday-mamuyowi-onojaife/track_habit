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
class Header2(Static):
    """A widget to display elapsed time."""
class Header3(Static):
    """A widget to display elapsed time."""
class HabitRow(Static):
    hab = reactive('')

    def render(self) -> str:

        return f"{self.hab}\n"

class HabitRow2(Static):
    hab2 = reactive('')

    def render(self) -> str:

        return f"{self.hab2}\n"

class HabitRow3(Static):
    hab3 = reactive('')

    def render(self) -> str:

        return f"{self.hab3}\n"

class Streak(Static):
    hab = reactive("")
    hab2 = reactive("")
    hab3 = reactive("")
    def __init__(self,u,apii):
        super().__init__()
        self.userList = u
        self.hapi = apii
        self.headertuple=("Habit ID","Task","Frequency","Period","Status","Start Date")
        self.rows = []
        self.rows.append(self.headertuple)
        self.list_of_habitid = self.hapi.list_of_a_user_habits(self.userList[0])
        self.listLen=len(self.list_of_habitid)
        self.table = DataTable(id='streak')






        for habit in self.list_of_habitid:
            thistuple = tuple((habit['habit_id'], habit['task'], habit['frequency'],habit['period'],habit['status'],habit['start_date']))
            self.rows.append(thistuple)




    def compose(self) -> ComposeResult:
        if self.listLen==0:
            yield ZeroDisplay("No habit registered yet")
        else:
            #self.myVal=self.query_one(Who2).who2
            yield Header1('Click On Any Row or Habit To View Its Streak')
            yield self.table

            yield Header2('Streak Information on Observed Habit Pattern')
            yield Header3('0 means the habit was broken, 1 means the habit was observed\n')
            yield HabitRow(self.hab)
            yield HabitRow2(self.hab2)
            yield HabitRow3(self.hab3)


    #def render(self) -> RenderableType:

    def on_mount(self) -> None:
        if self.listLen == 0:
            pass
        else:

            table = self.query_one('#streak')
            table.add_columns(*self.rows[0])
            table.add_rows(self.rows[1:])
            table.cursor_type = 'row'
            table.zebra_stripes = True

    def calculate_streak(self,completions):
        """
        Calculates the current streak based on a list of habit completions.

        Parameters:
        - completions (list): A list of habit completion data (e.g., [1, 1, 0, 1, 1]) where 1 represents a successful completion.

        Returns:
        - int: The current streak.
        """
        current_streak = 0
        max_streak = 0

        for completion in completions:
            if completion == 1:  # Successful completion
                current_streak += 1
            else:  # Breaks the streak
                max_streak = max(max_streak, current_streak)
                current_streak = 0

        return max(max_streak, current_streak)

    @on(DataTable.RowSelected)
    def on_row_clicked(self, event: DataTable.RowSelected) -> None:
        table = event.data_table
        row = table.get_row(event.row_key)


        self.query_one(HabitRow).hab = str(row)

        # self.query_one(Who2).who2 = str(row[0])
        li = self.hapi.get_habit_all_days_and_fulfilled(str(row[0]))
        all_days = li[0]
        days_fulfilled = li[1]
        habit_completions = []

        for i in all_days:
            if i in days_fulfilled:
                habit_completions.append(1)
            else:
                habit_completions.append(0)


        self.query_one(HabitRow).hab = str(f'\n\n{row}\n')
        self.query_one(HabitRow2).hab2 = str(f'Habit observation pattern : {habit_completions}\n')
        current_streak = self.calculate_streak(habit_completions)


        self.query_one(HabitRow3).hab3 = str(f'Current Streak or Highest Streak: {current_streak}')
