def input_temprature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    test = '25'
    print(f"Input data is'{test}'")
    try:
        input_temprature(test)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    else:
        print(f"Temperature is now {test}°C\n")
    test = 'abc'
    print(f"Input data is'{test}'")
    try:
        input_temprature(test)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    else:
        print(f"Temperature is now {test}°C\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
