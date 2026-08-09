from game.player import Player
from game.dungeon import Dungeon
from game.ui import ConsoleUI
from game.character import CharacterCreation


class Game:

    def __init__(self):
        self.ui = ConsoleUI()
        self.dungeon = Dungeon()

        self.ui.show_welcome()

        # Get the player's name
        player_name = self.ui.get_player_name()

        # Create the character
        character = CharacterCreation(player_name)
        character.choose_class()
        character.show_character()

        # Create the player
        self.player = Player(player_name)

        self.player.character_class = character.character_class
        self.player.health = character.health
        self.player.stamina = character.stamina
        self.player.magicka = character.magicka

        # Save the chosen class
        self.player.character_class = character.character_class

        # Start the player in the dungeon's starting room
        self.player.current_room = self.dungeon.current_room

    def start(self):
        self.ui.show_message(f"Welcome, {self.player.name}!")

        while True:

            # Display the current room
            self.player.current_room.display()

            print("\nCommands:")
            print("north")
            print("south")
            print("east")
            print("west")
            print("take <item>")
            print("attack")
            print("inventory")
            print("stats")
            print("quit")

            command = input("> ").lower().strip()

            if command == "north":
                self.dungeon.move_north()
                self.player.current_room = self.dungeon.current_room

            elif command == "south":
                self.dungeon.move_south()
                self.player.current_room = self.dungeon.current_room

            elif command == "east":
                self.dungeon.move_east()
                self.player.current_room = self.dungeon.current_room

            elif command == "west":
                self.dungeon.move_west()
                self.player.current_room = self.dungeon.current_room

            elif command.startswith("take "):
                item_name = command[5:]

                room = self.player.current_room

                if item_name in room.items:
                    room.remove_item(item_name)
                    self.player.add_item(item_name)
                    self.ui.show_message(f"You picked up {item_name}.")
                else:
                    self.ui.show_error("That item isn't here.")

            elif command == "attack":
                room = self.player.current_room

                if room.monsters:
                    monster = room.monsters[0]

                    self.ui.show_message(f"You attack {monster}!")

                    room.remove_monster(monster)

                    self.ui.show_message(f"{monster} was defeated!")
                else:
                    self.ui.show_error("There are no monsters here.")

            elif command == "inventory":
                self.ui.show_inventory(self.player)

            elif command == "stats":
                self.ui.show_player_stats(self.player)

            elif command == "quit":
                if self.ui.confirm_exit():
                    break

            else:
                self.ui.show_error("Unknown command.")