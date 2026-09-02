from game.save_system import SaveSystem


def test_load_missing_save(monkeypatch):
    monkeypatch.setattr(
        SaveSystem,
        "SAVE_FILE",
        "nonexistent_save.json"
    )

    result = SaveSystem.load()

    assert result is None


import json

from game.save_system import SaveSystem
from game.item import Item


def test_save_game(tmp_path):
    save_file = tmp_path / "savegame.json"

    monkeypatch = None

    SaveSystem.SAVE_FILE = str(save_file)

    class FakePlayer:
        name = "Elazar"
        gender = "Male"
        race = "Human"
        character_class = "Warrior"
        passive = "Strong"
        health = 100
        max_health = 100
        stamina = 120
        magicka = 50
        gold = 25
        inventory = [Item("Sword", "A sword.", 50)]

    class FakeDungeon:
        current_x = 3
        current_y = -2

    class FakeGame:
        player = FakePlayer()
        dungeon = FakeDungeon()

    SaveSystem.save(FakeGame())

    with open(save_file, "r") as file:
        data = json.load(file)

    assert data["player"]["name"] == "Elazar"
    assert data["player"]["gold"] == 25
    assert data["player"]["inventory"][0]["name"] == "Sword"
    assert data["dungeon"]["current_x"] == 3
    assert data["dungeon"]["current_y"] == -2



def test_save_game(tmp_path, monkeypatch):
    save_file = tmp_path / "savegame.json"

    monkeypatch.setattr(
        SaveSystem,
        "SAVE_FILE",
        str(save_file)
    )

    # rest of test...