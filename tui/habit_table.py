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



class Arrange30(Static):
    def __init__(self,hapi,hid):
        super().__init__()
        self.hapi=hapi
        self.hid=hid


    def render(self)->ConsoleRenderable:
        """Create child widgets of a stopwatch."""
        #'11079963450879'
        li = self.hapi.get_habit_all_days_and_fulfilled(self.hid)
        all_days = li[0]
        days_fulfilled = li[1]


        for x in all_days:
            val =4

            if x in days_fulfilled:
                val = 1
            else:
                val = 0


            yield Marking(x,val)



class Arranger(Static):
    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Marking("", 1)
        yield Marking2("", 1)
        yield Marking3("", 1)
        yield Marking4("", 1)
        yield Marking5("", 1)
        yield Marking6("", 1)
        yield Marking7("", 1)
        yield Marking8("", 1)
        yield Marking9("", 1)
        yield Marking10("", 1)
        yield Marking11("", 1)
        yield Marking12("", 1)
        yield Marking13("", 1)
        yield Marking14("", 1)
        yield Marking15("", 1)
        yield Marking16("", 1)
        yield Marking17("", 1)
        yield Marking18("", 1)
        yield Marking19("", 1)
        yield Marking20("", 1)
        yield Marking21("", 1)
        yield Marking22("", 1)
        yield Marking23("", 1)
        yield Marking24("", 1)
        yield Marking25("", 1)
        yield Marking26("", 1)
        yield Marking27("", 1)
        yield Marking28("", 1)
        yield Marking29("", 1)
        yield Marking30("", 1)




class ZeroDisplay(Static):
    """A widget to display elapsed time."""

class Prog(Static):
    pro = reactive('PROGRESS [Click a row to view Habit Progress]')

    def render(self) -> str:

        return f"{self.pro}\n"

class HabitRow(Static):
    hab = reactive('')

    def render(self) -> str:

        return f"{self.hab}\n"


class Who2(Static):
    who2 = reactive('Red means you miss the task, Green mean you observed it.')

    def render(self) -> str:

        return f"{self.who2}\n"
class ProgressDisplay(Static):
    """A widget to display elapsed time."""
    who = reactive("")

    def render(self) -> str:
        return f"{self.who}\n"
