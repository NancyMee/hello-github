"""Tests for hello.py. Run with: python -m pytest"""

from hello import greet


def test_greet_with_name():
    assert greet("Nancy") == "Hello, Nancy!"


def test_greet_trims_whitespace():
    assert greet("  Nancy  ") == "Hello, Nancy!"


def test_greet_without_name():
    assert greet("") == "Hello, friend!"
    assert greet(None) == "Hello, friend!"
