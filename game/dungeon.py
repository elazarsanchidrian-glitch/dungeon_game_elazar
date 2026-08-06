from game.room import Room


class Dungeon:

    def __init__(self):
        self.rooms = []
        self.current_row = 0
        self.current_col = 0
        self.create_rooms()

    def create_rooms(self):
        self.rooms = [
            [Room("Room 1"), Room("Room 2"), Room("Room 3")],
            [Room("Room 4"), Room("Room 5"), Room("Room 6")],
            [Room("Room 7"), Room("Room 8"), Room("Room 9")]
        ]

    def get_current_room(self):
        return self.rooms[self.current_row][self.current_col]

    def move_north(self):
        if self.current_row > 0:
            self.current_row -= 1
        else:
            print("You can't go north.")

    def move_south(self):
        if self.current_row < 2:
            self.current_row += 1
        else:
            print("You can't go south.")

    def move_east(self):
        if self.current_col < 2:
            self.current_col += 1
        else:
            print("You can't go east.")

    def move_west(self):
        if self.current_col > 0:
            self.current_col -= 1
        else:
            print("You can't go west.")

    def display_current_room(self):
        self.get_current_room().display()