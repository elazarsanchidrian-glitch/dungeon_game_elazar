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

    # -------------------------
    # CLASS STARTING INVENTORY
    # -------------------------

    def setup_starting_inventory(self):

        from game.item import Item

        # Clear inventory first
        self.inventory = []

        # -------------------------
        # WARRIOR
        # -------------------------

        if self.character_class == "Warrior":

            self.add_item(
                Item(
                    "Iron Sword",
                    "A sturdy sword made for close combat.",
                    50
                )
            )

            self.add_item(
                Item(
                    "Wooden Shield",
                    "A simple shield that offers basic protection.",
                    30
                )
            )

            self.add_item(
                Item(
                    "Chainmail",
                    "Basic metal armor offering decent protection.",
                    75
                )
            )

            self.add_item(
                Item(
                    "Health Potion",
                    "Restores some health.",
                    25
                )
            )

            self.add_item(
                Item(
                    "Health Potion",
                    "Restores some health.",
                    25
                )
            )

        # -------------------------
        # MAGE
        # -------------------------

        elif self.character_class == "Mage":

            self.add_item(
                Item(
                    "Apprentice Staff",
                    "A wooden staff used to channel magical energy.",
                    50
                )
            )

            self.add_item(
                Item(
                    "Mage Robes",
                    "Light robes designed for spellcasters.",
                    60
                )
            )

            self.add_item(
                Item(
                    "Spellbook",
                    "A book containing the mage's magical knowledge.",
                    100
                )
            )

            self.add_item(
                Item(
                    "Mana Potion",
                    "Restores some magicka.",
                    30
                )
            )

            self.add_item(
                Item(
                    "Mana Potion",
                    "Restores some magicka.",
                    30
                )
            )

        # -------------------------
        # ROGUE
        # -------------------------

        elif self.character_class == "Rogue":

            self.add_item(
                Item(
                    "Iron Dagger",
                    "A quick and lightweight dagger.",
                    35
                )
            )

            self.add_item(
                Item(
                    "Throwing Knife",
                    "A small knife designed to be thrown.",
                    25
                )
            )

            self.add_item(
                Item(
                    "Leather Armor",
                    "Light armor that allows freedom of movement.",
                    40
                )
            )

            self.add_item(
                Item(
                    "Lockpicks",
                    "A set of tools used to open locked containers.",
                    20
                )
            )

            self.add_item(
                Item(
                    "Health Potion",
                    "Restores some health.",
                    25
                )
            )

        # -------------------------
        # DEFAULT
        # -------------------------

        else:

            self.add_item(
                Item(
                    "Simple Dagger",
                    "A basic weapon.",
                    15
                )
            )

            self.add_item(
                Item(
                    "Health Potion",
                    "Restores some health.",
                    25
                )
            )

    # -------------------------
    # MOVEMENT
    # -------------------------

    def move(self, room):

        self.current_room = room

    # -------------------------
    # ATTACK DAMAGE
    # -------------------------

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

    # -------------------------
    # ATTACK
    # -------------------------

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
                f"{self.name} tries to attack "
                f"{monster.name}..."
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

    # -------------------------
    # TAKE DAMAGE
    # -------------------------

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

    # -------------------------
    # INVENTORY
    # -------------------------

    def add_item(self, item):

        self.inventory.append(item)

    def show_inventory(self):

        if not self.inventory:

            print("\nInventory is empty.")

            return

        print("\n" + "=" * 40)
        print(" INVENTORY")
        print("=" * 40)

        # -------------------------
        # EQUIPMENT
        # -------------------------

        equipment = []

        equipment_keywords = [
            "sword",
            "axe",
            "dagger",
            "staff",
            "shield",
            "armor",
            "robes",
            "throwing knife"
        ]

        for item in self.inventory:

            if any(
                keyword in item.name.lower()
                for keyword in equipment_keywords
            ):

                equipment.append(item)

        if equipment:

            print("\nEquipment:")

            for item in equipment:

                print(
                    f" - {item.name}"
                )

        # -------------------------
        # CONSUMABLES
        # -------------------------

        consumables = []

        for item in self.inventory:

            if (
                "potion" in item.name.lower()
                or "scroll" in item.name.lower()
            ):

                consumables.append(item)

        if consumables:

            print("\nConsumables:")

            for item in consumables:

                print(
                    f" - {item.name}"
                )

        # -------------------------
        # MISCELLANEOUS
        # -------------------------

        miscellaneous = []

        for item in self.inventory:

            if (
                item not in equipment
                and item not in consumables
            ):

                miscellaneous.append(item)

        if miscellaneous:

            print("\nMiscellaneous:")

            for item in miscellaneous:

                print(
                    f" - {item.name}"
                )

        print("\n" + "=" * 40)