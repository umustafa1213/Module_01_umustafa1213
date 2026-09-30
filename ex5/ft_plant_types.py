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


class Flower(Plant):
    def __init__(self, name: str, height: float, cur_age: int,
                 color: str, growth: float = 0.,
                 has_bloom: bool = False) -> None:

        super().__init__(name, height, cur_age, growth)
        self._color = color
        self._has_bloom = has_bloom

    def bloom(self) -> None:
        self._has_bloom = True
        print(f"[asking the {self._name.lower()} to bloom]")

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._has_bloom:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, cur_age: int,
                 trunk_diameter: float, growth: float = 0.) -> None:
        super().__init__(name, height, cur_age, growth)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name.capitalize()} now produces a shade",
              f"of {self._height:.1f}cm long",
              f"and {self._trunk_diameter:.1f} cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, cur_age: int,
                 harvest_season: str, nutritional_value: int,
                 growth: float = 0.) -> None:
        super().__init__(name, height, cur_age, growth)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self, days: int = 1) -> None:
        super().grow(days)
        self._nutritional_value += days
        print(f"[make {self._name} grow and age for {days} days]")

    def age(self, days: int = 1) -> None:
        super().age(days)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()

    print()
    print("=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    oak.produce_shade()

    print()
    print("=== Vegetable")
    tomato = Vegetable("tomato", 5, 10, "April", 0, 2.1)
    tomato.show()
    tomato.grow(20)
    tomato.age(20)
    tomato.show()
