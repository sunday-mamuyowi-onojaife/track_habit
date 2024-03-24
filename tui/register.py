from textual.app import ComposeResult
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Button, Input,Header,Footer,Label,Static
from textual.containers import Horizontal
from textual import on

class SignIn(Static):
    """A widget to display elapsed time."""

class Prog(Static):
    pro = reactive('')

    def render(self) -> str:

        return f"{self.pro}\n"
class RegisterScreen(Screen):
    CSS_PATH = "screen.tcss"




    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield SignIn('Register An Account')

        yield Input(placeholder="Enter your username", id='register_username')
        yield Input(placeholder="Enter email address", id='register_email')
        yield Input(placeholder="Enter Password", password=True,id='register_password')


        yield Horizontal(Button('Register Account', id='register_register'),Button('Reset Field', id='register_reset'),Button('Exit', id='register_exit'))

        yield Prog(id='register_status',classes='hidee')




        yield Footer()

    @on(Input.Submitted, "#login_email")
    def accept_user(self):
        input = self.query_one("#login_email")

        self.username = input.value
        self.mount(Label(self.username))
