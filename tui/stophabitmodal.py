from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label



class StopHabitModal(Screen):
    """Screen with a dialog to quit."""

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("The selected habit have deactived/stopped!!!", id="question"),
            Button("Back to Habit View", variant="primary", id="_habit_modal"),
            Button("Exit", variant="default", id="quit"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()



