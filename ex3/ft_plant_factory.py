class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float = 0) -> None:
        self.name = name
        self.height = height
        self.cur_age = age
        self.growth = growth
        self.total_growth = 0.

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height:.1f}cm, {self.cur_age} days old")

    def grow(self, days: int = 1) -> None:
        self.height += self.growth * days
        self.total_growth = self.growth * days

    def age(self, days: int = 1) -> None:
        self.cur_age += days


def main() -> None:
    garden = [
        Plant("rose", 25, 20, 0.8),
        Plant("tantaline", 20, 30, 1.1),
        Plant("peony", 15, 40, 0.2),
        Plant("daisy", 5, 15, 0.1),
        Plant("willow", 11, 20, 0.5)
    ]
    print("=== Plant Factory Output ===")
    for plant in garden:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
