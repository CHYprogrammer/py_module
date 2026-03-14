#!/usr/bin/env python3

import sys


def parse_args(argv: list[str]) -> dict | None:
    try:
        inventory = {}
        total = 0
        for str in argv:
            lst = str.split(":")
            key = lst[0]
            value = int(lst[1])
            if value < 0:
                print("***WARNING!: value cannot be less than 0: "
                      + f"{{'{key}': {value}}}***")
                break
            inventory.update({key: value})
            total += inventory[key]
        print(f"Total items in inventory: {total}")
        print(f"Unique item: {len(inventory)}")
        return inventory
    except Exception as e:
        print(f"Error while parsing arguments vectors: {e}")
        return None


def current_inventory(inventory: dict) -> None:
    total = 0
    for value in inventory.values():
        total += value

    visited = []
    for _ in inventory:
        max_key = None
        for item in inventory:
            if item not in visited:
                if max_key is None or inventory[item] > inventory[max_key]:
                    max_key = item
        visited += [max_key]

        quantity = inventory[max_key]
        occupancy_rate = quantity / total * 100
        unit = "unit" if quantity == 1 else "units"
        print(f"{max_key}: {quantity} {unit} ({occupancy_rate:.1f}%)")


def inventory_statistics(inventory: dict) -> None:
    if not inventory:
        return None

    max_item = None
    min_item = None

    for item in inventory:
        if max_item is None or inventory[item] > inventory[max_item]:
            max_item = item
        if min_item is None or inventory[item] < inventory[min_item]:
            min_item = item

    unit = "unit" if inventory[max_item] == 1 else "units"
    print(f"Most abundant: {max_item} ({inventory[max_item]} {unit})")
    unit = "unit" if inventory[min_item] == 1 else "units"
    print(f"Least abundant: {min_item} ({inventory[min_item]} {unit})")


def item_categories(inventory: dict) -> None:
    if not inventory:
        return None

    abundant = {}
    moderate = {}
    scarce = {}

    for item in inventory:
        if inventory[item] > 6:
            abundant[item] = inventory[item]
        elif inventory[item] > 3:
            moderate[item] = inventory[item]
        else:
            scarce[item] = inventory[item]

    if abundant:
        print(f"Abundant: {abundant}")
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")


def management_suggestions(inventory: dict) -> None:
    restock_needed = []
    for item in inventory:
        if inventory[item] <= 1:
            restock_needed += [item]
    print("Restock needed: ", end="")
    for item in restock_needed:
        if item == restock_needed[-1]:
            suf = "\n"
        else:
            suf = ", "
        print(item, end=suf)
    if not inventory:
        print()


def sample_lookup(target: str, inventory: dict) -> None:
    flag = False
    if target in inventory:
        flag = True
    print(f"Sample lookup - {target} in inventory: {flag}")


def check_keys_and_values(inventory: dict) -> None:
    print("Dictionary keys: ", end="")
    key_lst = list(inventory.keys())
    for key in key_lst:
        if key == key_lst[-1]:
            suf = "\n"
        else:
            suf = ", "
        print(key, end=suf)
    if not key_lst:
        print()

    print("Dictionary values: ", end="")
    key_lst = list(inventory.keys())
    for key in key_lst:
        if key == key_lst[-1]:
            suf = "\n"
        else:
            suf = ", "
        print(inventory.get(key), end=suf)
    if not key_lst:
        print()


if __name__ == "__main__":
    try:
        print("=== Inventory System Analysis ===")
        inventory = parse_args(sys.argv[1:])
        if not inventory:
            raise Exception("No inventory")

        print("\n=== Current Inventory ===")
        current_inventory(inventory)

        print("\n=== Inventory Statistics ===")
        inventory_statistics(inventory)

        print("\n=== Item Categories ===")
        item_categories(inventory)

        print("\n=== Management Suggestion ===")
        management_suggestions(inventory)

        print("\n=== Dictionary Properties Demo ===")
        check_keys_and_values(inventory)
        sample_lookup('sword', inventory)

    except KeyError:
        print("Usage: python3 ft_inventory_system.py"
              + " <item1:quantity1> <item2:quantity2> ...")
    except Exception as e:
        print(f"Error: {e}")
