import sys
import typing


def main() -> None:
    argc = len(sys.argv)

    if argc < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_path = sys.argv[1]

    print(f"=== Cyber Archives Recovery ==="
          f"\nAccessing file '{file_path}'")

    f: typing.IO
    try:
        f = open(file_path)
        print("---\n")
        print(f.read(), end="")
        print("---")
        f.close()
        print(f"File '{file_path}' closed")
    except FileNotFoundError as e:
        print(f"Error opening file '{file_path}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{file_path}': {e}")


if __name__ == "__main__":
    main()
