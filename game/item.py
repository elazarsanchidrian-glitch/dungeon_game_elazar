class Item:

    def __init__(self, name, description, value=0):

        self.name = name
        self.description = description
        self.value = value

    def inspect(self):

        print(f"\n{self.name}")
        print(self.description)

        if self.value > 0:
            print(f"Value: {self.value} gold")

    def __str__(self):

        return self.name