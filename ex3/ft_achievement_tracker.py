import random


def gen_player_achievments(achievments: list[str]) -> set[str]:
    i: int = random.randint(3, 6)
    return set(random.sample(achievments, i))


def main() -> None:
    achievments: list[str] = ["Crafting Genius", "World Savior",
                              "Master Explorer", "Collector Supreme",
                              "Untouchable", "Boss Slayer",
                              "Strategist", "Unstoppable",
                              "Speed Runner", "Survivor",
                              "Treasure Hunter", "First Steps",
                              "Sharp Mind", "Hidden Path Finder"]
    all_skills: set[str] = set(achievments)
    players: dict[str, set[str]] = {
        "Alice": gen_player_achievments(achievments),
        "Bob": gen_player_achievments(achievments),
        "Charlie": gen_player_achievments(achievments),
        "Dylan": gen_player_achievments(achievments)}
    print("=== Achievement Tracker System ===\n")
    for name, skills in players.items():
        print(f"Player {name}: {skills}")
    distinct: set[str] = set()
    for skills in players.values():
        distinct = distinct | skills
    print(f"\nAll distinct achievments: {distinct}")
    common: set[str] = distinct
    for skills in players.values():
        common = common & skills
    print(f"\nCommon achievments: {common}\n")
    for player, player_skills in players.items():
        others: set[str] = set()
        for other_players, other_skills in players.items():
            if other_players != player:
                others = others | other_skills
        print(f"Only {player} has: {player_skills - others}")
    print()
    for player, player_skills in players.items():
        print(f"{player} is missing: {all_skills - player_skills}")


if __name__ == "__main__":
    main()
