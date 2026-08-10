import random


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

        # 5% chance of dying while attacking
        if random.random() < 0.05:

            print(
                f"{self.name} tries to attack {monster.name}..."
            )

            print(
                f"{self.name} made a fatal mistake and died!"
            )

            self.health = 0
            return False

        # 20% chance to miss
        if random.random() < 0.20:

            print(
                f"{self.name} attacks {monster.name} but misses!"
            )

            return False

        # Successful attack
        damage = self.get_attack_damage()

        print(
            f"{self.name} attacks "
            f"{monster.name} for {damage} damage!"
        )

        monster.take_damage(damage)

        return True

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