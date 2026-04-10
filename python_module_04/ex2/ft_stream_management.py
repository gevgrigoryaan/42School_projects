import sys
import typing


def read_file(file_path: str) -> str:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file'{file_path}'")
    f: typing.IO
    content: str = ""
    try:
        f = open(file_path)
        print("---\n")
        content = f.read()
        print(content, end="")
        print("\n---")
        f.close()
        print(f"File '{file_path}' closed.")
    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR] Error opening file'{file_path}': {e}\n")
        sys.stderr.flush()
    except PermissionError as e:
        sys.stderr.write(f"[STDERR] Error opening file'{file_path}': {e}\n")
        sys.stderr.flush()
    return content


def modify_content(content: str) -> str:
    print("\nTransform data:")
    print("---\n")
    lines = content.splitlines()
    new_content: str = ""
    for line in lines:
        new_line = line + "#"
        print(new_line)
        new_content += new_line + "\n"
    print("\n---")
    return new_content


def save_file(new_content: str) -> None:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file: str = sys.stdin.readline().rstrip("\n")
    if new_file == "":
        print("Not saving data.")
        return
    print(f"Saving data to'{new_file}'")
    try:
        f: typing.IO = open(new_file, 'w')
        f.write(new_content)
        f.close()
        print(f"Data saved in file '{new_file}'.")
    except PermissionError as e:
        sys.stderr.write(f"[STDERR] Error opening file'{new_file}': {e}\n")
        sys.stderr.flush()
        print("Data not saved.")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_stream_management.py <file>")
        return

    content: str = read_file(sys.argv[1])
    if content == "":
        return
    new_content: str = modify_content(content)
    save_file(new_content)


if __name__ == "__main__":
    main()
