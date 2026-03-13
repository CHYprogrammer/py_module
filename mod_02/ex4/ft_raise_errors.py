#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, water: int, sunlight: int) -> None:
        self.name = name
        self.water = water
        self.sunlight = sunlight


def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
        ) -> str:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")
    else:
        return f"Plant '{plant_name}' is healthy!"


def execute_plant_check(name: str, water: int, sunlight: int) -> None:
    try:
        print(check_plant_health(name, water, sunlight))
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    tomato = Plant("tomato", 5, 7)

    print("\nTesting good values...")
    execute_plant_check(tomato.name, tomato.water, tomato.sunlight)

    print("\nTesting empty plant name...")
    execute_plant_check(None, tomato.water, tomato.sunlight)

    print("\nTesting bad water level...")
    execute_plant_check(tomato.name, 15, tomato.sunlight)

    print("\nTesting bad sunlight hours...")
    execute_plant_check(tomato.name, tomato.water, 0)

    print("\nAll error raisiing tests completed!")


if __name__ == "__main__":
    test_plant_checks()
