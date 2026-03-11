#!/usr/bin/env python3

class Player:
    def __init__(self,
                 name: str, score: int, status: str,
                 region: str, feats: list[str] = []) -> None:
        self.name = name
        self.score = score
        self.status = status
        self.region = region
        self.feats = feats


if __name__ == "__main__":
    # init Sample Data
    alice = Player("alice", 2300, "active", "north")
    alice.feats = ["first_kill", "boss_slayer", "level_10",
                   "head_shot", "no_damage"]

    bob = Player("bob", 1800, "active", "east")
    bob.feats = ["first_kill", "boss_slayer", "assault"]

    charlie = Player("charlie", 2150, "active", "central")
    charlie.feats = ["hide", "level_10", "speed_run", "treasure_hunter",
                     "seek", "survivor", "stone_actor"]

    diana = Player("diana", 2050, "inactive", "north")
    diana.feats = ["first_kill", "level_10", "boss_slayer", "speed_run"]

    players = [alice, bob, charlie, diana]

    # Comprehension Examples
    print("=== Game Analytic Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    high_scorers = [p.name for p in players if p.score > 2000]
    scores_doubled = [p.score * 2 for p in players]
    active_players = [p.name for p in players if p.status == "active"]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p.name: p.score for p in players}
    feat_counts = {p.name: len(p.feats) for p in players}
    print(f"Player scores: {player_scores}")
    print(f"Achievement counts {feat_counts}")

    print("\n=== Set Comprehension Examples ===")
    game_log = ["alice", "bob", "alice", "charlie", "bob", "diana", "eve"]
    unique_players = {name for name in game_log}
    unique_feats = {feat for p in players for feat in p.feats}
    active_regions = {p.region for p in players}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_feats}")
    print(f"Active regions: {active_players}")

    print("\n=== Combined Analysis ===")
    all_scores = {p.score for p in players}
    all_feats = {a for p in players for a in p.feats}
    name_to_data = {p.name: p for p in players}
    total_players = len(players)
    average_score = sum(all_scores) / total_players
    top = max(players, key=lambda p: (p.score, len(p.feats)))
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(all_feats)}")
    print(f"Average score: {average_score:.1f}")
    print(f"Top performer: {top.name} "
          + f"({top.score} points, {len(top.feats)} achievements)")
