import random


class Player:

    def __init__(self, name):
        self.name = name

        self.gender = None
        self.race = None
        self.character_class = None
        self.passive = None

        self.health = 100
        self.max_health = 100
        self.stamina = 100
        self.magicka = 100

        self.gold = 50
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100

        self.inventory = []

        self.equipped_weapon = None
        self.equipped_armor = None
        self.equipped_shield = None

        self.current_room = None

    def setup_starting_inventory(self):
        from .item import Item

        if self.character_class == "Warrior":
            self.inventory.append(
                Item("Iron Sword", "A sturdy iron sword.", 20, "weapon", power=15)
            )
            self.inventory.append(
                Item("Iron Shield", "A basic metal shield.", 25, "shield", defense=10)
            )
            self.inventory.append(
                Item(
                    "Health Potion",
                    "Restores 30 HP.",
                    15,
                    "consumable",
                    power=30,
                )
            )

        elif self.character_class == "Mage":
            self.inventory.append(
                Item(
                    "Wooden Staff",
                    "A wooden staff emitting faint magical energy.",
                    20,
                    "weapon",
                    power=10,
                )
            )
            self.inventory.append(
                Item("Cloth Robes", "Simple wizard robes.", 15, "armor", defense=5)
            )
            self.inventory.append(
                Item(
                    "Health Potion",
                    "Restores 30 HP.",
                    15,
                    "consumable",
                    power=30,
                )
            )

        elif self.character_class == "Rogue":
            self.inventory.append(
                Item(
                    "Steel Dagger",
                    "A sharp dagger for swift strikes.",
                    20,
                    "weapon",
                    power=12,
                )
            )
            self.inventory.append(
                Item(
                    "Leather Armor",
                    "Light armor allowing easy movement.",
                    20,
                    "armor",
                    defense=8,
                )
            )
            self.inventory.append(
                Item(
                    "Health Potion",
                    "Restores 30 HP.",
                    15,
                    "consumable",
                    power=30,
                )
            )

    def show_inventory(self):
        print("\n===== INVENTORY =====")
        if not self.inventory:
            print("Your inventory is empty.")
            return

        for item in self.inventory:
            equipped_status = ""
            if item == self.equipped_weapon:
                equipped_status = " (Equipped Weapon)"
            elif item == self.equipped_armor:
                equipped_status = " (Equipped Armor)"
            elif item == self.equipped_shield:
                equipped_status = " (Equipped Shield)"

            print(f"- {item.name}: {item.description}{equipped_status}")

        print(f"\nGold: {self.gold}")

    def auto_equip_starting_gear(self):
        for item in self.inventory:
            if item.item_type == "weapon" and not self.equipped_weapon:
                self.equipped_weapon = item
            elif item.item_type == "armor" and not self.equipped_armor:
                self.equipped_armor = item
            elif item.item_type == "shield" and not self.equipped_shield:
                self.equipped_shield = item

    def take_damage(self, damage):
        reduction = 0
        if self.equipped_armor:
            reduction += getattr(self.equipped_armor, "defense", 0)
        if self.equipped_shield:
            reduction += getattr(self.equipped_shield, "defense", 0)

        effective_damage = max(1, damage - reduction)
        self.health -= effective_damage
        if self.health < 0:
            self.health = 0
        return effective_damage

    def attack(self, monster):
        base_damage = random.randint(10, 20)
        if self.equipped_weapon:
            base_damage += getattr(self.equipped_weapon, "power", 0)

        monster.health -= base_damage
        print(
            f"You attack {monster.name} with {self.equipped_weapon.name if self.equipped_weapon else 'your fists'} for {base_damage} damage!"
        )
        return True

    def use_ability(self, monster):
        if self.character_class == "Warrior":
            if self.stamina < 20:
                print("Not enough stamina!")
                return False
            self.stamina -= 20
            damage = random.randint(25, 40)
            monster.health -= damage
            print(f"You use Power Strike! Dealt {damage} damage to {monster.name}.")
            return True

        elif self.character_class == "Mage":
            if self.magicka < 25:
                print("Not enough magicka!")
                return False
            self.magicka -= 25
            damage = random.randint(30, 50)
            monster.health -= damage
            print(f"You cast Fireball! Dealt {damage} damage to {monster.name}.")
            return True

        elif self.character_class == "Rogue":
            if self.stamina < 15:
                print("Not enough stamina!")
                return False
            self.stamina -= 15
            damage = random.randint(20, 45)
            monster.health -= damage
            print(f"You use Backstab! Dealt {damage} damage to {monster.name}.")
            return True

        return False

    def gain_xp(self, amount):
        self.xp += amount
        print(f"You gained {amount} XP!")
        if self.xp >= self.xp_to_next_level:
            self.level += 1
            self.xp -= self.xp_to_next_level
            self.xp_to_next_level = int(self.xp_to_next_level * 1.5)
            self.max_health += 20
            self.health = self.max_health
            print(f"Level Up! You are now level {self.level}!")

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def use_item(self, item_name):
        item = next(
            (i for i in self.inventory if i.name.lower() == item_name.lower()), None
        )
        if not item:
            print("You don't have that item.")
            return False

        if item.item_type == "consumable":
            # Fully restore health to maximum
            self.health = self.max_health
            self.inventory.remove(item)
            print(f"You used {item.name} and your health was fully restored to {self.max_health} HP!")
            return True
        else:
            print(f"{item.name} cannot be consumed. Try using 'equip'.")
            return False

    def equip_item(self, item_name):
        item = next(
            (i for i in self.inventory if i.name.lower() == item_name.lower()), None
        )
        if not item:
            print("You don't have that item in your inventory.")
            return

        if item.item_type == "weapon":
            self.equipped_weapon = item
            print(f"Equipped weapon: {item.name}")
        elif item.item_type == "armor":
            self.equipped_armor = item
            print(f"Equipped armor: {item.name}")
        elif item.item_type == "shield":
            self.equipped_shield = item
            print(f"Equipped shield: {item.name}")
        else:
            print(f"{item.name} cannot be equipped.")