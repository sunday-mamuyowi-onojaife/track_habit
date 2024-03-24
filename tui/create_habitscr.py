from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Input,Header,Footer,Static,Label, Select,Log
from textual.containers import Horizontal,ScrollableContainer


from user import User
from tui.habit_table import TableApp
from textual import on
from textual.reactive import reactive


class Creathabit(Static):
    """A widget to display elapsed time."""
class Prog(Static):
    pro = reactive('')

    def render(self) -> str:

        return f"{self.pro}\n"

class UserDisplay(Static):
    """A widget to display elapsed time."""
LINES="""Choose Frequency
Daily
Weekly""".splitlines()

LINES2="""Pick days for habit
Sunday
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday""".splitlines()

class CreateHabitScreen(Screen):
    CSS_PATH = "screen.tcss"
    disp = reactive("Kilo")
    selectedDays=[]
    allowed = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


    def __init__(self,u,apii):
        super().__init__()
        self.userList=u
        self.hapi=apii

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        yield Creathabit('Create New Habit')
        yield Input(placeholder="Specify A Task", id='task')
        yield Select(options=((line,line) for line in LINES),id='freq',prompt='Choose Frequency',classes='showw' )
        yield Select(options=((line, line) for line in LINES2), id='dayy',prompt='Pick days for habit',classes='hidee' )
        #yield Select.from_values(LINES)
        #yield Label(self.userList[2])

        yield Prog(id='display_selected_days',classes='hidee')


        yield Horizontal(Button('Create Habit', id='createhabit_but'), Button('Reset Field', id='createhabit_rest'))

        yield Input(id='hidden_field',classes='hidee')
        yield Footer()


    def listToString(self,s):

        # initialize an empty string
        str1 = " "

        # return string
        return (str1.join(s))
    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:

        self.title = str(event.value)
        if self.title == 'Weekly':
            self.query_one('#dayy').remove_class('hidee')
            self.query_one('#dayy').add_class('showw')
            self.query_one('#display_selected_days').remove_class('hidee')
            self.query_one('#display_selected_days').add_class('showw')
        elif self.title == 'Daily' or self.title == 'Choose Frequency':
            self.query_one('#dayy').remove_class('showw')
            self.query_one('#dayy').add_class('hidee')

            self.query_one('#display_selected_days').remove_class('showw')
            self.query_one('#display_selected_days').add_class('hidee')

        if self.title == 'Pick days for habit':
            pass

        if self.title in self.allowed:
            if self.title in self.selectedDays:
                pass
            else:
                self.selectedDays.append(self.title)

        self.query_one(Prog).pro='Chosen days : '+self.listToString(self.selectedDays)
        self.query_one('#hidden_field').value = self.listToString(self.selectedDays)




    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""

        if event.button.id == "createhabit_rest":
            options = [("Choose Frequency", 'Choose Frequency'), ("Daily", "Daily"), ("Weekly", "Weekly")]
            self.query_one('#freq').set_options(options)

            options = [("Pick days for habit", 'Pick days for habit'), ("Sunday", "Sunday"), ("Monday", "Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"), ("Thursday", "Thursday"),("Friday", "Friday"),("Saturday", "Saturday")]
            self.query_one('#dayy').set_options(options)

            self.query_one(Prog).pro = 'No chosen days for weekly habit'
            self.selectedDays.clear()
            self.query_one('#task').clear()





    '''
    @on(Select.Changed,'#freq')
    def select_changed(self, event: Select.Changed) -> None:
        self.title = str(event.value)
        if self.title == 'Weekly':
            self.query_one('#dayy').remove_class('hidee')
            self.query_one('#dayy').add_class('showw')
            self.query_one('#display_selected_days').remove_class('hidee')
            self.query_one('#display_selected_days').add_class('showw')
        elif self.title != 'Weekly':
            self.query_one('#dayy').remove_class('showw')
            self.query_one('#dayy').add_class('hidee')

            self.query_one('#display_selected_days').remove_class('showw')
            self.query_one('#display_selected_days').add_class('hidee')

    @on(Select.Changed, '#dayy')
    def select_changed(self, event: Select.Changed) -> None:
        self.title = str(event.value)
        self.query_one('#display_selected_days').remove_class('hidee')
        self.query_one('#display_selected_days').add_class('showw')
    '''




















