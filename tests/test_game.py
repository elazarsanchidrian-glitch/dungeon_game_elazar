from game.game import Game
from game.player import Player
from game.room import Room
from game.monster import Monster


def make_game():
    game = Game.__new__(Game)

    game.player = Player("Elazar")
    game.player.current_room = Room(
        "Test Room",
        "A room for testing."
    )

    class FakeUI:
        def show_message(self, message):
            pass

        def show_player_defeated(self):
            pass

        def show_victory(self):
            pass

    game.ui = FakeUI()

    return game




def test_monster_attack():
    game = make_game()

    monster = Monster("Goblin", 50, 10)

    starting_health = game.player.health

    game.monster_attack(monster)

    assert game.player.health < starting_health


def test_successful_dodge(monkeypatch):
    game = make_game()

    monster = Monster("Goblin", 50, 10)

    monkeypatch.setattr(
        "game.game.random.random",
        lambda: 0.1
    )

    starting_health = game.player.health

    result = game.dodge(monster)

    assert result is True
    assert game.player.health == starting_health




def test_failed_dodge(monkeypatch):
    game = make_game()

    monster = Monster("Goblin", 50, 10)

    monkeypatch.setattr(
        "game.game.random.random",
        lambda: 0.9
    )

    starting_health = game.player.health

    game.dodge(monster)

    assert game.player.health < starting_health



def test_successful_escape(monkeypatch):
    game = make_game()

    monster = Monster("Goblin", 50, 10)
    game.player.current_room.add_monster(monster)

    monkeypatch.setattr(
        "game.game.random.random",
        lambda: 0.1
    )

    result = game.escape(monster)

    assert result is True
    assert monster not in game.player.current_room.monsters



def test_failed_escape(monkeypatch):
    game = make_game()

    monster = Monster("Goblin", 50, 10)
    game.player.current_room.add_monster(monster)

    monkeypatch.setattr(
        "game.game.random.random",
        lambda: 0.9
    )

    starting_health = game.player.health

    game.escape(monster)

    assert monster in game.player.current_room.monsters
    assert game.player.health < starting_health



def test_successful_dialogue(monkeypatch):
    game = make_game()

    monster = Monster(
        "Goblin",
        50,
        10,
        dialogue=["Give me your gold!"],
        dialogue_success_chance=65
    )

    game.player.current_room.add_monster(monster)

    monkeypatch.setattr(
        "game.game.random.randint",
        lambda a, b: 1
    )

    result = game.dialogue(monster)

    assert result is True
    assert monster not in game.player.current_room.monsters




def test_failed_dialogue(monkeypatch):
    game = make_game()

    monster = Monster(
        "Goblin",
        50,
        10,
        dialogue=["Give me your gold!"],
        dialogue_success_chance=65
    )

    game.player.current_room.add_monster(monster)

    monkeypatch.setattr(
        "game.game.random.randint",
        lambda a, b: 100
    )

    starting_health = game.player.health

    game.dialogue(monster)

    assert monster in game.player.current_room.monsters
    assert game.player.health < starting_health



def test_check_for_exit():
    game = make_game()

    game.player.current_room.is_exit = True

    assert game.check_for_exit() is True


def test_check_for_exit_false():
    game = make_game()

    game.player.current_room.is_exit = False

    assert game.check_for_exit() is False



