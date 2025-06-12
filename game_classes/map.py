from random import randint
from copy import deepcopy
from .tile import Tile, plains, forests, mountains, water

class Map:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.init_map_data: list[list[str]]
        self.map_data: list[list[str]]

        self.generate_map()


    def generate_map(self) -> None:
        self.init_map_data = [[plains.symbol for _ in range(self.width)] for _ in range(self.height)]
        self.generate_patch(water, 8, 2, 10)
        self.generate_patch(forests, 5, 4, 5)
        self.generate_patch(mountains, 3, 1, 4)
        self.map_data = deepcopy(self.init_map_data)
    
    def update_map(self, pos: list[int], marker: Tile) -> None:
        x, y = pos
        self.map_data = deepcopy(self.init_map_data)
        self.map_data[y][x] = marker.symbol
    
    def generate_patch(self, tile: Tile, num_patches: int, min_size: int, max_size: int, irregular: bool = True) -> None:
        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            start_x = randint(1, self.width - width - 1)
            start_y = randint(1, self.height - height - 1)

            if irregular:
                irregular_start_x = randint(3, self.width - max_size)

            for i in range(height):
                if irregular:
                    width = randint(int(0.7 * max_size), max_size)
                    start_x = irregular_start_x - randint(1,2) # type: ignore
                for j in range(width):
                    self.init_map_data[start_y + i][start_x + j] = tile.symbol

        
    def display_map(self):
        frame = f'# {"# " * self.width}#'

        # print(frame)
        # for row in self.map_data:
        #     print(f'# {" ".join(row)} #')
        # print(frame)

        map_rows = [f'# {" ".join(row)} #' for row in self.map_data]

        middle_section_string = "\n".join(map_rows)
        return f'{frame}\n{middle_section_string}\n{frame}'
