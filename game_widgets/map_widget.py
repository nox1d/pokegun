from textual.widgets import Static
from textual.reactive import reactive

class MapWidget(Static):
    
    map_data = reactive("")

    def watch_map_data(self, new_map_data: str) -> None:
        self.update(new_map_data)