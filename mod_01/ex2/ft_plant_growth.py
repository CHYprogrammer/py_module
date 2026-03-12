#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, old: int) -> None:
        self.name = name
        self.height = height
        self.old = old

    def grow(self, count: int = 1) -> None:
        self.height += count

    def age(self, count: int = 1) -> None:
        self.old += count

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.old} days old"


def simulate_a_week(plant: Plant, days: int) -> None:
    print("=== Day 1 ===")
    print(plant.get_info())
    for _ in range(days - 1):
        plant.grow()
        plant.age()
    print(f"=== Day {days} ===")
    print(plant.get_info())
    print(f"Growth this week: +{days - 1}cm")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    simulate_a_week(rose, 7)
