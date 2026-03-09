#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__status = False

    def get_status(self) -> bool:
        return self.__status

    def water(self) -> None:
        self.__status = True

    def __str__(self) -> str:
        return self.name


class Garden:
    def __init__(self, water_tank: int, *plants: Plant) -> None:
        self.water_tank = water_tank
        self.plants = plants

    def water_all(self) -> None:
        for plant in self.plants:
            plant.water()
            self.water_tank -= 0

    def __str__(self) -> str:
        plants = [str(plant) for plant in self.plants]
        return f"water tank: {self.water_tank}\nplants: {plants}"


class GardenError(Exception):
    def __init__(self, message: str = "") -> None:
        super().__init__(self)
        self.message = message

    def __str__(self) -> str:
        return str(self.message)


class PlantError(GardenError):
    def __init__(self, plant: Plant = None) -> None:
        super().__init__(self)
        self.plant = plant

    def __str__(self) -> str:
        return f"The {self.plant} plant is wilting!"


class WaterError(GardenError):
    def __init__(self) -> None:
        super().__init__(self)

    def __str__(self) -> str:
        return "Not enough water in the tank!"


def test_plant_error(plant: Plant):
    if plant.get_status():
        print(f"The {plant} plant is fine.")
    else:
        raise PlantError(plant)


def test_water_error(water_tank: int):
    if water_tank <= 0:
        raise WaterError
    else:
        print("Enough water in the tank.")


def test_garden_error(garden: Garden):
    errors = []
    for plant in garden.plants:
        try:
            test_plant_error(plant)
        except GardenError as e:
            errors += [e]
    try:
        test_water_error(garden.water_tank)
    except GardenError as e:
        errors += [e]
    if errors:
        for error in errors:
            print(f"Caught a garden error: {error}")


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        tomato = Plant("tomato")
        # tomato.water()
        test_plant_error(tomato)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    except Exception as e:
        print(f"Unexpected error occured: {e}")

    print("\nTesting WaterError...")
    try:
        water_tank = 0
        test_water_error(water_tank)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    except Exception as e:
        print(f"Unexpected error occured: {e}")

    print("\nTesting catching all garden errors...")
    garden = Garden(water_tank, tomato)
    try:
        test_garden_error(garden)
    except Exception as e:
        print(f"Unexpected error occured: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
