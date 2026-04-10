def input_temperature(temp_str: str) -> int:
    """
    Converts a string input to an integer temperature and validates the range.
    
    Args:
        temp_str: A string representing a temperature reading
        
    Returns:
        The temperature as an integer if valid (0-40°C)
        
    Raises:
        ValueError: If the string cannot be converted to an integer or
                   if the temperature is outside the valid range (0-40°C)
    """
    temp = int(temp_str)
    
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    
    return temp


def test_temperature() -> None:
    """
    Tests the input_temperature() function with valid, invalid, and extreme inputs.
    Demonstrates exception handling for type errors and range validation.
    """
    print("=== Garden Temperature Checker ===")
    
    test_cases = ["25", "abc", "100", "-50"]
    
    for test_input in test_cases:
        print(f"Input data is'{test_input}'")
        try:
            temp = input_temperature(test_input)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
