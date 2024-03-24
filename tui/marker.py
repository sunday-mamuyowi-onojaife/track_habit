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

class HabitRow(Static):
    hab = reactive('')

    def render(self) -> str:

        return f"{self.hab}\n"

class HabitRow2(Static):
    hab2 = reactive('')

    def render(self) -> str:

        return f"{self.hab2}\n"
class Marker(Static):

    def __init__(self,u,apii):
        super().__init__()
        self.userList = u
        self.hapi = apii
        self.headertuple=("Habit ID","Task","Frequency","Period","Status","Start Date")
        self.rows = []
        self.rows.append(self.headertuple)
        self.list_of_habitid = self.hapi.list_of_a_user_habits(self.userList[0])
        self.listLen=len(self.list_of_habitid)
        self.table = DataTable(id='marker_habit')






        for habit in self.list_of_habitid:
            thistuple = tuple((habit['habit_id'], habit['task'], habit['frequency'],habit['period'],habit['status'],habit['start_date']))
            self.rows.append(thistuple)




    def compose(self) -> ComposeResult:
        if self.listLen==0:
            yield ZeroDisplay("No habit registered yet")
        else:
            #self.myVal=self.query_one(Who2).who2
            yield Header1('Click On A Row or Habit To Be Marked')
            yield self.table
            yield HabitRow()
            yield HabitRow2()


    #def render(self) -> RenderableType:

    def on_mount(self) -> None:
        if self.listLen == 0:
            pass
        else:

            table = self.query_one('#marker_habit')
            table.add_columns(*self.rows[0])
            table.add_rows(self.rows[1:])
            table.cursor_type = 'row'
            table.zebra_stripes = True

    @on(DataTable.RowSelected)
    def on_row_clicked(self, event: DataTable.RowSelected) -> None:
        table = event.data_table
        row = table.get_row(event.row_key)

        self.query_one(HabitRow).hab = '\n\nSelected Habit -->' + str(row)


        self.habitidd = row[4]
        if self.habitidd == 'IN_PROGRESS':
            li = self.hapi.get_habit_all_days_and_fulfilled(row[0])
            all_days = li[0]
            days_fulfilled = li[1]
            import datetime
            presentday = datetime.datetime.today()
            d = str(presentday)
            dd = d[:10]

            if dd == all_days[0]:
                f = "\n\tThe habit is due for marking today."
                self.query_one(HabitRow2).hab2 = f
                self.query_one(HabitRow2).add_class('greener')
                self.query_one(HabitRow2).remove_class('reder')
                checker=self.hapi.check_if_habit(self.userList[0], row[0], dd)
                if checker:
                    #needs to be marked
                    self.hapi.mark_habit_completed(self.userList[0], row[0], dd)
                    f = "\n\tThe Habit was just marked."
                    self.query_one(HabitRow2).hab2 = f
                    self.query_one(HabitRow2).add_class('greener')
                    self.query_one(HabitRow2).remove_class('reder')
                else:
                    # have been marked
                    f = "\n\tThe habit has already been marked for today."
                    self.query_one(HabitRow2).hab2 = f
                    self.query_one(HabitRow2).add_class('greener')
                    self.query_one(HabitRow2).remove_class('reder')

            else:
                f = "\n\tThe habit is not due for marking today."
                self.query_one(HabitRow2).hab2 = f
                self.query_one(HabitRow2).add_class('reder')
                self.query_one(HabitRow2).remove_class('greener')


        if self.habitidd == 'STOPPED':
            f="\n\tThis habit have been deactived, you can't mark it as done."
            self.query_one(HabitRow2).hab2 = f
            self.query_one(HabitRow2).add_class('reder')
            self.query_one(HabitRow2).remove_class('greener')
        
