class Room:

    def __init__(self, name):
        self.name = name
        self.description = ""
        self.items = []
        self.monsters = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def add_monster(self, monster):
        self.monsters.append(monster)

    def remove_monster(self, monster):
        if monster in self.monsters:
            self.monsters.remove(monster)

    def display(self):
        print(f"\nRoom: {self.name}")

        if self.description:
            print(self.description)

        if self.items:
            print("\nItems:")
            for item in self.items:
                print(f"- {item}")

        if self.monsters:
            print("\nMonsters:")
            for monster in self.monsters:
                print(f"- {monster}")