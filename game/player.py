import random


class Player:

    def __init__(self, name):

        self.name = name
        self.gender = None

        self.health = 100
        self.max_health = 100

        self.stamina = 100
        self.magicka = 100

        self.race = None
        self.character_class = None
        self.passive = None

        self.inventory = []

        self.gold = 0

        self.current_room = None

    # Everything below these stays exactly as it was.
    def move(self, room):
        self.current_room = room

    def get_attack_damage(self):

        if self.character_class == "Warrior":
            damage = 30

        elif self.character_class == "Mage":
            damage = 25

        elif self.character_class == "Rogue":
            damage = 28

        else:
            damage = 20

        # Orc and Elf racial attack bonuses
        if self.passive == "Brutal":
            damage = int(damage * 1.15)

        elif self.passive == "Arcane Affinity":
            damage = int(damage * 1.10)

        return damage

    def attack(self, monster):

        # Halfling Lucky passive
        if self.passive == "Lucky":

            if random.random() < 0.15:

                print(
                    f"{self.name}'s Lucky passive activates!"
                )

                print(
                    f"{self.name} avoids danger completely!"
                )

                return True

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
                f"{self.name} attacks "
                f"{monster.name} but misses!"
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

        # Dwarf Tough passive
        if self.passive == "Tough":

            reduced_damage = int(damage * 0.90)

            print(
                f"{self.name}'s Tough passive reduces "
                f"the damage from {damage} to "
                f"{reduced_damage}!"
            )

            damage = reduced_damage

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