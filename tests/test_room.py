from game.room import Room
from game.item import Item
from game.monster import Monster
from game.npc import NPC


def test_room_creation():
    room = Room("Cavern", "A dark cavern.")

    assert room.name == "Cavern"
    assert room.description == "A dark cavern."
    assert room.items == []
    assert room.monsters == []
    assert room.npcs == []


def test_add_and_remove_item():
    room = Room("Cavern", "A dark cavern.")
    item = Item("Sword", "A sword.", 50)

    room.add_item(item)

    assert item in room.items

    room.remove_item(item)

    assert item not in room.items


def test_add_and_remove_monster():
    room = Room("Cavern", "A dark cavern.")
    monster = Monster("Goblin", 50, 10)

    room.add_monster(monster)

    assert monster in room.monsters

    room.remove_monster(monster)

    assert monster not in room.monsters


def test_add_and_remove_npc():
    room = Room("Cavern", "A dark cavern.")
    npc = NPC("Traveler", "A mysterious traveler.")

    room.add_npc(npc)

    assert npc in room.npcs

    room.remove_npc(npc)

    assert npc not in room.npcs

