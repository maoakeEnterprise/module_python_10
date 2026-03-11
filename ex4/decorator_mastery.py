from typing import Callable
from functools import wraps
import time
import random


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def measure_time(*args, **kwargs) -> None:
        print(f"Casting {func.__name__}:\n")
        t = time.time()
        func(*args, **kwargs)
        print(f"\nSpell completed in {(time.time() - t):.8f} s")
    return measure_time


def power_validator(min_power: int) -> Callable:

    def validator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> None:
            if kwargs["power"] >= min_power:
                return func(*args, **kwargs)
            else:
                return ("Insufficient power for this spell")
        return wrapper
    return validator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def retry(*args, **kwargs):
            attemps = 0
            while attemps < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"{e}")
                attemps += 1
            return f"Spell casting failed after {max_attempts} attemps"
        return retry
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        res = [letter for letter in name if not letter.isalpha()
               and letter != " "]
        if len(name) < 3 or res != []:
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


@spell_timer
def hadoken(spells: list) -> None:
    for spell in spells:
        print(f"Spell: {spell}")


@power_validator(14)
def hadokoko(powers: list) -> None:
    print(powers)


@retry_spell(6)
def test_spell(nb: int):
    valid = random.randint(1, 10)
    if valid < 9:
        raise ValueError("Miss attack")
    return nb


def main() -> None:
    test_powers = [26, 27, 7, 16]
    spell_names = ['lightning', 'flash', 'freeze', 'heal']
    mage_names = ['River', 'Alex', 'Rowan', 'Zara', 'Ash', 'Sage']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']
    print("Testing spell timer:")
    hadoken(spell_names)
    print("\nTesting retry spell: ")
    res = test_spell(8)
    print(f"Attack succeed -> damage: {res}")
    print("\nTest static method: ")
    for name in mage_names:
        print(f"name valid ? {MageGuild.validate_mage_name(name)} -> {name}")
    for name in invalid_names:
        print(f"name valid ? {MageGuild.validate_mage_name(name)} -> {name}")
    print("\nTesting cast_spell: ")
    mage = MageGuild()
    for i in range(0, len(test_powers)):
        print(mage.cast_spell(spell_name=spell_names[i],
                              power=(test_powers[i])))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Type Error {e.__class__.__name__}")
        print(f"Detail Error: {e}")
