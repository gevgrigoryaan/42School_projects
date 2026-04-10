def garden_operations(operation_number: int) -> int:
    if operation_number == 0:
        return int('abc')
    elif operation_number == 1:
        return 0/0
    elif operation_number == 2:
        return open("abc")
    elif operation_number == 3:
        return "abc" + 1
    else:
        return operation_number


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    test_ops = [0, 1, 2, 3, 4]
    for op in test_ops:
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"aught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
