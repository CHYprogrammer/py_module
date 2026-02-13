class SecurePlant():
    def __init__(self, name: str, height: int, age: int):
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def set_name(self, name):
        self.name = name
        print(f"Plant created: {name}")

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negatvie height rejected")
            return
        else:
            self.height = height
            print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negatvie age rejected")
            return
        else:
            self.age = age
            print(f"Age updated: {self.age} days [OK]")

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name} ({self.height} cm, {self.age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ==")
    rose = SecurePlant("Rose", 25, 30)
    print()
    rose.set_height(-5)
    print()
    rose.set_age(-10)
    print()
    print(f"Current plant: {rose}")
