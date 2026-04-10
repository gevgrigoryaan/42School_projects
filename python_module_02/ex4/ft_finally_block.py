class GardenError(Exception):
    """ Basic error for garden problems """
    pass


class PlantError(GardenError):
    """ Problems with plants """
    def __init__(self, error_message: str = "Unknown plant error") -> None:
        self.error_message = error_message
        # super().__init__(error_message)

    def __str__(self) -> str:
        return self.error_message


class WaterError(GardenError):
    """ Problems with water """
    def __init__(self, error_message: str = "Unknown watering error") -> None:
        self.error_message = error_message
        # super().__init__(error_message)

    def __str__(self) -> str:
        return self.error_message


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    try:
        plants = ["Tomato", "lettuce", "Carrots"]
        print("Testing valid plants...")
        print("Opening watering system")
        for plant in plants:
            water_plant(str.capitalize(plant))
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")

    try:
        plants = ["Tomato", "lettuce", "Carrots"]
        print("Testing valid plants...")
        print("Opening watering system")
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
