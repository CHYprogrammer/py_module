class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def grow(self, count: int = 1) -> None:
        self.__height += count

    def age(self, count: int = 1) -> None:
        self.__age += count

    def get_info(self) -> str:
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str
            ) -> None:
        super().__init__(name, height, age)
        self.__color = color
        self.__flag = False

    def bloom(self) -> None:
        self.__flag = True

    def get_info(self) -> str:
        if self.__flag:
            bloom_status = f"{self.get_name()} is blooming beautifully!"
        else:
            bloom_status = f"{self.get_name()} have not bloomed yet"
        return (f"{self.get_name()} (Flower): {self.get_height()}cm, "
                + f"{self.get_age()} days, {self.__color} color\n"
                + bloom_status)


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            diameter: int
            ) -> None:
        super().__init__(name, height, age)
        self.__diameter = diameter
        self.__shade = 0

    def produce_shade(self, shade: int) -> None:
        self.__shade = shade

    def get_info(self) -> str:
        if not self.__shade:
            shade_str = f"{self.get_name()} provides no shade"
        else:
            shade_str = (f"{self.get_name()} provides "
                         + f"{self.__shade} square meters of shade")
        return (f"{self.get_name()} (Tree): {self.get_height()}cm, "
                + f"{self.get_age()} days, {self.__diameter}cm diameter\n"
                + shade_str)


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutrition: str = "nothing"
            ) -> None:
        super().__init__(name, height, age)
        self.__harvest_season = harvest_season
        self.__nutrition = nutrition

    def get_info(self) -> str:
        return (f"{self.get_name()} (Vegetable): {self.get_height()}cm, "
                + f"{self.get_age()} days, {self.__harvest_season} harvest\n"
                + f"{self.get_name()} is rich in {self.__nutrition}")


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "Vitamin C")
    sunflower = Flower("Sunflower", 50, 35, "yellow")
    pine = Tree("Pine", 3000, 3650, 200)
    broccoli = Vegetable("Broccoli", 40, 70, "autumn", "folate")

    rose.bloom()
    oak.produce_shade(78)

    print("=== Garden Plant Types ===")
    for plant in [rose, oak, tomato, sunflower, pine, broccoli]:
        print()
        print(plant.get_info())
