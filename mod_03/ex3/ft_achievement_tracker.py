#!/usr/bin/env python3

def unique_achievements(target: set, *others: set) -> set:
    return target.difference(set.union(*others))


def ahievement_analytics(*players: set) -> None:
    try:
        all = set.union(*players)
        print(f"All unique achievements: {all}")
        print(f"Total unique achievements: {len(all)}\n")
        print(f"Common to all players: {set.intersection(*players)}")

        rare = set()
        for target in players:
            others = [player for player in players if player is not target]
            rare |= unique_achievements(target, *others)
        print(f"Rare achievements (1 player): {rare}\n")
    except Exception as e:
        print(f"\n*******\nError: {e}\n******\n")

        alice_unique = unique_achievements(alice, bob, charlie)
        bob_unique = unique_achievements(bob, alice, charlie)
        charlie_unique = unique_achievements(charlie, alice, bob)
        rare = set.union(alice_unique, bob_unique, charlie_unique)
        print(f"Rare achievements (1 player): {rare}\n")


if __name__ == "__main__":
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice ahievement: {alice}")
    print(f"Player bob ahievement: {bob}")
    print(f"Player charlie ahievement: {charlie}")

    print("\n=== Achievement Analytics ===")
    ahievement_analytics(alice, bob, charlie)

    ab_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {ab_common}")
    print(f"Alice unique: {alice - ab_common}")
    print(f"Bob unique: {bob - ab_common}")
