class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self._name = name
        self._growth = growth
        self._total_growth = 0.
        self._stats = self.Stats()
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
        self._stats._shows += 1

    def grow(self, days: int = 1) -> None:
        self._height += self._growth * days
        self._total_growth = self._growth * days
        self._stats._grows += 1

    def age(self, days: int = 1) -> None:
        self._cur_age += days
        self._stats._ages += 1

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

    @staticmethod
    def year_old(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0., 0, 0.)

    class Stats:
        def __init__(self) -> None:
            self._grows = 0
            self._ages = 0
            self._shows = 0

    def show_stats(self) -> None:
        print(f"[statistics for {self._name}]")
        print(f"Stats: {self._stats._grows} grows,",
              f"{self._stats._ages} age, {self._stats._shows} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, cur_age: int,
                 color: str, growth: float = 0.,
                 has_bloom: bool = False) -> None:

        super().__init__(name, height, cur_age, growth)
        self._color = color
        self._has_bloom = has_bloom

    def bloom_simple(self) -> None:
        self._in_bloom = True

    def bloom(self) -> None:
        self.bloom_simple()
        print(f"[asking the {self._name.lower()} to bloom]")

    def grow_and_bloom(self, days: int = 1) -> None:
        self.grow(days)
        self.bloom_simple()
        print(f"[asking the {self._name.lower()} to grow and bloom]")

    def grow_age_bloom(self, days: int = 1) -> None:
        self.grow()
        self.age(days)
        self.bloom_simple()
        print(f"[make {self._name.lower()} grow, age and bloom]")

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._has_bloom:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, curr_age: int,
                 color: str, growth: float = 0., in_bloom: bool = False,
                 seeds: int = 0, seeds_per_bloom: int = 0) -> None:
        super().__init__(name, height, curr_age, color, growth, in_bloom)
        self._seeds = seeds
        self._seeds_per_bloom = seeds_per_bloom

    def bloom_simple(self) -> None:
        super().bloom_simple()
        self._seeds += self._seeds_per_bloom

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


class Tree(Plant):
    _stats: "Stats"

    def __init__(self, name: str, height: float, cur_age: int,
                 trunk_diameter: float, growth: float = 0.) -> None:
        super().__init__(name, height, cur_age, growth)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shades = 0

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name.capitalize()} now produces a shade",
              f"of {self._height:.1f}cm long",
              f"and {self._trunk_diameter:.1f} cm wide.")
        self._stats._shades += 1

    def show_stats(self) -> None:
        super().show_stats()
        print(f" {self._stats._shades} shade")


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

    def age(self, days: int = 1) -> None:
        super().age(days)

    def grow_and_age(self, days: int = 1) -> None:
        self.grow(days)
        self.age(days)
        print(f"[make {self._name} grow and age for {days} days]")


def show_stats(plant: Plant) -> None:
    plant.show_stats()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.year_old(400)}")
    print("\n=== Flower")
    rose = Flower(name="rose", height=15., cur_age=10, color="red", growth=8.)
    rose.show()
    rose.show_stats()
    rose.grow_and_bloom()
    rose.show()
    rose.show_stats()
    print("\n=== Tree")
    oak = Tree("oak", 200., 365, 5.)
    oak.show()
    oak.show_stats()
    oak.produce_shade()
    oak.show_stats()
    print("\n=== Seed")
    sunflower_seed = Seed("sunflower", 80., 45, "yellow", 30., False,
                          12, 10)
    sunflower_seed.show()
    sunflower_seed.grow_age_bloom(days=20)
    sunflower_seed.show()
    sunflower_seed.show_stats()
    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    anonymous.show_stats()


if __name__ == "__main__":
    main()
