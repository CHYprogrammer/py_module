import sys
sys.path.append("..")
from ex3.ft_plant_factory import Plant

class SecurePlant(Plant):
    def __init__(self, name: str, height: int, age: int):
        super().__init__(name, height, age)
        

    def security(self, value: int)
        print("=== Garden Security System ===")
        print("")
        if value < 0
            raise ValueError("Invalid attempted: height")

    def set_height(self, height):
        
