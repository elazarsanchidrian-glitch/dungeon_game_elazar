import json


class SaveSystem:

    SAVE_FILE = "savegame.json"

    @staticmethod
    def save(game):

        data = {
            "player": {
                "name": game.player.name,
                "gender": game.player.gender,
                "race": game.player.race,
                "character_class": game.player.character_class,
                "passive": game.player.passive,

                "health": game.player.health,
                "max_health": game.player.max_health,
                "stamina": game.player.stamina,
                "magicka": game.player.magicka,
                "gold": game.player.gold,

                "inventory": [
                    {
                        "name": item.name,
                        "description": item.description,
                        "value": item.value
                    }
                    for item in game.player.inventory
                ]
            },

            "dungeon": {
                "current_x": game.dungeon.current_x,
                "current_y": game.dungeon.current_y
            }
        }

        with open(SaveSystem.SAVE_FILE, "w") as file:
            json.dump(data, file, indent=4)

        print("\nGame saved successfully!")

    @staticmethod
    def load():

        try:
            with open(SaveSystem.SAVE_FILE, "r") as file:
                return json.load(file)

        except FileNotFoundError:

            print("\nNo save file found.")

            return None

        except json.JSONDecodeError:

            print("\nSave file is corrupted.")

            return None