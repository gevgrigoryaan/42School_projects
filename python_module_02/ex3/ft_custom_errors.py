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


def test_water(water: float) -> None:
    if water < 1:
        raise WaterError("Not enough water in the tank!")
    print("Water is OK!")


def test_plant(moizture: float) -> None:
    if moizture < 1:
        raise PlantError("The tomato plant is wilting!")
    print("Plant is OK!")


def test_garden(g):
    if g < 1:
        raise GardenError()


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    try:
        print("\nTesting PlantError...")
        test_plant(0)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("\nTesting WaterError...")
        test_water(0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    try:
        exceptions: list[Exception] = []
        print("\nTesting all garden errors...")

        try:
            test_plant(0)
        except PlantError as e:
            exceptions += [e]
        try:
            test_water(0)
        except WaterError as e:
            exceptions += [e]

        if len(exceptions) > 0:
            raise GardenError(*exceptions)
    except GardenError as e:
        for exception in e.args:
            print(f"Caught GardenError: {exception}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
