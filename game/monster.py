import random


class Monster:

    def __init__(self, name, health=100, attack_damage=10):
        self.name = name
        self.health = health
        self.max_health = health
        self.stamina = 100
        self.magicka = 100
        self.attack_damage = attack_damage

    def speak(self):
        dialogue = [
            f"{self.name}: Grrrr...",
            f"{self.name}: Who dares enter my dungeon?",
            f"{self.name}: You should not have come here...",
            f"{self.name}: Leave... while you still can.",
            f"{self.name}: RAAAAAGH!",
            f"{self.name}: Fresh meat!",
            f"{self.name}: Hssss...",
            f"{self.name}: You will regret this.",
            f"{self.name}: Intruder!",
            f"{self.name}: Grrrrr... prepare yourself!"
        ]

        print(random.choice(dialogue))

    def attack(self):
        attack_sounds = [
            f"{self.name}: RAAAH!",
            f"{self.name}: Grrrrr!",
            f"{self.name}: HAAA!",
            f"{self.name}: DIE!",
            f"{self.name}: *roars*"
        ]

        print(random.choice(attack_sounds))
        print(f"{self.name} attacks!")

        return self.attack_damage

    def take_damage(self, damage):
        self.health -= damage

        if self.health < 0:
            self.health = 0

        if self.health > 0:
            reactions = [
                f"{self.name}: GRAAAH!",
                f"{self.name}: You will pay for that!",
                f"{self.name}: *growls in pain*",
                f"{self.name}: Rrrrr...",
                f"{self.name}: Is that all you've got?"
            ]

            print(random.choice(reactions))

        else:
            death_sounds = [
                f"{self.name}: Noooo...",
                f"{self.name}: *lets out a final roar*",
                f"{self.name}: Grrrr... *falls*",
                f"{self.name}: This... cannot be..."
            ]

            print(random.choice(death_sounds))

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return self.name