class TableApp(Static):
    who = reactive("name")
    who2 = reactive("name")
    pro= reactive("name")
    hab=reactive("name")
    myVal=reactive("47312092427142")
    def __init__(self,u,apii):
        super().__init__()
        self.userList = u
        self.hapi = apii
        self.headertuple=("Habit ID","Task","Frequency","Period","Status","Start Date")
        self.rows = []
        self.rows.append(self.headertuple)
        self.list_of_habitid = self.hapi.list_of_a_user_habits(self.userList[0])
        self.listLen=len(self.list_of_habitid)
        self.table = DataTable(id='habitTablee')
        self.lab='free'
        #y=self.list_of_habitid[0]
        #self.query_one(Who2).who2 = '47312092427142'
        self.myVal= '47312092427142'
        #self.myVal = y['habit_id']





        for habit in self.list_of_habitid:
            thistuple = tuple((habit['habit_id'], habit['task'], habit['frequency'],habit['period'],habit['status'],habit['start_date']))
            self.rows.append(thistuple)




    def compose(self) -> ComposeResult:
        if self.listLen==0:
            yield ZeroDisplay("No habit registered yet")
        else:
            #self.myVal=self.query_one(Who2).who2
            yield Prog(self.pro)
            yield self.table

            yield ProgressDisplay(self.who)
            yield Who2(self.who2)
            yield HabitRow(self.hab)
            #yield Arrange30(self.hapi,self.myVal)
            #yield Marking("2023-04-05",1)
            #yield Marking2("2023-04-05", 1)
            #yield Label('rrrrrrrrrrrrrrrrr',id='kkk')
            yield Arranger()

    #def render(self) -> RenderableType:

    def on_mount(self) -> None:
        if self.listLen == 0:
            pass
        else:

            table = self.query_one('#habitTablee')
            table.add_columns(*self.rows[0])
            table.add_rows(self.rows[1:])
            table.cursor_type = 'row'
            table.zebra_stripes = True



    @on(DataTable.RowSelected)
    def on_row_clicked(self, event: DataTable.RowSelected) -> None:
        table = event.data_table
        row = table.get_row(event.row_key)
        #table = self.query_one('#habitTablee')
        #row = table.get_row(event.row_key)

        self.query_one(HabitRow).hab = str(row)

        #self.query_one(Who2).who2 = str(row[0])
        li = self.hapi.get_habit_all_days_and_fulfilled(str(row[0]))
        all_days = li[0]
        days_fulfilled = li[1]

        if len(all_days)==0:
            pass
        else:
            counter=0
            val=0
            for x in all_days:
                val = 4

                if x in days_fulfilled:
                    val=1
                else:
                    val = 0

                if counter<30:
                    if counter==0:


                        self.query_one(Marking).t = x
                        self.query_one(Marking).val = val
                    if counter==1:
                        self.query_one(Marking2).t = x
                        self.query_one(Marking2).val = val
                    if counter==2:
                        self.query_one(Marking3).t = x
                        self.query_one(Marking3).val = val
                    if counter==3:
                        self.query_one(Marking4).t = x
                        self.query_one(Marking4).val = val
                    if counter==4:
                        self.query_one(Marking5).t = x
                        self.query_one(Marking5).val = val
                    if counter==5:
                        self.query_one(Marking6).t = x
                        self.query_one(Marking6).val = val
                    if counter==6:
                        self.query_one(Marking7).t = x
                        self.query_one(Marking7).val = val
                    if counter==7:
                        self.query_one(Marking8).t = x
                        self.query_one(Marking8).val = val
                    if counter==8:
                        self.query_one(Marking9).t = x
                        self.query_one(Marking9).val = val
                    if counter==9:
                        self.query_one(Marking10).t = x
                        self.query_one(Marking10).val = val
                    if counter==10:
                        self.query_one(Marking11).t = x
                        self.query_one(Marking11).val = val
                    if counter==11:
                        self.query_one(Marking12).t = x
                        self.query_one(Marking12).val = val
                    if counter==12:
                        self.query_one(Marking13).t = x
                        self.query_one(Marking13).val = val
                    if counter==13:
                        self.query_one(Marking14).t = x
                        self.query_one(Marking14).val = val

                    if counter==14:
                        self.query_one(Marking15).t = x
                        self.query_one(Marking15).val = val

                    if counter==15:
                        self.query_one(Marking16).t = x
                        self.query_one(Marking16).val = val

                    if counter==16:
                        self.query_one(Marking17).t = x
                        self.query_one(Marking17).val = val

                    if counter==17:
                        self.query_one(Marking18).t = x
                        self.query_one(Marking18).val = val

                    if counter==18:
                        self.query_one(Marking19).t = x
                        self.query_one(Marking19).val = val

                    if counter==19:
                        self.query_one(Marking20).t = x
                        self.query_one(Marking20).val = val

                    if counter==20:
                        self.query_one(Marking21).t = x
                        self.query_one(Marking21).val = val

                    if counter==21:
                        self.query_one(Marking22).t = x
                        self.query_one(Marking22).val = val

                    if counter==22:
                        self.query_one(Marking23).t = x
                        self.query_one(Marking23).val = val

                    if counter==23:
                        self.query_one(Marking24).t = x
                        self.query_one(Marking24).val = val

                    if counter==24:
                        self.query_one(Marking25).t = x
                        self.query_one(Marking25).val = val

                    if counter==25:
                        self.query_one(Marking26).t = x
                        self.query_one(Marking26).val = val

                    if counter==26:
                        self.query_one(Marking27).t = x
                        self.query_one(Marking27).val = val

                    if counter==27:
                        self.query_one(Marking28).t = x
                        self.query_one(Marking28).val = val

                    if counter==28:
                        self.query_one(Marking29).t = x
                        self.query_one(Marking29).val = val
                    if counter==29:
                        self.query_one(Marking30).t = x
                        self.query_one(Marking30).val = val

                counter=counter+1
        '''
        y=['kasparov','polgar','karpov','carlsen']
        h = random.randint(0, 3)
        hh = random.randint(0, 1)
        f=[1,0]
        self.query_one(Marking).t=y[h]
        self.query_one(Marking).val = 0
        h = random.randint(0, 3)
        hh = random.randint(0, 1)
        self.query_one(Marking2).t = y[h]
        self.query_one(Marking2).val = 0
        '''










