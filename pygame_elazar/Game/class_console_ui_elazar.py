class ConsoleUI:

    ##################################################
    # Welcome Screen
    ##################################################

    def show_welcome(self):
        """
        Display the welcome screen.
        """

    def get_player_name(self):
        """
        Ask the player for their name.
        """

    ##################################################
    # Main Menu
    ##################################################

    def show_menu(self):
        """
        Display the main menu.
        """

    def get_menu_choice(self):
        """
        Ask the player to choose a menu option.
        """

    ##################################################
    # Room Display
    ##################################################

    def show_room(self, room):
        """
        Display information about the current room.
        """

    ##################################################
    # Player Movement
    ##################################################

    def get_direction(self, exits):
        """
        Ask the player which direction they want to move.
        """

    ##################################################
    # General Messages
    ##################################################

    def show_message(self, message):
        """
        Display a message to the player.
        """

    def show_error(self, message):
        """
        Display an error message.
        """

    ##################################################
    # Inventory
    ##################################################

    def show_inventory(self, player):
        """
        Display the player's inventory.
        """

    ##################################################
    # Player Statistics
    ##################################################

    def show_player_stats(self, player):
        """
        Display the player's statistics.
        """

    ##################################################
    # Combat
    ##################################################

    def show_combat_start(self, monster):
        """
        Announce the start of combat.
        """

    def show_attack(self, attacker, defender, damage):
        """
        Display the result of an attack.
        """

    def show_monster_defeated(self, monster):
        """
        Display a message when a monster is defeated.
        """

    def show_player_defeated(self):
        """
        Display the game over message.
        """

    ##################################################
    # Items
    ##################################################

    def show_items_found(self, items):
        """
        Display the items found in a room.
        """

    def confirm_pickup(self, item):
        """
        Ask whether the player wants to pick up an item.
        """

    ##################################################
    # Victory
    ##################################################

    def show_victory(self):
        """
        Display the victory message.
        """

    ##################################################
    # Exit
    ##################################################

    def confirm_exit(self):
        """
        Ask the player to confirm exiting the game.
        """
