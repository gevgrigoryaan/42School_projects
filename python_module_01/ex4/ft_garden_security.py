class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._init_height = 15.0
        self._height = 15.0
        self._age_of_plant = 10
        print("Plant created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age_of_plant} days old")

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"\n{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return False
        self._height = round(height, 1)
        print(f"\nHeight updated: {height}cm")
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected\n")
            return False
        self._age_of_plant = age
        print(f"Age updated: {age} days")
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_of_plant

    def grow(self, length: float) -> None:
        self._height = round(self._height + length, 1)

    def age(self) -> None:
        self._age_of_plant += 1


def main() -> None:
    print("=== Garden Security System ===")
    plant_rose = Plant("Rose", 15, 10)
    plant_rose.set_height(25)
    plant_rose.set_age(30)
    plant_rose.set_height(-4)
    plant_rose.set_age(-5)

    print("Current state: ", end="")
    plant_rose.show()


if __name__ == "__main__":
    main()
