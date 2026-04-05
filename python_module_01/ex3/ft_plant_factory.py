class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.init_height = round(height, 1)
        self.height = round(height, 1)
        self.age_of_plant = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_of_plant} days old")

    def grow(self, length: float) -> None:
        self.height = round(self.height + length, 1)

    def age(self) -> None:
        self.age_of_plant += 1


def main():
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sanflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)
    plants = [plant1, plant2, plant3, plant4, plant5]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
