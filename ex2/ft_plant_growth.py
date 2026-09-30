class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
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
        self.total_growth += self.growth * days

    def age(self, days: int = 1) -> None:
        self.cur_age += days


if __name__ == "__main__":
    rose = Plant("rose", 25, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()
    old_height = rose.height
    for i in range(1, 8):
        rose.age(1)
        rose.grow()
        print(f"=== Day {i} ===")
        rose.show()
    print(f"Growth this week: {rose.total_growth:.1f}cm")
