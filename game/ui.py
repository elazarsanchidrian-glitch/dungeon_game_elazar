class ConsoleUI:

    ##################################################
    # Welcome Screen
    ##################################################

    def show_welcome(self):
        print("=" * 40)
        print(" Welcome to the Dungeon Game!")
        print("=" * 40)

    def get_player_name(self):
        return input("Enter your name: ")

    ##################################################
    # Main Menu
    ##################################################

    def show_menu(self):
        print("\nMain Menu")
        print("1. Start Game")
        print("2. Show Stats")
        print("3. Inventory")
        print("4. Quit")

    def get_menu_choice(self):
        return input("Choose an option: ")

    ##################################################
    # Room Display
    ##################################################

    def show_room(self, room):
        room.display()

    ##################################################
    # Commands
    ##################################################

    def show_commands(self):
        print("\nCommands:")
        print("north")
        print("south")
        print("east")
        print("west")
        print("inventory")
        print("stats")
        print("quit")

    def get_command(self):
        return input("> ").lower()

    ##################################################
    # Player Movement
    ##################################################

    def get_direction(self, exits):
        print(f"Available directions: {', '.join(exits)}")
        return input("Which direction? ").lower()

    ##################################################
    # General Messages
    ##################################################

    def show_message(self, message):
        print(message)

    def show_error(self, message):
        print(f"\n[ERROR] {message}")

    ##################################################
    # Inventory
    ##################################################

    def show_inventory(self, player):
        print("\nInventory:")

        if not player.inventory:
            print("Empty")
        else:
            for item in player.inventory:
                print(f"- {item}")

    ##################################################
    # Player Statistics
    ##################################################

    def show_player_stats(self, player):
        print("\nPlayer Stats")
        print(f"Name: {player.name}")
        print(f"Health: {player.health}")
        print(f"Stamina: {player.stamina}")
        print(f"Magicka: {player.magicka}")
        print(f"Gold: {player.gold}")

    ##################################################
    # Combat
    ##################################################

    def show_combat_start(self, monster):
        print(f"\nA {monster.name} appears!")

    def show_attack(self, attacker, defender, damage):
        print(f"{attacker.name} attacks {defender.name} for {damage} damage!")

    def show_monster_defeated(self, monster):
        print(f"{monster.name} has been defeated!")

    def show_player_defeated(self):
        print("Game Over!")

    ##################################################
    # Items
    ##################################################

    def show_items_found(self, items):
        if items:
            print("\nItems found:")
            for item in items:
                print(f"- {item}")
        else:
            print("No items found.")

    def confirm_pickup(self, item):
        choice = input(f"Pick up {item}? (y/n): ")
        return choice.lower() == "y"

    ##################################################
    # Victory
    ##################################################

    def show_victory(self):
        print("Congratulations! You escaped the dungeon!")

    ##################################################
    # Exit
    ##################################################

    def confirm_exit(self):
        choice = input("Are you sure you want to quit? (y/n): ")
        return choice.lower() == "y"