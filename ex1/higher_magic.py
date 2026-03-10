from typing import Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs) -> tuple:
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs) -> int:
        res = base_spell(*args, **kwargs)
        res *= multiplier
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


def fireball(target: str) -> str:
    return f"Fire Power {target}"


def heal(target: str) -> str:
    return f"Heal {target}"


def base_spell(spell: str):
    spells = {
        "Fireball": 10,
        "Bolted": 7,
        "heal": 3
    }
    if spell not in [key for key in spells.keys()]:
        return 0
    return spells[spell]


def conditional(string: Any):
    if isinstance(string, str):
        return True
    return False


def main() -> None:
    test_values = [5, 15, 8]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    test_targets1 = ['Dragon', 'Goblin', {'gogo'},
                     {'go': 23}, 'Wizard', 'Knight', 23]

    print("\nTesting spell combiner...")
    for target in test_targets:
        combined = spell_combiner(fireball, heal)
        sp1, sp2 = combined(target=target)
        print(f"Combined spell result: {sp1}, {sp2}")

    print("\nTesting amplifier: ")
    for value in test_values:
        amplified = power_amplifier(base_spell, value)
        print(f"Spell amplified dmg or heal: {amplified('Fireball')}")

    print("\nTesting conditional")
    conditioned = conditional_caster(conditional, fireball)
    for target in test_targets1:
        print(conditioned(target))

    print("\n Testing sequenced")
    sequenced = spell_sequence([fireball, heal])
    for target in test_targets:
        print(sequenced(target))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Type Error: {e.__class__.__name__}")
        print(f"Error Message: {e}")
