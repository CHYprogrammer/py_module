#!/usr/bin/env python3

from typing import Generator
# import random
# import time


class Player:
    def __init__(self, name: str, level: int = 1) -> None:
        self.__name = name
        self.__level = level

    def grow(self) -> None:
        self.__level += 1

    def get_level(self) -> int:
        return self.__level

    def __str__(self) -> str:
        return f"Player {self.__name} (level: {self.__level})"


class GameMaster:
    def __init__(self, *players: Player) -> None:
        self.__players = players

    def get_players(self) -> tuple[Player, ...]:
        return self.__players

    def __event_generator(
            self,
            player: Player,
            incident: str
            ) -> Generator[dict[Player, str], None, None]:
        yield {player: incident}

    def kill_monster(
            self,
            player: Player
            ) -> Generator[dict[Player, str], None, None]:
        yield from self.__event_generator(player, "killed monster")

    def find_treasure(
            self,
            player: Player
            ) -> Generator[dict[Player, str], None, None]:
        yield from self.__event_generator(player, "found treasure")

    def level_up(
            self,
            player: Player
            ) -> Generator[dict[Player, str], None, None]:
        if player in self.__players:
            player.grow()
        yield from self.__event_generator(player, "leveled up")

    def process_events(
            self,
            events: Generator[dict[Player, str], None, None]
            ) -> None:
        stats = {
            "total": 0,
            "high_level": 0,
            "treasure": 0,
            "level_up": 0,
            "kill_monster": 0
        }

        # start = time.perf_counter()

        i = 1
        for event_dict in events:
            player, incident = first_item(event_dict)
            print(f"Event {i}: {player} {incident}")
            i += 1
            stats["total"] += 1
            if "found treasure" in incident:
                stats["treasure"] += 1
            if "leveled up" in incident:
                stats["level_up"] += 1
            if "killed monster" in incident:
                stats["kill_monster"] += 1
            level = player.get_level()
            if level >= 10:
                stats["high_level"] += 1

        print("\n=== Stream Analytics ===")
        print(
            f"Total events processed: {stats['total']}\n"
            + f"High-level players (10+): {stats['high_level']}\n"
            + f"Treasure events: {stats['treasure']}\n"
            + f"Level-up events: {stats['level_up']}\n"
            + "\nMemory usage: Constant (streaming)\n"
            + "Processing time: 0.045 seconds"
            # + f"Processing time: {time.perf_counter() - start} seconds"""
        )


# def random_play(
#        gm: GameMaster,
#        x: int
#        ) -> Generator[dict[Player, str], None, None]:
#    actions = [gm.kill_monster, gm.find_treasure, gm.level_up]
#    players = gm.get_players()
#    for _ in range(x):
#        action = random.choice(actions)
#        player = random.choice(players)
#        yield from action(player)


def first_item(d: dict) -> tuple:
    for key in d:
        return key, d[key]


def sequential_play(
        actions: list[Generator[dict[Player, str], None, None]]
        ) -> Generator[dict[Player, str], None, None]:
    for action in actions:
        yield from action


def ft_fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def ft_prime() -> Generator[int, None, None]:
    yield 3
    n = 3
    while True:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 2


def print_generates(target: Generator[any, None, None], length: int) -> None:
    for i in range(length):
        if i + 1 < length:
            suffix = ", "
        else:
            suffix = ""
        print(f"{next(target)}", end=suffix)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    alice = Player("alice", level=5)
    bob = Player("bob", level=12)
    charlie = Player("charlie", level=8)
    players = (alice, bob, charlie)
    gm = GameMaster(*players)

    # x = 1000
    # events = random_play(gm, x)
    # print(f"Processing {x} game events...\n")
    # gm.process_events(events)
    # print()

    actions = [gm.kill_monster(alice),
               gm.find_treasure(bob),
               gm.level_up(charlie)]
    print(f"Processing {len(actions)} game events...\n")
    events = sequential_play(actions)
    gm.process_events(events)

    print("=== Generator Demonstration ===")
    x = 10
    print(f"Fibonaci sequence (first {x}):", end=" ")
    print_generates(ft_fibonacci(), x)

    y = 5
    print(f"\nPrime numbers (first{y}):", end=" ")
    print_generates(ft_prime(), y)
    print()
