import math


def str_to_float(position: str) -> float:
    coord: float = float(position)
    return (coord)


def get_player_pos() -> tuple[float, float, float]:
    position: str = input("Enter new coordinates "
                          "as floats in format 'x,y,z': ")
    spl_position: list[str] = position.split(",")
    coordinates: list[float] = []
    i: int = 0
    if len(spl_position) != 3:
        print("Invalid syntax")
        return (get_player_pos())
    else:
        for coord in spl_position[0:3]:
            spl_position[i] = coord.strip()
            i += 1
        for coords in spl_position[0:3]:
            try:
                coordinates.append(str_to_float(coords))
            except ValueError as error:
                print(f"Error on parameter '{coords}': {error}")
                return (get_player_pos())
    return (coordinates[0], coordinates[1], coordinates[2])


def distance_to_center(coords: tuple[float, float, float]) -> float:
    distance: float = math.sqrt(coords[0]**2 + coords[1]**2 + coords[2]**2)
    return (distance)


def distance_between(coords_a: tuple[float, float, float],
                     coords_b: tuple[float, float, float]) -> float:
    distance: float = math.sqrt((coords_b[0] - coords_a[0])**2 +
                                (coords_b[1] - coords_a[1])**2 +
                                (coords_b[2] - coords_a[2])**2)
    return (distance)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]:.1f}, Y={first[1]:.1f}, Z={first[2]:.1f}")
    print(f"Distance to center: {distance_to_center(first):.4f}")
    print("\nGet a second set of coordinates")
    second: tuple[float, float, float] = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{distance_between(first, second):.4f}")


if __name__ == "__main__":
    main()
