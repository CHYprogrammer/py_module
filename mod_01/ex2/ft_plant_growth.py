class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, days: int = 1) -> None:
        self.height += days

    def age(self, days: int = 1) -> None:
        self.age += days

    def update(self, days: int = 1) -> None:
        self.height += days
        self.age += days


def observation_growth(plant: Plant, days: int) -> None:
    print("=== Day 1 ===")
    plant.get_info()
    initial_height = plant.height
    for _ in range(days - 1):
        plant.update()
    print(f"=== Day {days} ===")
    plant.get_info()
    growth = plant.height - initial_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    observation_growth(rose, 7)
