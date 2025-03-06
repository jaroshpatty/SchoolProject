import random

def get_random_number(low: int = 1, high: int = 100) -> int:
    """Returns a random number between low and high (inclusive)."""
    return random.randint(low, high)