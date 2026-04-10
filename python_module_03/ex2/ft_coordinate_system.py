import math


def get_player_pos() -> tuple:
    while True:
        try:
            user_input = input("Enter new coordinates"
                               "as floats in format 'x,y,z': ")
            x, y, z = user_input.strip().split(",")
            return (float(x), float(y), float(z))
        except ValueError as e:
            if "could not convert" in str(e):
                # extract the problematic value from the error message
                bad_val = user_input.strip().split(",")
                for v in bad_val:
                    try:
                        float(v.strip())
                    except ValueError:
                        print(f"Error on parameter'{v.strip()}': could not "
                              f"convert string to float:'{v.strip()}'")
                        break
            else:
                print("Invalid syntax")


def calculate_dinstance(r1: tuple, r2: tuple) -> float:
    x1, y1, z1 = r1
    x2, y2, z2 = r2
    dinstance = round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 4)
    return dinstance


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first_coords = get_player_pos()
    print(f"Got a first tuple: {first_coords}")
    print(f"It includes: X={first_coords[0]}, "
          f"Y={first_coords[1]}, Z={first_coords[2]}")
    dinstance_centre = calculate_dinstance((0.0, 0.0, 0.0,), first_coords)
    print(f"Distance to center: {dinstance_centre}")

    print("\nGet a second set of coordinates")
    second_coords = get_player_pos()
    dinstance_between = calculate_dinstance(second_coords, first_coords)
    print(f"Distance between the 2 sets of coordinates: {dinstance_between}")


if __name__ == "__main__":
    main()
