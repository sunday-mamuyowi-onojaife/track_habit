from textual.app import App
from textual import on

from tui.MarkHabitScr import MarkHabitScreen
from tui.StopHabitScreen import StopHabitScreen
from tui.analyticScr import AnalyticScreen
from tui.create_habitscr import CreateHabitScreen
from tui.createhabit_modal import QuitScreen
from tui.loginscr import LoginScreen

from tui.authscr import AuthScreen
from textual.widgets import Button,Select
from habitdb import HabitDatabase
from habitapi import HabitAPI
from tui.register import RegisterScreen
from tui.stophabitmodal import StopHabitModal
from user import User

class HabitTrackingHelper(App):
    CSS_PATH = "tui/screen.tcss"
    BINDINGS = [
                ("r", "register_account", "Register An Account"),
                ("c", "create_habit", "Create New Habit"),
                ("a", "analytics", "Analytics"),
                ("v", "view_habit", "View all Habit"),
                ("s", "stop_habit", "Stop an Habit"),
                ("m", "mark_habit", "Mark an Habit"),
                ("l", "log_out", "Log Out"),
                ]

    SCREENS ={
        'login':LoginScreen(),

        'auth':AuthScreen([],'aa'),
        'createhabit':CreateHabitScreen([],'aa'),
        'analy': AnalyticScreen([], 'aa'),
        'stop_habit':StopHabitScreen([], 'aa'),
        'mark_habit': MarkHabitScreen([], 'aa'),
        'registry':RegisterScreen()
    }

    def __init__(self):
        super().__init__()
        self.binder='INCORRECT'
        self.db = HabitDatabase()
        self.db.connect()
        self.hapi = HabitAPI(self.db)
        self.vall=[]


    def on_mount(self) -> None:
        #self.install_screen(LoginScreen())
        #self.install_screen(RegisterScreen())

        self.push_screen('login')
    ############################################################################################

    def action_register_account(self) -> None:
        self.push_screen(RegisterScreen())



    def action_mark_habit(self) -> None:
        if self.binder == 'INCORRECT':
            pass
        else:
            #self.push_screen('createhabit')
            self.push_screen(MarkHabitScreen(self.vall, self.hapi))


    def action_create_habit(self) -> None:
        if self.binder == 'INCORRECT':
            pass
        else:
            #self.push_screen('createhabit')
            self.push_screen(CreateHabitScreen(self.vall, self.hapi))

    def action_view_habit(self) -> None:
        if self.binder == 'INCORRECT':
            pass
        else:
            #self.push_screen('createhabit')
            self.push_screen(AuthScreen(self.vall,self.hapi))


    def action_analytics(self) -> None:
        if self.binder == 'INCORRECT':
            pass
        else:
            #self.push_screen('createhabit')
            self.push_screen(AnalyticScreen(self.vall,self.hapi))



    def action_stop_habit(self) -> None:
        if self.binder == 'INCORRECT':
            pass
        else:
            #self.push_screen('createhabit')
            self.push_screen(StopHabitScreen(self.vall,self.hapi))

    def action_log_out(self) -> None:
        app.exit()
    ####################################################################################################



    ####################################################################################################




    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""

        if event.button.id == "login_loginreset":
            self.query_one("#login_email").clear()
            self.query_one("#login_password").clear()
            

        if event.button.id == "login_noaact":
            self.push_screen(RegisterScreen())
        if event.button.id == "register_register":
            username = self.query_one("#register_username").value
            email = self.query_one("#register_email").value
            pwd = self.query_one("#register_password").value

            if len(username)>2 and len(email)>10 and len(pwd)>2:
                user = self.hapi.register_user(email, username, pwd)
                val = self.hapi.login(email, pwd)
                self.vall = val

                self.binder = 'CORRECT'
                db = HabitDatabase()
                db.connect()
                # user = User(val[0], val[1], db)
                # email = val[2]

                self.push_screen(AuthScreen(self.vall, self.hapi))

            else:
                self.query_one('#register_status').pro = 'The data you filled in is not correct, fill it correctly to register with the system, PRESS the RESET Field button'
                self.query_one('#register_status').remove_class('hidee')
                self.query_one('#register_status').add_class('showw')
                self.query_one('#register_status').add_class('reder')

        if event.button.id == "register_reset":
            self.query_one('#register_status').remove_class('showw')
            self.query_one('#register_status').add_class('hidee')
            self.query_one('#register_username').clear()
            self.query_one('#register_email').clear()
            self.query_one('#register_password').clear()

        if event.button.id == "register_exit":
            app.exit()

        if event.button.id == "login_loginbut":
            input = self.query_one("#login_email")
            input2 = self.query_one("#login_password")

            username = input.value
            pwd=input2.value

            val = self.hapi.login(username, pwd)
            self.vall=val
            if val[0] == 'INCORRECT':
                input.value=''
                input2.value = ''
            else:
                self.binder = 'CORRECT'
                db = HabitDatabase()
                db.connect()
                #user = User(val[0], val[1], db)
                #email = val[2]
                self.push_screen(AuthScreen(self.vall,self.hapi))


        if event.button.id == "createhabit_but":
            taskk=str(self.query_one('#task').value)
            freq_val=str(self.query_one('#freq').value)

            chosen_days = str(self.query_one('#hidden_field').value)
            if freq_val == 'Daily':
                self.hapi.add_habit(self.vall[0], taskk, freq_val, target_days=None)

            if freq_val == 'Weekly' and len(chosen_days) > 0 and len(taskk) > 3:
            #if freq_val == 'Weekly' and taskk > 3:
                # days_string= self.listToString(self.selected_days)
                self.hapi.add_habit(self.vall[0], taskk, freq_val, target_days=chosen_days)

            self.push_screen(QuitScreen())


        if event.button.id == "loginid2":

            self.push_screen('login')

        if event.button.id == "createanother_habit":
            self.push_screen(CreateHabitScreen(self.vall, self.hapi))

        if event.button.id == "exit_create":
            self.push_screen(AuthScreen(self.vall, self.hapi))



        if event.button.id == "_habit_modal":
            self.push_screen(AuthScreen(self.vall, self.hapi))

        if event.button.id == "stop_habit_":
            self.hapi.stop_habit(self.query_one('#zzzzz').value)
            self.push_screen(StopHabitModal())

if __name__ == "__main__":
    app = HabitTrackingHelper()
    app.run()