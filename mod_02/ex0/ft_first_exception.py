#!/usr/bin/env python3

class TemperatureError(Exception):
    pass


def check_temperature(temp_str: str) -> int:
    print(f"\nTesting temperature: {temp_str}")
    try:
        temp = int(temp_str)
        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
        elif temp > 40:
            raise TemperatureError(
                f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            raise TemperatureError(
                f"Error: {temp}°C is too cold for plants (min 0°C)")
    except TemperatureError as e:
        print(e)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-50"]
    for temp_str in tests:
        check_temperature(temp_str)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
