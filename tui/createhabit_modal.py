from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label



class QuitScreen(Screen):
    """Screen with a dialog to quit."""

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Your new Habit have been created!!!", id="question"),
            Button("Create Another Habit", variant="primary", id="createanother_habit"),
            Button("Exit To Habit's View", variant="default", id="exit_create"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()
        else:
            self.app.pop_screen()


