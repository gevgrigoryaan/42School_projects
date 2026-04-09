import sys
import typing


def ancient_data_recovery() -> bool:
    argc = len(sys.argv)

    if argc < 2:
        print("Usage: ft_ancient_text.py <file>")
        return False

    file_path = sys.argv[1]

    print(f"=== Cyber Archives Recovery & Preservation ==="
          f"\nAccessing file '{file_path}'")

    f: typing.IO
    try:
        f = open(file_path)
        print("---\n")
        print(f.read(), end="")
        print("---")
        f.close()
        print(f"File '{file_path}' closed")
        return True
    except FileNotFoundError as e:
        print(f"Error opening file '{file_path}': {e}")
        return False
    except PermissionError as e:
        print(f"Error opening file '{file_path}': {e}")
        return False


def add_special_character(char: str) -> None:
    print("Transform data:")
    print


if __name__ == "__main__":
    if ancient_data_recovery():
        add_special_character()

