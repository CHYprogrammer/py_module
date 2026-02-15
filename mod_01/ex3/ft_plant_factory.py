#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.old = age

    def grow(self, count: int = 1) -> None:
        self.height += count

    def age(self, count: int = 1) -> None:
        self.old += count

    def get_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.old} days)"


def ft_plant_factory(*plants: Plant) -> None:
    count = 0
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.get_info()}")
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
