from game.room import Room
from game.item import Item
from game.monster import Monster


class Dungeon:

    def __init__(self):
        self.rooms = []
        self.current_row = 0
        self.current_col = 0

        self.create_rooms()

        self.current_room = self.get_current_room()

    def create_rooms(self):
        self.rooms = [
            [
                Room(
                    "Entrance",
                    "The entrance to the dungeon. It's cold and quiet."
                ),

                Room(
                    "Hallway",
                    "A long stone hallway with flickering torches."
                ),

                Room(
                    "Armory",
                    "Old weapons are scattered across the floor."
                )
            ],

            [
                Room(
                    "Cave",
                    "A damp cave echoes with strange noises."
                ),

                Room(
                    "Crossroads",
                    "Four paths meet here."
                ),

                Room(
                    "Library",
                    "Dusty books fill ancient shelves."
                )
            ],

            [
                Room(
                    "Crypt",
                    "Broken tombs line the walls."
                ),

                Room(
                    "Treasure Room",
                    "Gold sparkles in the darkness."
                ),

                Room(
                    "Boss Room",
                    "A powerful enemy waits here."
                )
            ]
        ]

        # -------------------------
        # ITEMS
        # -------------------------

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

        # Place items
        self.rooms[0][0].add_item(rusty_sword)
        self.rooms[0][2].add_item(leather_armor)
        self.rooms[1][2].add_item(potion)
        self.rooms[2][1].add_item(gold)

        # -------------------------
        # MONSTERS
        # -------------------------

        goblin = Monster(
            "Goblin",
            50,
            10,
            dialogue=[
                "Goblin: Hehehe... shiny!",
                "Goblin: You got gold?",
                "Goblin: GOBLIN HUNGRY!",
                "Goblin: Stupid human!",
                "Goblin: Get out of my cave!"
            ],
            attack_sounds=[
                "Goblin: YAAAA!",
                "Goblin: STAB!",
                "Goblin: GRAAA!",
                "Goblin: DIE!",
                "Goblin: *high-pitched screech*"
            ]
        )

        skeleton = Monster(
            "Skeleton",
            75,
            15,
            dialogue=[
                "Skeleton: ...You disturb the dead.",
                "Skeleton: Your bones will join ours.",
                "Skeleton: *rattles ominously*",
                "Skeleton: There is no escape from death.",
                "Skeleton: We have waited for you..."
            ],
            attack_sounds=[
                "Skeleton: *rattling scream*",
                "Skeleton: DIE, MORTAL!",
                "Skeleton: *CLACK CLACK CLACK*",
                "Skeleton: HAAAA!",
                "Skeleton: *bone-rattling roar*"
            ]
        )

        dragon = Monster(
            "Dragon",
            200,
            25,
            dialogue=[
                "Dragon: You dare enter my domain?",
                "Dragon: FLEE, LITTLE MORTAL!",
                "Dragon: Your bones will feed the flames.",
                "Dragon: I have devoured armies greater than you.",
                "Dragon: You will burn."
            ],
            attack_sounds=[
                "Dragon: RAAAAAAAGH!",
                "Dragon: *DEEP ROAR*",
                "Dragon: BURN!",
                "Dragon: *flames roar*",
                "Dragon: DIE!"
            ]
        )

        # -------------------------
        # BANDIT
        # -------------------------

        bandit = Monster(
            "Bandit",
            65,
            18,
            dialogue=[
                "Bandit: Drop your weapons and hand over the gold.",
                "Bandit: Wrong place, friend.",
                "Bandit: This road belongs to us.",
                "Bandit: Your money or your life!",
                "Bandit: I've killed better fighters than you."
            ],
            attack_sounds=[
                "Bandit: HYAA!",
                "Bandit: Take this!",
                "Bandit: GOTCHA!",
                "Bandit: *draws blade*",
                "Bandit: DIE!"
            ]
        )

        # -------------------------
        # TROLL
        # -------------------------

        troll = Monster(
            "Troll",
            150,
            22,
            dialogue=[
                "Troll: Little thing... why you enter troll cave?",
                "Troll: Troll smell fear.",
                "Troll: YOU LOOK LIKE DINNER!",
                "Troll: Leave cave!",
                "Troll: Troll crush you!"
            ],
            attack_sounds=[
                "Troll: RAAAAAAARGH!",
                "Troll: CRUSH!",
                "Troll: SMASH!",
                "Troll: *thunders forward*",
                "Troll: DIE, LITTLE THING!"
            ]
        )

        # -------------------------
        # ORC
        # -------------------------

        orc = Monster(
            "Orc",
            120,
            20,
            dialogue=[
                "Orc: You have entered the territory of the Orcs.",
                "Orc: Prove your strength!",
                "Orc: Weakness will be your death.",
                "Orc: I will grind your bones beneath my axe.",
                "Orc: COME! FIGHT!"
            ],
            attack_sounds=[
                "Orc: WAAAAAGH!",
                "Orc: FOR GLORY!",
                "Orc: RAAAAH!",
                "Orc: *war cry*",
                "Orc: DIE!"
            ]
        )

        # -------------------------
        # DEMON
        # -------------------------

        demon = Monster(
            "Demon",
            175,
            28,
            dialogue=[
                "Demon: Your soul smells delicious.",
                "Demon: You should not have crossed this threshold.",
                "Demon: The darkness welcomes you.",
                "Demon: I have waited centuries for a soul like yours.",
                "Demon: SCREAM, MORTAL!"
            ],
            attack_sounds=[
                "Demon: RAAAAAAAH!",
                "Demon: BURN IN HELL!",
                "Demon: *infernal roar*",
                "Demon: YOUR SOUL IS MINE!",
                "Demon: DIE, MORTAL!"
            ]
        )

        # -------------------------
        # SPIRIT
        # -------------------------

        spirit = Monster(
            "Spirit",
            90,
            17,
            dialogue=[
                "Spirit: Leave this place...",
                "Spirit: Why have you awakened me?",
                "Spirit: You cannot escape death.",
                "Spirit: *whispers from the darkness*",
                "Spirit: Join us..."
            ],
            attack_sounds=[
                "Spirit: *ghostly scream*",
                "Spirit: AAAAAAAAH!",
                "Spirit: *whispers* DIE...",
                "Spirit: *unnatural shriek*",
                "Spirit: COME WITH US!"
            ]
        )

        # -------------------------
        # VAMPIRE
        # -------------------------

        vampire = Monster(
            "Vampire",
            130,
            24,
            dialogue=[
                "Vampire: Such warm blood...",
                "Vampire: You have no idea what hunts you.",
                "Vampire: I can hear your heart beating.",
                "Vampire: How fortunate. Dinner has arrived.",
                "Vampire: Your blood will sustain me."
            ],
            attack_sounds=[
                "Vampire: *hisses*",
                "Vampire: DIE!",
                "Vampire: *vicious snarl*",
                "Vampire: YOUR BLOOD!",
                "Vampire: *fangs snap*"
            ]
        )

        # -------------------------
        # PLACE MONSTERS
        # -------------------------

        self.rooms[0][1].add_monster(bandit)
        self.rooms[0][2].add_monster(goblin)

        self.rooms[1][0].add_monster(troll)
        self.rooms[1][1].add_monster(orc)
        self.rooms[1][2].add_monster(spirit)

        self.rooms[2][0].add_monster(skeleton)
        self.rooms[2][1].add_monster(vampire)
        self.rooms[2][2].add_monster(demon)
    # -------------------------
    # MOVEMENT
    # -------------------------

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

    def display_current_room(self):
        self.current_room.display()