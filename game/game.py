from game.player import Player
from game.dungeon import Dungeon
from game.ui import ConsoleUI
from game.character import CharacterCreation


class Game:

    def __init__(self):

        self.ui = ConsoleUI()
        self.dungeon = Dungeon()

        self.ui.show_welcome()

        # Get player name
        player_name = self.ui.get_player_name()

        # Create character
        character = CharacterCreation(player_name)

        character.choose_class()
        character.show_character()

        # Create player
        self.player = Player(player_name)

        self.player.character_class = character.character_class
        self.player.health = character.health
        self.player.stamina = character.stamina
        self.player.magicka = character.magicka

        # Start player in dungeon
        self.player.current_room = self.dungeon.current_room

    def move_player(self, direction):

        old_room = self.player.current_room

        if direction == "north":
            self.dungeon.move_north()

        elif direction == "south":
            self.dungeon.move_south()

        elif direction == "east":
            self.dungeon.move_east()

        elif direction == "west":
            self.dungeon.move_west()

        self.player.current_room = self.dungeon.current_room

        # Announce monsters when entering a new room
        if self.player.current_room is not old_room:

            if self.player.current_room.monsters:

                for monster in self.player.current_room.monsters:
                    self.ui.show_combat_start(monster)
                    monster.speak()

    def start(self):

        self.ui.show_message(
            f"Welcome to the dungeon, {self.player.name}!"
        )

        while True:

            # Display room
            self.player.current_room.display()

            # Commands
            self.ui.show_commands()

            command = input("> ").lower().strip()

            # -------------------------
            # MOVEMENT
            # -------------------------

            if command in ("north", "south", "east", "west"):

                self.move_player(command)

            # -------------------------
            # TAKE ITEM
            # -------------------------

            elif command.startswith("take "):

                item_name = command[5:].strip()

                room = self.player.current_room

                found_item = None

                for item in room.items:

                    if item.name.lower() == item_name:
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

            elif command == "attack":

                room = self.player.current_room

                if room.monsters:

                    monster = room.monsters[0]

                    damage = self.player.get_attack_damage()

                    self.ui.show_attack(
                        self.player,
                        monster,
                        damage
                    )

                    monster.take_damage(damage)

                    # Monster died
                    if not monster.is_alive():

                        room.remove_monster(monster)

                        self.ui.show_monster_defeated(
                            monster
                        )

                    # Monster survived
                    else:

                        monster.attack()

                        self.player.take_damage(10)

                        self.ui.show_message(
                            f"{monster.name} hits you for 10 damage."
                        )

                        if self.player.health <= 0:

                            self.ui.show_player_defeated()

                            break

                else:

                    self.ui.show_error(
                        "There are no monsters here."
                    )

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