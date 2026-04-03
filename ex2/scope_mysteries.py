from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def increase() -> int:
        nonlocal count
        count += 1
        return count
    return increase


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def increase_power(increase: int) -> int:
        nonlocal power
        power += increase
        return power
    return increase_power


def enchantment_factory(enchantment_type: str) -> Callable:
    enchant = enchantment_type

    def item_enchanted(item: str) -> str:
        nonlocal enchant
        return f"{enchant} {item}"
    return item_enchanted


def memory_vault() -> dict[str, Callable]:
    store: dict = {}

    def stores(key: str, value: Any) -> None:
        nonlocal store
        store.update({key: value})

    def recall(key: str) -> Any:
        nonlocal store
        if key not in {key for key in store.keys()}:
            return "Memory not found"
        return store[key]
    return {"stores": stores, "recall": recall}


def main() -> None:
    initial_powers = [60, 49, 78]
    power_additions = [9, 15, 16, 14, 18]
    enchantment_types = ['Windy', 'Earthen', 'Flowing']
    items_to_enchant = ['Staff', 'Cloak', 'Amulet', 'Ring']
    print("Testing mage counter:")
    increase = mage_counter()
    for _ in range(10):
        print(f"mage {increase()}")

    print("\nTesting increase power: ")
    for start in initial_powers:
        power_up = spell_accumulator(start)
        for add_power in power_additions:
            pw = power_up(add_power)
            print(f"Mage power to start: {start}  to power up : {pw}")

    print("\nTesting enchant item: ")
    for enchant in enchantment_types:
        f = enchantment_factory(enchant)
        for item in items_to_enchant:
            print(f"Enchanted item{f(item)}")

    print("\n Testing my vault: ")
    dict_f = memory_vault()
    for i in range(0, len(initial_powers)):
        dict_f["stores"](enchantment_types[i], initial_powers[i])
    for key in enchantment_types:
        print(f"vaulted: {dict_f['recall'](key)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Type Error : {e.__class__.__name__}")
        print(f"Details Error : {e}")
