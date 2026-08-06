class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.monsters = []

    ##################################################
    # Items
    ##################################################

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    ##################################################
    # Monsters
    ##################################################

    def add_monster(self, monster):
        self.monsters.append(monster)

    def remove_monster(self, monster):
        if monster in self.monsters:
            self.monsters.remove(monster)

    ##################################################
    # Display
    ##################################################

    def display(self):
        print(f"\n{'=' * 40}")
        print(f"Room: {self.name}")
        print(f"{'=' * 40}")

        if self.description:
            print(self.description)

        if self.items:
            print("\nItems:")
            for item in self.items:
                print(f" - {item}")

        if self.monsters:
            print("\nMonsters:")
            for monster in self.monsters:
                print(f" - {monster}")

        if not self.items and not self.monsters:
            print("\nThe room is empty.")