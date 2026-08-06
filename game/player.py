class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.stamina = 100
        self.magicka = 100
        self.inventory = []
        self.gold = 0
        self.current_room = None

    def move(self, room):
        self.current_room = room

    def attack(self, monster):
        print(f"{self.name} attacks {monster.name}!")

    def take_damage(self, damage):
        self.health -= damage

        if self.health < 0:
            self.health = 0

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item}")