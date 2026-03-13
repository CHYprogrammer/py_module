#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


def garden_operations(type: str) -> None:
    violet = Plant("Violet", 15)
    garden = {"existing_plant": violet.name}

    if type == "multiple":
        print("Testing multiple errors together...")
        int(violet.name)
        violet.height / 0
    else:
        print(f"Testing {type}Error...")
        if type == "Value":
            int(violet.name)
        elif type == "ZeroDivision":
            violet.height / 0
        elif type == "FileNotFound":
            f = open("missingt.txt")
            f.close()
        elif type == "Key":
            print(f"{garden['missing_plant']}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    errors = ["Value", "ZeroDivision", "FileNotFound", "Key"]

    # raise single error
    for type in errors:
        try:
            garden_operations(type)
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}\n")
        except KeyError as e:
            print(f"Caught KeyError: {e}\n")

    # raise multiple errors
    try:
        garden_operations("multiple")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
