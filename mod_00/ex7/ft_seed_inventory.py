def ft_seed_inventory(seed: str, num: int, unit: str) -> None:
    if unit == "packets":
        last_str = f"{num} packets available"
    elif unit == "grams":
        last_str = f"{num} grams total"
    elif unit == "area":
        last_str = f"covers {num} square meters"
    else:
        print("Unknown unit type")
        return

    print(f"{seed.capitalize()} seeds: {last_str}")
