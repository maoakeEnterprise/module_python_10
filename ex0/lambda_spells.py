def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    res = sorted(artifacts, key=lambda x: x["power"], reverse=True)
    return res


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    tab = filter(lambda x: x["power"] >= min_power, mages)
    return list(tab)


def spell_transformer(spells: list[str]) -> list[str]:
    res = map(lambda x: "*" + x + "*", spells)
    return list(res)


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda x: x["power"])["power"],
        "min_power": min(mages, key=lambda x: x["power"])["power"],
        "avg_power": sum(map(lambda x: x["power"], mages)) / len(mages)
    }


def main() -> None:
    artifacts = [
        {'name': 'Fire Staff', 'power': 110, 'type': 'armor'},
        {'name': 'Shadow Blade', 'power': 83, 'type': 'focus'},
        {'name': 'Wind Cloak', 'power': 117, 'type': 'relic'},
        {'name': 'Light Prism', 'power': 66, 'type': 'focus'}
        ]
    mages = [
        {'name': 'Phoenix', 'power': 84, 'element': 'shadow'},
        {'name': 'Casey', 'power': 95, 'element': 'earth'},
        {'name': 'Jordan', 'power': 94, 'element': 'light'},
        {'name': 'Rowan', 'power': 70, 'element': 'fire'},
        {'name': 'Phoenix', 'power': 55, 'element': 'water'}]
    spells = ['shield', 'tornado', 'freeze', 'flash']

    print("Testing artifact sorter...")
    res = artifact_sorter(artifacts)
    print(f"{res[0]['name']} ({res[0]['power']} power) "
          f"come before {res[1]['name']} ({res[1]['power']} power)")

    print("\nTesting power lifter....")
    min_p = 90
    res = power_filter(mages, 90)
    print(f"There is {len(res)} mages upper to {min_p}")

    print("\nTesting spell transformer..............")
    res = spell_transformer(spells)
    print(res)

    print("\nTesting mage stats............;;;.......")
    res = mage_stats(mages)
    print(res)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Type Error: {e.__class__.__name__}")
        print(f"Message Error: {e}")
