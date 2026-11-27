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


if __name__ == "__main__":
    rose = Plant("rose", 15.0, 10)
    print("=== Garden Security System ===")

    print("Plant created:", end="  ")
    rose.show()

    rose.grow()
    rose.age()
    print()
    rose.set_height(-10)
    rose.set_age(-5)
    print()
    print("Current state:", end=" ")
    rose.show()
