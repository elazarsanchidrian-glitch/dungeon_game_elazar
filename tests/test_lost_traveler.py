from game.lost_traveler import LostTraveler


def test_lost_traveler_creation():
    traveler = LostTraveler()

    assert traveler.name == "Lost Traveler"
    assert traveler.description == (
        "A weary traveler covered in dust and scratches."
    )