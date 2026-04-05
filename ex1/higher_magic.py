from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs) -> tuple:
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs) -> int:
        kwargs["power"] *= multiplier
        res = base_spell(*args, **kwargs)
        return res
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditioned(*args, **kwargs) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditioned


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequenced(*args, **kwargs) -> list:
        res = []
        res = [spell(*args, **kwargs) for spell in spells]
        return res
    return sequenced


def fireball(target: str, power: int) -> str:
    return f"Fire Power {target} for {power} DMG"


def heal(target: str, power: int) -> str:
    return f"Heal {target} for {power} HP"


def conditional(target: str, power: int) -> bool:
    if target == "DRAGON" or power == 2:
        return False
    return True


def main() -> None:
    amplified_data = {
        "GOBLIN": 4,
        "DRAGON": 2,
        "FISHER": 1,
    }
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    conditional_data = {
        "DRAGON": 4,
        "GOBLIN": 2,
        "WIZZARD": 6,
        "POOP": 4562
    }

    print("\nTesting spell combiner...")
    for target in test_targets:
        combined = spell_combiner(fireball, heal)
        sp1, sp2 = combined(target=target, power=3)
        print(f"Combined spell result: {sp1}, {sp2}")

    print("\nTesting amplifier: ")
    for k, v in amplified_data.items():
        amplified = power_amplifier(fireball, v)
        print(amplified(target=k, power=3))

    print("\nTesting conditional")
    conditioned = conditional_caster(conditional, fireball)
    for k, v in conditional_data.items():
        print(conditioned(target=k, power=v))

    print("\n Testing sequenced")
    sequenced = spell_sequence([fireball, heal])
    for target in test_targets:
        print(sequenced(target=target, power=3))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Type Error: {e.__class__.__name__}")
        print(f"Error Message: {e}")
