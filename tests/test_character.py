from game.character import CharacterCreation


def test_character_creation():
    character = CharacterCreation("Elazar")

    assert character.name == "Elazar"
    assert character.gender is None
    assert character.race is None
    assert character.character_class is None


def test_choose_class_mage(monkeypatch):
    character = CharacterCreation("Elazar")

    monkeypatch.setattr("builtins.input", lambda _: "2")

    character.choose_class()

    assert character.character_class == "Mage"
    assert character.health == 180
    assert character.stamina == 180
    assert character.magicka == 250