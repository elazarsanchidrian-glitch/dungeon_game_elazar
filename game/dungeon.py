from game.room import Room
from game.item import Item
from game.monster import Monster


class Dungeon:

    def __init__(self):
        self.rooms = []
        self.current_row = 0
        self.current_col = 0

        self.create_rooms()

        # Starting room
        self.current_room = self.get_current_room()

    ##################################################
    # Create Rooms
    ##################################################

    def create_rooms(self):
        self.rooms = [
            [
                Room("Entrance", "The entrance to the dungeon. It's cold and quiet."),
                Room("Hallway", "A long stone hallway with flickering torches."),
                Room("Armory", "Old weapons are scattered across the floor.")
            ],
            [
                Room("Cave", "A damp cave echoes with strange noises."),
                Room("Crossroads", "Four paths meet here."),
                Room("Library", "Dusty books fill ancient shelves.")
            ],
            [
                Room("Crypt", "Broken tombs line the walls."),
                Room("Treasure Room", "Gold sparkles in the darkness."),
                Room("Boss Room", "A powerful enemy waits here.")
            ]
        ]

        ##################################################
        # Create Items
        ##################################################

        rusty_sword = Item(
            "Rusty Sword",
            "An old sword. Better than fighting with your fists.",
            10
        )

        leather_armor = Item(
            "Leather Armor",
            "Simple armor that offers basic protection.",
            20
        )

        potion = Item(
            "Health Potion",
            "Restores a little health.",
            25
        )

        gold = Item(
            "Pile of Gold",
            "A small pile of shiny gold coins.",
            100
        )

        ##################################################
        # Place Items
        ##################################################

        self.rooms[0][0].add_item(rusty_sword)
        self.rooms[0][2].add_item(leather_armor)
        self.rooms[1][2].add_item(potion)
        self.rooms[2][1].add_item(gold)

        ##################################################
        # Place Monsters
        ##################################################

        self.rooms[1][0].add_monster("Goblin")
        self.rooms[2][0].add_monster("Skeleton")
        self.rooms[2][2].add_monster("Dragon")

    ##################################################
    # Current Room
    ##################################################

    def get_current_room(self):
        return self.rooms[self.current_row][self.current_col]

    ##################################################
    # Movement
    ##################################################

    def move_north(self):
        if self.current_row > 0:
            self.current_row -= 1
        else:
            print("You can't go north.")

        self.current_room = self.get_current_room()

    def move_south(self):
        if self.current_row < len(self.rooms) - 1:
            self.current_row += 1
        else:
            print("You can't go south.")

        self.current_room = self.get_current_room()

    def move_east(self):
        if self.current_col < len(self.rooms[0]) - 1:
            self.current_col += 1
        else:
            print("You can't go east.")

        self.current_room = self.get_current_room()

    def move_west(self):
        if self.current_col > 0:
            self.current_col -= 1
        else:
            print("You can't go west.")

        self.current_room = self.get_current_room()

    ##################################################
    # Display
    ##################################################

    def display_current_room(self):
        self.current_room.display()