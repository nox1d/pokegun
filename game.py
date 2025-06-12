from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static
from textual.reactive import reactive

from start_menu import StartMenu
from __init__ import Map, Player, player_tile

class MapWidget(Static):
    """A widget to display the game map."""
    
    # 2. Use a "reactive" variable. When this variable changes,
    # Textual will automatically call the `watch_map_data` method.
    map_data = reactive("")

    # 3. This "watch" method is triggered when `self.map_data` is changed.
    # Its job is to update what the widget displays.
    def watch_map_data(self, new_map_data: str) -> None:
        """Called when the map_data reactive is changed."""
        self.update(new_map_data)


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
        # self.push_screen("StartMenu")
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

        # Use our player's move logic
        self.player.move(dx, dy)

        # After moving, update the display
        self.update_map_display()





if __name__ == "__main__":
    app = GameApp()
    app.run()