import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    scores = []

    for i in range(1, argc):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter:'{sys.argv[i]}'")
            i += 1

    real_argc = len(scores)

    if real_argc < 2:
        print("No scores provided. Usage:"
              " python3 ft_score_analytics.py <score1> <score2> ...")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {real_argc}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / (real_argc)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
