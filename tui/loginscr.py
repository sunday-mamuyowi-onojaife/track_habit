from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Input,Header,Footer,Label,Static
from textual.containers import Horizontal
from textual import on

class SignIn(Static):
    """A widget to display elapsed time."""
class LoginScreen(Screen):
    CSS_PATH = "screen.tcss"




    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield SignIn('Sign In')

        yield Input(placeholder="Enter email address", id='login_email')
        yield Input(placeholder="Enter Password", password=True,id='login_password')


        yield Horizontal(Button('Login', id='login_loginbut'),Button('Reset Field', id='login_loginreset'))
        yield Horizontal(Button("Don't have an account yet, click now for one!", id='login_noaact'))





        yield Footer()

    @on(Input.Submitted, "#login_email")
    def accept_user(self):
        input = self.query_one("#login_email")

        self.username = input.value
        self.mount(Label(self.username))
