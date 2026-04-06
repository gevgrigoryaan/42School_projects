class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._init_height = 15.0
        self._height = 15.0
        self._age_of_plant = 10

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

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_of_plant

    def grow(self, length: float) -> None:
        self._height = round(self._height + length, 1)

    def age(self, days: int = 1) -> None:
        self._age_of_plant += days


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 trunk_diameter: float
                 ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"[asking the {self._name} to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 harvest_season: str,
                 nutritional_value: int = 0
                 ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self, amount: float = 2.1):
        super().grow(amount)
        self.nutritional_value += 1

    def age(self, days: int = 1):
        super().age(days)
        self.nutritional_value += days - 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    ros.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    days = 20
    print(f"[make {tomato.get_name()} grow and age for {days} days]")
    tomato.grow(27)
    tomato.age(days)
    tomato.show()


if __name__ == "__main__":
    main()
