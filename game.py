from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static
from textual.reactive import reactive

from game_classes import Map, Player, player_tile
from game_screens import StartMenu
from game_widgets import MapWidget


class GameApp(App):
    CSS = """
        MapWidget {
        height: 1fr;
        border: round white; /* Optional: adds a nice border */
        }
    """

    SCREENS = {"StartMenu": StartMenu}

    BINDINGS = [
        ("w", "move('up')", "Move Up"),
        ("s", "move('down')", "Move Down"),
        ("a", "move('left')", "Move Left"),
        ("d", "move('right')", "Move Right"),
        ("q", "quit", "Quit Game"),
    ]

    game_map = Map(50, 20)
    player = Player("Bob", 100)
    map_widget = MapWidget()
    width = game_map.width
    height = game_map.height

    def compose(self) -> ComposeResult:
        yield Header()
        yield self.map_widget
        yield Footer()

    def on_mount(self) -> None:
        self.update_map_display()
    
    def update_map_display(self) -> None:
        """Renders the map and updates the widget."""
        self.game_map.update_map(self.player.pos, player_tile)
        new_map_str = self.game_map.display_map()

        self.map_widget.map_data = new_map_str
    
    def action_move(self, direction: str) -> None:
        """Called when the player moves."""
        dx, dy = 0, 0
        if direction == "up":
            dy = -1
        elif direction == "down":
            dy = 1
        elif direction == "left":
            dx = -1
        elif direction == "right":
            dx = 1

        self.player.move(dx, dy)

        self.update_map_display()





if __name__ == "__main__":
    app = GameApp()
    app.run()