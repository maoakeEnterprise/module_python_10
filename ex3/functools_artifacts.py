from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    res = 0
    if operation == "add":
        res = reduce(operator.add, spells)
    elif operation == "multiply":
        res = reduce(operator.mul, spells)
    elif operation == "max":
        res = reduce(max, spells)
    elif operation == "min":
        res = reduce(min, spells)
    return res


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, enchant=154)
    lightning = partial(base_enchantment, enchant=120)
    ice = partial(base_enchantment, enchant=140)
    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning
    }


@lru_cache(maxsize=2)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> callable:

    @singledispatch
    def anyfunc(value: Any) -> None:
        print(f"Unknow type: {value}")

    @anyfunc.register
    def _(value: int):
        print(f"dammage: {value}")

    @anyfunc.register
    def _(value: str):
        print(f"enchant: {value}")

    @anyfunc.register
    def _(value: list):
        print(f"multi cast: {value}")

    return anyfunc


def base_enchant(power: int, enchant: int) -> int:
    return power + enchant


def main() -> None:
    spell_powers = [20, 24, 18, 11, 41, 37]
    operations = ['add', 'multiply', 'max', 'min']
    enchant = ["fire_enchant", "ice_enchant", "lightning_enchant"]
    dispatcher = [20, "fire", [10, 30, "water"], {}]
    fibonacci_tests = [12, 18, 12]
    print("Testing spell_reducer: ")
    for operation in operations:
        print(f"{operation} -> {spell_powers}: "
              f"{spell_reducer(spell_powers, operation)} ")

    print("\nTestin partial enchanter: ")
    enchant_spell = partial_enchanter(base_enchant)
    for key in enchant:
        print(f"{key} -> {enchant_spell[key](50)}")

    print("\nTesting fibo: ")
    for test in fibonacci_tests:
        print(memoized_fibonacci(test))

    print("\nTesting spell dispatcher: ")
    dispatch = spell_dispatcher()
    for var in dispatcher:
        dispatch(var)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Type Erro: {e.__class__.__name__}")
        print(f"Details Error: {e}")
