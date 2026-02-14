#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, old: int) -> None:
        self.name = name
        self.height = height
        self.old = old

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.old} days old"

    def get_info(self) -> None:
        print(self)

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.old += 1


def simulate_a_week(plant: Plant) -> None:
    print("=== Day 1 ===")
    plant.get_info()
    for _ in range(6):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    plant.get_info()


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    simulate_a_week(rose)
