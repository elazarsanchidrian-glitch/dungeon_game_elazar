class Monster:

    def __init__(self,name):
        self.name = name
        self.health = 100
        self.stamina = 100
        self.magicka = 100



    def attack(self):
        pass

    def take_damage(self):
        self.health -= 10

    def is_alive(self):
        pass
