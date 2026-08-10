class Player:

    def __init__(self, name):

        self.name = name

        self.health = 100
        self.stamina = 100
        self.magicka = 100

        self.character_class = None

        self.inventory = []

        self.gold = 0

        self.current_room = None

    def move(self, room):

        self.current_room = room

    def get_attack_damage(self):

        if self.character_class == "Warrior":

            return 30

        elif self.character_class == "Mage":

            return 25

        elif self.character_class == "Rogue":

            return 28

        return 20

    def attack(self, monster):

        damage = self.get_attack_damage()

        print(
            f"{self.name} attacks "
            f"{monster.name} for {damage} damage!"
        )

        monster.take_damage(damage)

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