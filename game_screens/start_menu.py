from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button
from textual.screen import Screen

class StartMenu(Screen):
    def compose(self) -> ComposeResult:
        yield HorizontalGroup(
            VerticalScroll(
                Button("Start Game"),
                Button("Load Game"),
                Button("Exit")
            )
        )
