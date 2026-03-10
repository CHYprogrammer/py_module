#!/usr/bin/env python3

from typing import Generator


class Player:
    def __init__(self, name: str, level: int = 1) -> None:
        self.__name = name
        self.__level = level

    def grow(self) -> None:
        self.__level += 1

    def __str__(self) -> str:
        return f"Player {self.__name} (level: {self.__level})"


class GameMaster:
    def __init__(self, *players: Player) -> None:
        self.__players = players
        self.__events = []

    def add_event(self, event: str) -> None:
        self.__events += [event]

    def kill_monster(self, *players: Player) -> None:
        for player in players:
            if player in self.__players:
                self.add_event(f"{player} killed monster")

    def find_treasure(self, *players: Player) -> None:
        for player in players:
            if player in self.__players:
                self.add_event(f"{player} found treasure")

    def level_up(self, *players: Player) -> None:
        for player in players:
            if player in self.__players:
                player.grow()
                self.add_event(f"{player} leveled up")

    def get_event(self) -> Generator[str, None, None]:
        for event in self.__events:
            yield event

    def show_events(self, x: int) -> None:
        print(f"Processing {x} game events...\n")
        try:
            if x < 0:
                raise ValueError("*** 'x' must be integer ***\n")
            events = self.get_event()
            for count in range(x):
                event = next(events)
                print(f"Event {count + 1}: {event}")
        except StopIteration:
            print()
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

        try:
            next(events)
            print("...\n")
        except StopIteration:
            print()


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    alice = Player("alice", 5)
    bob = Player("bob", 12)
    charlie = Player("charlie", 7)
    game = GameMaster(alice, bob, charlie)

    game.kill_monster(alice)
    game.find_treasure(bob)
    game.level_up(charlie)
    game.kill_monster(bob)

    game.show_events(-3)
    game.show_events(5)

    print("=== Stream Analytics ===")
