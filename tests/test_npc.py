from game.npc import NPC


def test_npc_creation():
    npc = NPC("Traveler", "A mysterious traveler.")

    assert npc.name == "Traveler"
    assert npc.description == "A mysterious traveler."