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


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    lst = [rose, oak, cactus, sunflower, fern]
    count = 0
    print("=== Plant Factory Output ===")
    for plant in lst:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        count += 1
    print()
    print(f"Total plants created: {count}")
