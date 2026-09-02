from game.ui import ConsoleUI


def test_show_welcome(capsys):
    ui = ConsoleUI()

    ui.show_welcome()

    output = capsys.readouterr().out

    assert "Welcome to the Dungeon Game!" in output


def test_get_command(monkeypatch):
    ui = ConsoleUI()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "  NORTH  "
    )

    result = ui.get_command()

    assert result == "north"


def test_show_error(capsys):
    ui = ConsoleUI()

    ui.show_error("Invalid direction.")

    output = capsys.readouterr().out

    assert "[ERROR] Invalid direction." in output


def test_get_menu_choice(monkeypatch):
    ui = ConsoleUI()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "2"
    )

    assert ui.get_menu_choice() == "2"




