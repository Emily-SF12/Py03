import sys


def str_to_int(score: str) -> int:
    score_int: int = int(score)
    return (score_int)


def print_analytics(scores: list[str], players: int) -> None:
    scores_str: str = ""
    total: int = 0
    average: float = 0
    high: int = 0
    low: int = 0
    range: int = 0
    i: int = 0
    for score in scores[0:]:
        total += str_to_int(score)
        if i == 0:
            high = str_to_int(score)
            low = str_to_int(score)
        else:
            if str_to_int(score) > high:
                high = str_to_int(score)
            if str_to_int(score) < low:
                low = str_to_int(score)
        i += 1
    average = float(total) / float(players)
    range = high - low
    for score in scores[0:]:
        if scores_str == "":
            scores_str = score
        else:
            scores_str = scores_str + ", " + score
    print(f"Scores processed: [{scores_str}]")
    print(f"Total players: {players}")
    print(f"Total score: {total}")
    print(f"Average score: {average:.1f}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {range}")


def score_list(scores: list[str]) -> None:
    validated_scores: list[str] = []
    i: int = 0
    for score in scores[1:]:
        try:
            str_to_int(score)
            validated_scores.append(score)
            i += 1
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    if len(validated_scores) == 0:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        print_analytics(validated_scores, i)


def main() -> None:
    args = sys.argv
    print("=== Player Score Analytics ===")
    score_list(args)
    print()


if __name__ == "__main__":
    main()
