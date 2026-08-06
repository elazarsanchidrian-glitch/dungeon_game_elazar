from game.player import Player
from game.dungeon import Dungeon
from game.ui import ConsoleUI


class Game:

    def __init__(self):
        self.ui = ConsoleUI()
        self.dungeon = Dungeon()

        self.ui.show_welcome()

        player_name = self.ui.get_player_name()
        self.player = Player(player_name)

    def start(self):
        self.ui.show_message(f"Welcome, {self.player.name}!")

        while True:

            self.dungeon.display_current_room()

            print("\nCommands:")
            print("north")
            print("south")
            print("east")
            print("west")
            print("inventory")
            print("stats")
            print("quit")

            command = input("> ").lower()

            if command == "north":
                self.dungeon.move_north()

            elif command == "south":
                self.dungeon.move_south()

            elif command == "east":
                self.dungeon.move_east()

            elif command == "west":
                self.dungeon.move_west()

            elif command == "inventory":
                self.ui.show_inventory(self.player)

            elif command == "stats":
                self.ui.show_player_stats(self.player)

            elif command == "quit":
                if self.ui.confirm_exit():
                    break

            else:
                self.ui.show_error("Unknown command.")