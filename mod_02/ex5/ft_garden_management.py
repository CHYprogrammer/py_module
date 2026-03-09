#!/usr/bin/env python3

class GardenError(Exception):
    pass


class AddingPlantError(GardenError):
    pass


class HealthError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    def __init__(self, water: int = 0) -> None:
        self.__plants: list[Plant] = []
        self.tank = water

    def add_plant(self, plant: Plant) -> None:
        if not plant.name:
            raise AddingPlantError("Plant name cannot be empty!")
        print(f"Added {plant.name} successfully")
        self.__plants += [plant]

    def water_plants(self) -> None:
        for plant in self.__plants:
            try:
                plant.name + ""
            except TypeError:
                raise WaterError(plant.name)
            print(f"Watering {plant.name} - success")
            self.tank -= 1

    def check_plant_health(self) -> None:
        for plant in self.__plants:
            if plant.water < 1:
                raise HealthError(
                    f"Error checking {plant.name}: "
                    + f"Water level {plant.water} is too low (min 1)")
            elif plant.water > 10:
                raise HealthError(
                    f"Error checking {plant.name}: "
                    + f"Water level {plant.water} is too high (max 10)")
            if plant.sun < 2:
                raise HealthError(
                    f"Error checking {plant.name}: "
                    + f"Sunlight hours {plant.sun} is too low (min 2)")
            elif plant.sun > 12:
                raise HealthError(
                    f"Error checking {plant.name}: "
                    + f"Sunlight hours {plant.sun} is too high (max 12)")
            print(f"{plant.name}: healthy "
                  + f"(water: {plant.water}, sun: {plant.sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===")

    water_amount = 1
    garden = GardenManager(water_amount)
    tomato = Plant("tomato", 5, 8)
    lettuce = Plant("lettuce", 15, 5)
    empty = Plant(None, 3, 4)
    plant_list = [tomato, lettuce, empty]

    print("\nAdding plants to garden...")
    for plant in plant_list:
        try:
            garden.add_plant(plant)
        except AddingPlantError as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    print("Opening watering system")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Error: Cannot Water {e} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    try:
        garden.check_plant_health()
    except HealthError as e:
        print(f"{e}")

    print("\nTesting error recovery...")
    try:
        if garden.tank <= 0:
            raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
