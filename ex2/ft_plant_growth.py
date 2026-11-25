class Plant:
    def __init__(self: Plant, name: str, height: float, age_: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_ = age_

    def grow(self: Plant) -> None:
        self.height = round((self.height + 0.8), 1)

    def age(self: Plant) -> None:
        self.age_ = self.age_ + 1

    def show(self: Plant) -> None:
        print(f"{self.name}:  {self.height}cm, {self.age_} days old")


if __name__ == "__main__":
    total: float = 0
    rose = Plant("rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
for i in range(1, 8):
    print(f"=== Day {i} ===")
    rose.grow()
    rose.age()
    rose.show()
    total = total + 0.8
print("Growth this week:", total)
