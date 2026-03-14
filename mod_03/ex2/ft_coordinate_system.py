#!/usr/bin/env python3

import math
import sys


def create_position(x: int, y: int, z: int) -> tuple:
    return int(x), int(y), int(z)


def calc_distance(pos1: tuple, pos2: tuple) -> float:
    # unpacking
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def parse_coordinate(coord_string: str) -> tuple:
    try:
        if ',' in coord_string:
            parts = coord_string.split(',')
        elif ' ' in coord_string:
            parts = coord_string.split(' ')
        x, y, z = int(parts[0]), int(parts[1]), int(parts[2])
        return tuple([x, y, z])
    except ValueError as e:
        print(f"Error parsing coodinates: {e}")
        print(f"Error - datails - Type: ValueError, Args: ({e})")
        return ()


def trace_example() -> None:
    pos1 = create_position(10, 20, 5)
    print(f"\nPosition created: {pos1}")
    origin = (0, 0, 0)
    distance1 = calc_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {distance1:.2f}")

    coord_str = "3, 4, 0"
    print(f'\nParsing coordinates: "{coord_str}"')
    pos2 = parse_coordinate(coord_str)
    if pos2:
        print(f"Parsed position: {pos2}")
        distance2 = calc_distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {distance2}")

    invalid_str = "abc, def, ghi"
    print(f'\nParsing invalid coordinates: "{invalid_str}"')
    parse_coordinate(invalid_str)

    # Unpacking demonstration
    print("\nUnpacking demonstration:")
    x, y, z = pos2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def valid_three_numbers_case() -> None:
    arg_lst = []
    for arg in sys.argv[1:]:
        try:
            tmp = int(arg)
            arg_lst += [tmp]
        except ValueError:
            print("Please enter three numbers: x, y, and z")
            return None
    coord = tuple(arg_lst)
    x, y, z = coord
    create_position(x, y, z)
    print(f"\nPosition created: {coord}")
    origin = (0, 0, 0)
    dist = calc_distance(origin, coord)
    print(f"Distance between {origin} and {coord}: {dist}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    argc = 0
    for _ in sys.argv:
        argc += 1
    if argc == 1:
        trace_example()
    elif argc == 2:
        coord = parse_coordinate(sys.argv[1])
        if coord:
            print(f"\nParsed position: {coord}")
            origin = (0, 0, 0)
            dist = calc_distance(origin, coord)
            print(f"Distance between {origin} and {coord}: {dist}")
    elif argc == 4:
        valid_three_numbers_case()
    else:
        print("Oops! you should enter valid three numbers or a string.")
