class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.flag = False

    def bloom(self):
        self.flag = True

    def get_info(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")
        if not self.flag:
            print(f"{self.name} have not bloomed yet")
        else:
            print(f"{self.name} is blooming beatifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.diameter = diameter
        self.shade = 0

    def produce_shade(self, shade: int):
        self.shade = shade

    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.diameter}cm diameter")
        if not self.shade:
            print(f"{self.name} provides no shade")
        else:
            print(f"{self.name} provides {self.shade} square meters of shade")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutrition: str = ""
          ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrition = nutrition

    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")
        if not self.nutrition:
            print(f"{self.name} has no nutritional value")
        else:
            print(f"{self.name} is rich in {self.nutrition}")


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "Vitamin C")

    rose.bloom()
    oak.produce_shade(78)

    print("=== Garden Plant Types ===\n")
    rose.get_info()
    print()
    oak.get_info()
    print()
    tomato.get_info()
