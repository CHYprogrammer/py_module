#!/usr/bin/env python3

class TemperatureError:
    def __init__(self, error_message: str) -> None:
        try:
            error_message + ""
        except ValueError:
            print(f"{error_message} is invalid as error message.")
            pass
        self.__message = error_message

    def __str__(self) -> str:
        if self.__message:
            return (self.__message)
        return "Error: the temp is outside the safe range for plants (0~40°C)."


def check_temperature(temp_str: str) -> int:
    print(f"\nTesting temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    if 0 <= temp <= 40:
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp
    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-50"]
    for temp in tests:
        check_temperature(temp)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
