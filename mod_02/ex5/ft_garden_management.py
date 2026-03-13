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
        self.plants: list[Plant] = []
        self.tank = water

    def add_plant(self, plant: Plant) -> None:
        try:
            if not plant.name:
                raise AddingPlantError("Plant name cannot be empty!")
            print(f"Added {plant.name} successfully")
            self.plants += [plant]
        except AddingPlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if not plant.name:
                    raise WaterError("None")
                print(f"Watering {plant.name} - success")
                self.tank -= 1
        except WaterError as e:
            print(f"Error: Cannot Water {e} - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        try:
            for plant in self.plants:
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
                else:
                    print(f"{plant.name}: healthy "
                          + f"(water: {plant.water}, sun: {plant.sun})")
        except HealthError as e:
            print(f"{e}")


def test_garden_management() -> None:
    print("=== Garden Management System ===")

    water_amount = 1
    garden = GardenManager(water_amount)
    tomato = Plant("tomato", water=5, sun=8)
    lettuce = Plant("lettuce", water=15, sun=5)
    empty = Plant(None, water=3, sun=4)
    plant_list = [tomato, lettuce, empty]

    print("\nAdding plants to garden...")
    for plant in plant_list:
        garden.add_plant(plant)

    print("\nWatering plants...")
    garden.water_plants()

    print("\nChecking plant health...")
    garden.check_plant_health()

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
