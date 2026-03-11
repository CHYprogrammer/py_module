#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount: int = 1) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(
        self, name: str, height: int, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = True

    def get_info(self) -> str:
        state = "blooming" if self.is_blooming else "not blooming"
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers ({state})"
        )


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, Prize points: {self.prize_points}"


class GardenManager:
    _total_gardens = 0

    class GardenStats:
        @staticmethod
        def total_height(plants: list[Plant]) -> int:
            total = 0
            for plant in plants:
                total += plant.height
            return total

        @staticmethod
        def count_by_type(plants: list) -> dict:
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in plants:
                plant_type = type(plant)
                if plant_type is PrizeFlower:
                    counts["prize"] += 1
                elif plant_type is FloweringPlant:
                    counts["flowering"] += 1
                else:
                    counts["regular"] += 1
            return counts

        @staticmethod
        def garden_score(plants: list[Plant]) -> int:
            total_height = 0
            for plant in plants:
                total_height += plant.height
            return total_height

        @staticmethod
        def validate_height(plants: list) -> int:
            return all(plant.height >= 0 for plant in plants)

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        self._growth_count = 0
        GardenManager._total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)
        self._growth_count += len(self.plants)

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"  - {plant.get_info()}")
        counts = self.stats.count_by_type(self.plants)
        print(
            f"\nPlants added: {len(self.plants)}, "
            f"Total growth: {self._growth_count}cm"
        )
        print(
            f"Plant types: {counts['regular']} regular, "
            f"{counts['flowering']} flowering, "
            f"{counts['prize']} prize flowers"
        )

    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        return [cls(owner) for owner in owners]

    @classmethod
    def total_gardens_managed(cls) -> int:
        return cls._total_gardens


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")

    oak = Plant("Oak Tree", 100, 1825)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    print()
    alice.grow_all()

    alice.report()

    print(
        f"\nHeight validation test: "
        f"{GardenManager.GardenStats.validate_height(alice.plants)}"
    )
    bob = GardenManager("Bob")
    bob.add_plant(Plant("Cacutus", 50, 90))
    bob.add_plant(Plant("Fern", 22, 60))
    alice_score = alice.stats.garden_score(alice.plants)
    bob_score = bob.stats.garden_score(bob.plants)
    print(f"Garden Scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total garden managed: {GardenManager._total_gardens}")
