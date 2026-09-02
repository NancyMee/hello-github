"""Tests for hello.py. Run with: python -m pytest"""

import pytest

from hello import greet, add


def test_greet_with_name():
    assert greet("Nancy") == "Hello, Nancy!"


def test_greet_trims_whitespace():
    assert greet("  Nancy  ") == "Hello, Nancy!"


def test_greet_without_name():
    assert greet("") == "Hello, friend!"
    assert greet(None) == "Hello, friend!"


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-4, 1) == -3


def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)
