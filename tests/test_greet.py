from src.greet import greet


def test_greet_returns_greeting():
    assert greet("World") == "Hello, World!"


def test_greet_with_empty_name():
    assert greet("") == "Hello, !"
