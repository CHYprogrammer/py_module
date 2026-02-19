#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int) -> None:
        self.__name = name
        self.__height = height

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def grow(self, amount: int = 1) -> None:
        self.__height += amount
        print(f"{self.__name} grew {amount}cm")

    def get_info(self) -> str:
        return f"{self.__name}: {self.__height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.__color = color
        self.__state = "not blooming"

    def bloom(self) -> None:
        self.__state = "blooming"

    def get_color(self) -> str:
        return self.__color

    def get_bloom_state(self) -> str:
        return self.__state

    def get_info(self) -> str:
        base = super().get_info()
        return (f"{base},",
                f"{self.__color} flowers",
                f"({self.__state})")


class PrizeFlower(FloweringPlant):
    def __init__(self,
                 name: str,
                 height: int,
                 color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, color)
        self.__prize_points = prize_points

    def get_prize_points(self) -> int:
        return self.__prize_points

    def get_info(self) -> str:
        base = super().get_info()
        return (f"{base}),",
                f"Prize points: {self.__prize_points}")


class Garden:
    def __init__(self, owner: str) -> None:
        self.__owner = owner
        self.__plants = []
        self.grow_count = 0

    def get_owner(self) -> str:
        return self.__owner

    def add_plant(self, plant: Plant) -> None:
        self.__plants += plant
        print(f"Added {plant.get_name()} to {self.__owner}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self.__owner} is helping all plants grow...")
        for plant in self.__plants:
            plant.grow()
        self.grow_count += 1

    def show_report(self) -> None:
        print(f"\n=== {self.__owner}'s Garden Report ===")
        print(f"Plants in garden:")
        for plant in self.__plants:
            print("- " + plant.get_info())
        print()


class GardenManager:
    
    def __init__(self) -> None:
        self.__gardens = []

    def add_garden(self, garden: Garden) -> None:
        self.__gardens.append(garden)

    class GardenStats:
        @staticmethod
        def calculate(garden: Garden) -> None:
            regular_nbr = 0
            flower_nbr = 0
            prize_nbr = 0
            total_plants = 0
            for plant in garden.__plants:
                plant_type = type(plant)
                if plant_type == PrizeFlower:
                    prize_nbr += 1
                elif plant_type == FloweringPlant:
                    flower_nbr += 1
                elif plant_type == Plant:
                    regular_nbr += 1
                total_plants += 1
            total_growth = total_plants * garden.grow_count
            print(f"Plants added: {total_plants}, Total growth: {total_growth}cm")
            print(f"Plant types: {regular_nbr} regular, {flower_nbr} flowering, {prize_nbr} prize flowers")

    def check_height_validate(garden: Garden) ->
