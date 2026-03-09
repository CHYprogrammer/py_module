#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc <= 1:
        print("No arguments provided!")
        print("Program name: " + sys.argv[0])
    else:
        print("Program name: " + sys.argv[0])
        print("Arguments received: " + str(argc - 1))
        count = 1
        for argv in sys.argv[1:]:
            print(f"Argument {count}: {argv}")
    print("Total arguments: " + str(argc))
