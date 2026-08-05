from room import Room


class Dungeon:
    """
    Represents the entire dungeon.

    Responsible for creating rooms, connecting them together,
    and keeping track of the dungeon layout.
    """

    def __init__(self):
        """
        Create a new dungeon.
        """
        self.rooms = []

        self.create_rooms()
        # self.connect_rooms()
        # self.add_monsters()
        # self.add_items()

    def create_rooms(self, num_rooms):
        """
        Create all the rooms in the dungeon.
        """
        rooms = [
            [Room("1") , Room("2"), Room("3")],
            [Room("4"), Room("5"), Room("6")],
            [Room("7"), Room("8"), Room("9")],
        ]

    def connect_rooms(self):
        """
        Connect the rooms together by setting
        their north/south/east/west exits.
        """

    def place_items(self):
        """
        Place items into appropriate rooms.
        """

    def place_monsters(self):
        """
        Place monsters into appropriate rooms.
        """

    def choose_start_room(self):
        """
        Select which room is the player's starting room.
        """

    def choose_exit_room(self):
        """
        Select which room is the exit from the dungeon.
        """

    def get_start_room(self):
        """
        Return the starting room.
        """

    def get_exit_room(self):
        """
        Return the exit room.
        """

    def get_room(self, room_name):
        """
        Return a room by its name.
        """

    def display_map(self):
        """
        Display a simple map of the dungeon.
        (Optional extension)
        """

    def add_monsters(self):
        pass

    def add_items(self):
        pass