class Monster:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.stamina = 100
        self.magicka = 100

    def attack(self):
        print(f"{self.name} attacks!")

    def take_damage(self, damage):
        self.health -= damage

        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return self.name