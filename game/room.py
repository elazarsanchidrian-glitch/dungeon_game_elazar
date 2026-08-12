import random


class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.items = []
        self.monsters = []

        self.visited = False

        # Things the player might notice
        self.sights = []
        self.sounds = []

    # -------------------------
    # ITEMS
    # -------------------------

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    # -------------------------
    # MONSTERS
    # -------------------------

    def add_monster(self, monster):
        self.monsters.append(monster)

    def remove_monster(self, monster):
        if monster in self.monsters:
            self.monsters.remove(monster)

    # -------------------------
    # EXPLORATION
    # -------------------------

    def generate_atmosphere(self):
        """Generate things the player can see and hear."""

        sight_options = [
            "Dust floats through the air.",
            "Old scratches cover the stone walls.",
            "Faint torchlight flickers in the distance.",
            "The walls are covered in strange markings.",
            "Broken stones litter the floor.",
            "You notice old footprints in the dust.",
            "Something seems to have moved recently.",
            "Cobwebs hang from the ceiling.",
            "The darkness makes it difficult to see far ahead.",
            "You notice dried blood on the floor."
        ]

        sound_options = [
            "You hear dripping water somewhere nearby.",
            "A distant scraping sound echoes through the dungeon.",
            "You hear the faint sound of wind.",
            "Something creaks in the darkness.",
            "You hear distant footsteps.",
            "A strange whisper echoes through the room.",
            "You hear something moving far away.",
            "The dungeon is completely silent.",
            "Water trickles somewhere beneath the floor.",
            "You hear a distant growl."
        ]

        self.sights = random.sample(
            sight_options,
            random.randint(1, 3)
        )

        self.sounds = random.sample(
            sound_options,
            random.randint(1, 2)
        )

    def explore(self):

        print(f"\n{'=' * 50}")
        print(f"Exploring: {self.name}")
        print(f"{'=' * 50}")

        print(f"\n{self.description}")

        # Generate atmosphere the first time
        if not self.visited:
            self.generate_atmosphere()
            self.visited = True

        # -------------------------
        # SIGHTS
        # -------------------------

        print("\nYou look around...")

        if self.sights:
            print("\nYou see:")
            for sight in self.sights:
                print(f" - {sight}")

        # -------------------------
        # SOUNDS
        # -------------------------

        if self.sounds:
            print("\nYou hear:")
            for sound in self.sounds:
                print(f" - {sound}")

        # -------------------------
        # ITEMS
        # -------------------------

        if self.items:
            print("\nYou notice something you can pick up:")

            for item in self.items:
                print(f" - {item.name}")

        else:
            print("\nYou don't see anything useful to pick up.")

        # -------------------------
        # MONSTERS
        # -------------------------

        if self.monsters:
            print("\nYou sense danger...")

            for monster in self.monsters:
                print(
                    f" - {monster.name} "
                    f"(HP: {monster.health}/{monster.max_health})"
                )

        else:
            print("\nYou don't see any enemies.")

    # -------------------------
    # DISPLAY
    # -------------------------

    def display(self):

        print(f"\n{'=' * 40}")
        print(f"Room: {self.name}")
        print(f"{'=' * 40}")

        if self.description:
            print(self.description)

        if self.items:
            print("\nItems:")

            for item in self.items:
                print(f" - {item}")

        if self.monsters:
            print("\nMonsters:")

            for monster in self.monsters:
                print(
                    f" - {monster} "
                    f"(HP: {monster.health}/{monster.max_health})"
                )

        if not self.items and not self.monsters:
            print("\nThe room is empty.")