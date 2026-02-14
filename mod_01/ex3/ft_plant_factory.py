#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_factory(*plants: Plant) -> None:
    count = 0
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        count += 1
    print()
    print(f"Total plants created: {count}")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    ft_plant_factory(rose, oak, cactus, sunflower, fern)
