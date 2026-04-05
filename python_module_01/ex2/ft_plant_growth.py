class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.init_height = height
        self.height = height
        self.age_of_plant = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_of_plant} days old")

    def grow(self, length: float) -> None:
        self.height = round(self.height + length, 1)

    def age(self) -> None:
        self.age_of_plant += 1


def main() -> None:
    plant_rose = Plant("Rose", 25, 30)

    print("=== Garden Plant Growth ===")
    plant_rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant_rose.grow(0.8)
        plant_rose.age()
        plant_rose.show()
    final_height = round(plant_rose.height - plant_rose.init_height, 1)
    print(F"Growth this week: {final_height}cm")


if __name__ == "__main__":
    main()
