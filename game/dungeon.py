import random

from .room import Room
from .item import Item
from .monster import Monster
from .lost_traveler import LostTraveler
from .merchant import Merchant


class Dungeon:

    def __init__(self):
        self.rooms = {}

        self.current_x = 0
        self.current_y = 0

        self.exit_min_distance = 5
        self.exit_max_distance = 12
        self.exit_x, self.exit_y = self._choose_exit_location()

        self.special_room_chance = 0.01      # 1% of newly discovered rooms
        self.boss_spawn_chance = 0.10        # 10% if the rare room occurs
        self.boss_key_drop_chance = 0.05     # 5% after defeating the boss

        self.current_room = self.generate_room(0, 0, starting_room=True)

    def _choose_exit_location(self):
        """Choose a guaranteed normal exit somewhere away from the entrance."""
        while True:
            x = random.randint(-self.exit_max_distance, self.exit_max_distance)
            y = random.randint(-self.exit_max_distance, self.exit_max_distance)
            distance = abs(x) + abs(y)

            if self.exit_min_distance <= distance <= self.exit_max_distance:
                return x, y

    def generate_room(self, x, y, starting_room=False):

        if (x, y) in self.rooms:
            return self.rooms[(x, y)]

        room_types = [
            ("Dark Hallway", "A long stone hallway disappears into the darkness."),
            ("Cavern", "A damp natural cavern surrounds you."),
            ("Crypt", "Ancient tombs line the walls."),
            ("Abandoned Armory", "Broken weapons and rusty armor litter the floor."),
            ("Forgotten Library", "Dusty bookshelves disappear into the darkness."),
            ("Underground Shrine", "An ancient shrine stands silently in the darkness."),
            ("Collapsed Chamber", "Broken stone blocks cover parts of the floor."),
            ("Underground Lake", "Dark water stretches into the shadows."),
            ("Bloodstained Chamber", "The floor is stained with old, dark blood."),
            ("Ancient Prison", "Rusty cells line the walls of this forgotten prison."),
            ("Mysterious Chamber", "You cannot tell what this chamber was once used for."),
            ("Torchlit Corridor", "Old torches burn weakly along the walls.")
        ]

        if starting_room:
            name = "Dungeon Entrance"
            description = "The entrance to the dungeon. Cold air flows in from behind you."
        else:
            name, description = random.choice(room_types)

        room = Room(name, description)

        if not starting_room and (x, y) == (self.exit_x, self.exit_y):
            room.name = "Dungeon Exit"
            room.description = (
                "A massive ancient doorway stands before you. "
                "Cold air flows from beyond it. This must be the way out."
            )
            room.is_exit = True

        room.generate_atmosphere()

        if not starting_room and not room.is_exit:
            self.generate_items(room)

        if not starting_room and not room.is_exit:
            self.generate_special_boss_room(room)

        if not room.is_boss_room and not room.is_exit:
            self.generate_monsters(room)

        if not room.is_boss_room and not room.is_exit:
            self.generate_npc(room)

        self.rooms[(x, y)] = room
        return room

    def generate_special_boss_room(self, room):
        if random.random() >= self.special_room_chance:
            return

        room.name = "Forbidden Boss Chamber"
        room.description = (
            "The air is unnaturally still. Ancient symbols cover the walls, "
            "and a huge sealed chamber dominates the room."
        )
        room.is_boss_room = True

        if random.random() >= self.boss_spawn_chance:
            return

        boss = Monster(
            "Dungeon Warden",
            300,
            35,
            dialogue=[
                "Dungeon Warden: You were never meant to find this chamber.",
                "Dungeon Warden: Turn back, intruder.",
                "Dungeon Warden: The dungeon itself has chosen your grave.",
                "Dungeon Warden: Few ever reach me. Fewer survive.",
                "Dungeon Warden: YOU WILL NOT LEAVE!"
            ],
            dialogue_success_chance=5,
            attack_sounds=[
                "Dungeon Warden: RAAAAAAAH!",
                "Dungeon Warden: TRESPASSER!",
                "Dungeon Warden: DIE!",
                "Dungeon Warden: *the chamber shakes with a roar*",
                "Dungeon Warden: YOU CANNOT ESCAPE!"
            ],
            reactions=[
                "Dungeon Warden: Impressive... but futile.",
                "Dungeon Warden: You dare wound me?",
                "Dungeon Warden: *the Warden roars in fury*"
            ],
            death_sounds=[
                "Dungeon Warden: No... the key...",
                "Dungeon Warden: *the ancient guardian collapses*",
                "Dungeon Warden: You... actually defeated me..."
            ]
        )

        boss.is_dungeon_boss = True
        room.add_monster(boss)

    def generate_items(self, room):
        if random.random() > 0.45:
            return

        item_types = [
            Item("Rusty Sword", "An old sword. Better than fighting with your fists.", 10),
            Item("Leather Armor", "Simple armor that offers basic protection.", 20),
            Item("Health Potion", "Restores a little health.", 25),
            Item("Pile of Gold", "A small pile of shiny gold coins.", 100),
            Item("Ancient Coin", "An old coin from a forgotten civilization.", 50),
            Item("Silver Ring", "A small silver ring. It may be worth something.", 75)
        ]

        number_of_items = random.choices([1, 2], weights=[85, 15])[0]
        selected_items = random.sample(item_types, min(number_of_items, len(item_types)))

        for item in selected_items:
            room.add_item(item)

    def generate_monsters(self, room):
        if room.name == "Dungeon Entrance" or random.random() < 0.55:
            return

        monster_types = [
            Monster("Goblin", 50, 10, dialogue=["Goblin: Hehehe... shiny!"], dialogue_success_chance=65),
            Monster("Skeleton", 75, 15, dialogue=["Skeleton: ...You disturb the dead."], dialogue_success_chance=40),
            Monster("Bandit", 65, 18, dialogue=["Bandit: Drop your weapons!"], dialogue_success_chance=55),
            Monster("Troll", 150, 22, dialogue=["Troll: Troll smell fear."], dialogue_success_chance=30),
            Monster("Orc", 120, 20, dialogue=["Orc: Prove your strength!"], dialogue_success_chance=40),
            Monster("Demon", 175, 28, dialogue=["Demon: Your soul smells delicious."], dialogue_success_chance=20),
            Monster("Spirit", 90, 17, dialogue=["Spirit: Leave this place..."], dialogue_success_chance=35),
            Monster("Vampire", 130, 24, dialogue=["Vampire: Such warm blood..."], dialogue_success_chance=25)
        ]

        weights = [25, 20, 20, 12, 10, 5, 5, 3]
        monster = random.choices(monster_types, weights=weights, k=1)[0]
        room.add_monster(monster)

    def generate_npc(self, room):
        if random.random() > 0.10:
            return

        npc_types = [LostTraveler, Merchant]
        npc_class = random.choice(npc_types)
        room.add_npc(npc_class())

    def move(self, direction):
        x, y = self.current_x, self.current_y

        if direction == "north":
            y -= 1
        elif direction == "south":
            y += 1
        elif direction == "east":
            x += 1
        elif direction == "west":
            x -= 1
        else:
            return False

        self.current_room = self.generate_room(x, y)
        self.current_x, self.current_y = x, y
        return True

    def get_current_room(self):
        return self.current_room

    def get_position(self):
        return self.current_x, self.current_y