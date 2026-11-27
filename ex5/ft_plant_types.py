class Plant:
    def __init__(self: Plant, name: str, height: float, age_: int) -> None:
        self.name = name.capitalize()
        if height >= 0:
            self._height = height
        else:
            self._height = 0

        if age_ >= 0:
            self._age_ = age_
        else:
            self._age_ = 0

    def grow(self: Plant) -> None:
        self._height = round((self._height + 10), 1)
        print(f"Height updated: {self._height:g}cm")

    def age(self: Plant) -> None:
        self._age_ = self._age_ + 20
        print(f"Age updated:  {self._age_} days")

    def set_height(self: Plant, heightt: float) -> None:
        if heightt >= 0:
            self._height = heightt
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self: Plant, agee: int) -> None:
        if agee >= 0:
            self._age_ = agee
        else:
            print(f"{self.name}:   Error, age can’t be negative")
            print("Age update rejected")

    def get_height(self: Plant) -> float:
        return self._height

    def get_age(self: Plant) -> int:
        return self._age_

    def show(self: Plant) -> None:
        print(f"{self.name}:  {self._height}cm, {self._age_} days old")


class Flower(Plant):
    def __init__(self: Flower, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.blooming: bool = False

    def bloom(self) -> None:
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color:  {self.color}")
        if self.blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self: Tree,
                 name: str,
                 height: float,
                 age: int,
                 trunk_diameter: float
                 ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print("Tree Oak now produces a shade of ", end="")
        print(f"{self._height}cm long", end=" ")
        print(f"and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter:  {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 harvest_season: str
                 ):
        super().__init__(name, height, age)
        self.nutritional_value: int = 0
        self.harvest_season = harvest_season

    def age(self) -> None:
        self._age_ += 20
        self.nutritional_value += 10

    def grow(self) -> None:
        self._height += 42
        self.nutritional_value += 10

    def show(self) -> None:
        super().show()
        print(f"Harvest season:  {self.harvest_season}")
        print(f"Nutritional value:  {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    oak = Tree("oak", 200.0, 365, 5.0)
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print()
    print("=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.age()
    tomato.grow()
    tomato.show()
