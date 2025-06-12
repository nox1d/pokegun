class Player:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.attack = 10

        self.pos = [0, 0]
    
    def move(self, x: int, y: int):
        self.pos[0] += x
        self.pos[1] += y
    
    def calculate_movement(self, movement: str, width: int, height: int):
        self.movement = movement

        match self.movement:
            case 'w':
                self.move(0, -1) if not self.pos[1] - 1 < 0 else print('you are at the edge of the map.')
            case 'a':
                self.move(-1, 0) if not self.pos[0] - 1 < 0 else print('you are at the edge of the map.')
            case 's':
                self.move(0, 1) if not self.pos[1] + 1 > height else print('you are at the edge of the map.')
            case 'd':
                self.move(1, 0) if not self.pos[1] + 1 > width else print('you are at the edge of the map.')
            case _:
                print('invalid move')
