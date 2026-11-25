class Plant:
    def __init__(self: Plant, name: str, height: float, age_: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_ = age_

    def show(self: Plant) -> None:
        print(f"{self.name}:  {self.height}cm, {self.age_} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)

    rose.show()
    sunflower.show()
    cactus.show()
