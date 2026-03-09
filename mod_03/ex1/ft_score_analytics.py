#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    if argc <= 1:
        print("No scores provided. "
              + "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores = []
        for arg in sys.argv[1:]:
            try:
                score = int(arg)
                scores += [score]
            except ValueError as e:
                print(f"******\nPlease input a number!\nProblem: {e}\n******")
                break
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"Hight score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
