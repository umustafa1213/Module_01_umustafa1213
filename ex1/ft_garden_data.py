class Plant:
    def __init__(self, name: str, height: float, cur_age: int) -> None:
        self.name = name
        self.height = height
        self.cur_age = cur_age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height:.1f}cm, {self.cur_age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    tantalines = Plant("Tantaline", 30, 20)
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    tantalines.show()
