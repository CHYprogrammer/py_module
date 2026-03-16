#!/usr/bin/env python3

import sys
# from typing import TextIO


# def ft_input(prompt: str = "") -> str:
#    if prompt:
#        sys.stdout.write(prompt)
#        sys.stdout.flush()

#    line = sys.stdin.readline()
#    if not line:
#        raise EOFError
#    return line.rstrip("\n")


# def ft_print(
#        prompt: str = "",
#        end: str = "\n",
#        file: TextIO = sys.stdout
#        ) -> None:
#    file.write(prompt + end)
#    file.flush()


def communication_system() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream astive. Enter status report: ")

    print("\n[STANDARD] Archive status from "
          f"{archivist_id}: {status_report}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)

    print("\nThree-channel communication test successfull.")


if __name__ == "__main__":
    communication_system()
