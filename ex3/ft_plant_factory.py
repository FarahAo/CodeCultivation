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
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    rose_list: list[Plant] = [rose, oak, cactus, sunflower, fern]
    for i in range(0, 5):
        print("Created:", end="  ")
        rose_list[i].show()
