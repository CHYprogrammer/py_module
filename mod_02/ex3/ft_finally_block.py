#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            try:
                plant + ""
            except TypeError:
                raise TypeError(plant)
            print(f"Watering {plant}")
    except TypeError as e:
        print(f"Error: Cannot Water {e} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    try:
        print("\nTesting normal watering...")
        valid_lists = ["tomato", "lettuce", "carrots"]
        water_plants(valid_lists)
        print("Watering completed successfully!")

        print("\nTesting with error...")
        invalid_lists = ["tomato", None, "carrot"]
        water_plants(invalid_lists)
    except Exception as e:
        print(f"Unexpected error occured: {e}")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
