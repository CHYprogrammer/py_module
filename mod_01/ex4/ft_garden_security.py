#!/usr/bin/env python3

class SecurePlant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def set_name(self, name: str) -> None:
        self.__name = name
        print(f"Plant created: {name}")

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negatvie height rejected")
            return

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negatvie age rejected")
            return

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


if __name__ == "__main__":
    print("=== Garden Security System ==")
    rose = SecurePlant("Rose", 25, 30)
    print()
    rose.set_height(-5)
    print()
    rose.set_age(-10)
    print()
    print(f"Current plant: {rose.get_info()}")
