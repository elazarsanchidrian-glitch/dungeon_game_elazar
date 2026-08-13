import random

from game.player import Player
from game.dungeon import Dungeon
from game.ui import ConsoleUI
from game.character import CharacterCreation
from game.save_system import SaveSystem


class Game:

    def __init__(self):

        self.ui = ConsoleUI()
        self.dungeon = Dungeon()

        self.ui.show_welcome()

        # -------------------------
        # CHARACTER CREATION
        # -------------------------

        player_name = self.ui.get_player_name()

        character = CharacterCreation(player_name)

        character.choose_gender()
        character.choose_race()
        character.choose_class()

        character.show_character()

        # -------------------------
        # CREATE PLAYER
        # -------------------------

        self.player = Player(player_name)

        self.player.gender = character.gender
        self.player.race = character.race
        self.player.character_class = character.character_class
        self.player.passive = character.passive

        self.player.health = character.health
        self.player.max_health = character.health

        self.player.stamina = character.stamina
        self.player.magicka = character.magicka

        # -------------------------
        # CLASS STARTING INVENTORY
        # -------------------------

        self.player.setup_starting_inventory()

        self.player.health = character.health

        # -------------------------
        # STARTING ROOM
        # -------------------------

        self.player.current_room = self.dungeon.current_room

    # -------------------------
    # MONSTER ATTACK
    # -------------------------

    def monster_attack(self, monster):

        damage = monster.attack()

        self.player.take_damage(damage)

        self.ui.show_message(
            f"{monster.name} hits you for {damage} damage!"
        )

        self.ui.show_message(
            f"Your health: "
            f"{self.player.health}/{self.player.max_health}"
        )

        if self.player.health <= 0:

            self.ui.show_player_defeated()

            return False

        return True

    # -------------------------
    # DODGE
    # -------------------------

    def dodge(self, monster):

        # 50% chance to successfully dodge
        if random.random() < 0.50:

            self.ui.show_message(
                f"You dodge {monster.name}'s attack!"
            )

            return True

        self.ui.show_message(
            f"You try to dodge, but {monster.name} catches you!"
        )

        return self.monster_attack(monster)

    # -------------------------
    # ESCAPE
    # -------------------------

    def escape(self, monster):

        # 50% chance to escape
        if random.random() < 0.50:

            self.ui.show_message(
                f"You successfully escape from {monster.name}!"
            )

            # The monster loses track of you
            self.player.current_room.remove_monster(monster)

            return True

        self.ui.show_message(
            f"You try to escape, but {monster.name} catches you!"
        )

        return self.monster_attack(monster)

    # -------------------------
    # MOVEMENT
    # -------------------------

    def move_player(self, direction):

        old_room = self.player.current_room

        # Move through the infinite dungeon
        moved = self.dungeon.move(direction)

        if not moved:

            self.ui.show_error("Invalid direction.")

            return

        # Update player location
        self.player.current_room = self.dungeon.current_room

        # -------------------------
        # NEW ROOM
        # -------------------------

        if self.player.current_room is not old_room:

            x, y = self.dungeon.get_position()

            self.ui.show_message(
                f"\nYou travel {direction}..."
            )

            self.ui.show_message(
                f"You enter: {self.player.current_room.name}"
            )

            self.ui.show_message(
                f"Dungeon coordinates: ({x}, {y})"
            )

            # -------------------------
            # RANDOM ENCOUNTER
            # -------------------------

            room = self.player.current_room

            if room.monsters:

                for monster in room.monsters:

                    self.ui.show_combat_start(monster)

                    monster.speak()

                    while monster.is_alive() and monster in room.monsters:

                        self.ui.show_combat_options()

                        choice = self.ui.get_combat_choice()

                        # -------------------------
                        # ATTACK
                        # -------------------------

                        if choice in ("1", "attack"):

                            if not self.attack():

                                return

                        # -------------------------
                        # DODGE
                        # -------------------------

                        elif choice in ("2", "dodge"):

                            if not self.dodge(monster):

                                return

                        # -------------------------
                        # ESCAPE
                        # -------------------------

                        elif choice in ("3", "escape", "run"):

                            if not self.escape(monster):

                                return

                            # Successful escape
                            if monster not in room.monsters:

                                break

                        else:

                            self.ui.show_error(
                                "Choose Attack, Dodge, or Escape."
                            )

    # -------------------------
    # LOOK / EXPLORE
    # -------------------------

    def explore(self):

        room = self.player.current_room

        x, y = self.dungeon.get_position()

        print(
            f"\nDungeon coordinates: ({x}, {y})"
        )

        room.explore()

    # -------------------------
    # TAKE ITEM
    # -------------------------

    def take_item(self, item_name):

        room = self.player.current_room

        found_item = None

        for item in room.items:

            if item.name.lower() == item_name.lower():

                found_item = item

                break

        if found_item:

            room.remove_item(found_item)

            self.player.add_item(found_item)

            self.ui.show_message(
                f"You picked up {found_item.name}."
            )

        else:

            self.ui.show_error(
                "That item isn't here."
            )

    # -------------------------
    # ATTACK
    # -------------------------

    def attack(self):

        room = self.player.current_room

        if not room.monsters:

            self.ui.show_error(
                "There are no monsters here."
            )

            return True

        monster = room.monsters[0]

        # Player attacks
        attack_successful = self.player.attack(monster)

        # Player died
        if self.player.health <= 0:

            self.ui.show_player_defeated()

            return False

        # Player missed
        if not attack_successful:

            if not self.monster_attack(monster):

                return False

            return True

        # Monster died
        if not monster.is_alive():

            room.remove_monster(monster)

            self.ui.show_monster_defeated(
                monster
            )

            # -------------------------
            # ENEMY LOOT
            # -------------------------

            loot = monster.generate_loot()

            if loot:

                self.ui.show_message(
                    f"\n{monster.name} dropped:"
                )

                for item in loot:

                    room.add_item(item)

                    self.ui.show_message(
                        f" - {item.name}"
                    )

                self.ui.show_message(
                    "\nThe loot is lying on the ground."
                )

            else:

                self.ui.show_message(
                    f"{monster.name} dropped nothing."
                )

            return True

        # Monster survived
        if not self.monster_attack(monster):

            return False

        return True

    # -------------------------
    # START GAME
    # -------------------------

    def start(self):

        self.ui.show_message(
            f"\nWelcome to the dungeon, "
            f"{self.player.name}!"
        )

        self.ui.show_message(
            "\nYou stand at the entrance of an "
            "endless dungeon."
        )

        self.ui.show_message(
            "Type 'look' to examine your surroundings."
        )

        while True:

            # -------------------------
            # COMMANDS
            # -------------------------

            self.ui.show_commands()

            command = self.ui.get_command()

            # -------------------------
            # MOVEMENT
            # -------------------------

            if command in (
                "north",
                "south",
                "east",
                "west"
            ):

                self.move_player(command)

                if self.player.health <= 0:

                    break

            # -------------------------
            # LOOK
            # -------------------------

            elif command in (
                "look",
                "search",
                "explore",
                "observe"
            ):

                self.explore()

            # -------------------------
            # TAKE ITEM
            # -------------------------

            elif command.startswith("take "):

                item_name = command[5:].strip()

                self.take_item(item_name)

            # -------------------------
            # ATTACK
            # -------------------------

            elif command == "attack":

                if not self.attack():

                    break

            # -------------------------
            # INVENTORY
            # -------------------------

            elif command == "inventory":

                self.ui.show_inventory(
                    self.player
                )

            # -------------------------
            # STATS
            # -------------------------

            elif command == "stats":

                self.ui.show_player_stats(
                    self.player
                )

            # -------------------------
            # QUIT
            # -------------------------

            elif command == "save":

                SaveSystem.save(self)

            elif command == "quit":

                if self.ui.confirm_exit():

                    break

            # -------------------------
            # UNKNOWN COMMAND
            # -------------------------

            else:

                self.ui.show_error(
                    "Unknown command."
                )


if __name__ == "__main__":

    Game().start()