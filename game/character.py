class CharacterCreation:

    def __init__(self, name):
        self.name = name
        self.character_class = None

        self.health = 100
        self.stamina = 100
        self.magicka = 100

    def choose_class(self):
        print("\nChoose your class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")

        choice = input("Choice: ")

        if choice == "1":
            self.character_class = "Warrior"
            self.health = 150
            self.stamina = 120
            self.magicka = 50

        elif choice == "2":
            self.character_class = "Mage"
            self.health = 80
            self.stamina = 80
            self.magicka = 150

        elif choice == "3":
            self.character_class = "Rogue"
            self.health = 100
            self.stamina = 150
            self.magicka = 75

        else:
            print("Invalid choice. Warrior selected.")
            self.character_class = "Warrior"
            self.health = 150
            self.stamina = 120
            self.magicka = 50

    def show_character(self):
        print("\n===== CHARACTER CREATED =====")
        print(f"Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Health: {self.health}")
        print(f"Stamina: {self.stamina}")
        print(f"Magicka: {self.magicka}")