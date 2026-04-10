def secure_archive(file_path: str, mode: str = 'r', src: str = '') -> tuple:
    try:
        with open(file_path, mode) as file:
            if mode == 'w':
                file.write(src)
                buf = 'Content successfully written to file'
            else:
                buf = file.read()
    except FileNotFoundError as e:
        return (False, str(e))
    except PermissionError as e:
        return (False, str(e))
    else:
        return (True, buf)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file', 'r'))

    print("\nUsing'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/shadow', 'r'))

    print("\nUsing'secure_archive' to read from a regular file:")
    tp = secure_archive('ancient_fragment.txt', 'r')
    print(tp)

    print("\nUsing'secure_archive' to write previous content to a new file:")
    print(secure_archive('new_fragment.txt', 'w', tp[1]))


main()
