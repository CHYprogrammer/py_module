#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot Water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    valid_lists = ["tomato", "lettuce", "carrots"]
    water_plants(valid_lists)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    invalid_lists = ["tomato", None, "carrots"]
    water_plants(invalid_lists)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
