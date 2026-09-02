"""A tiny module for practicing the GitHub pull request workflow."""


def greet(name):
    """Return a friendly greeting for the given name."""
    name = (name or "").strip()
    if not name:
        return "Hello, friend!"
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    print(greet("NancyMee"))
    print(f"2 + 3 = {add(2, 3)}")
