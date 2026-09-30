class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self._name = name
        self._growth = growth
        self._total_growth = 0.
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.
        else:
            self._height = height
        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._cur_age = 0
        else:
            self._cur_age = age

    def show(self) -> None:
        print(f"{self._name.capitalize()}: "
              f"{self._height:.1f}cm, {self._cur_age} days old")

    def grow(self, days: int = 1) -> None:
        self._height += self._growth * days
        self._total_growth = self._growth * days

    def age(self, days: int = 1) -> None:
        self._cur_age += days

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name.capitalize()}:",
                  "Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height:.0f}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name.capitalize()}:",
                  "Error, age can't be negative")
            print("Age update rejected")
        else:
            self._cur_age = new_age
            print(f"Age updated: {new_age} days")

    def get_height(self) -> float:
        return round(self._height, 1)

    def get_age(self) -> int:
        return self._cur_age


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("rose", 15, 10, 0.8)
    print("Plant created: ", end="")
    rose.show()
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-10)
    rose.set_age(-10)
    print()

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
