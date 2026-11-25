
class Plant:
    def __init__(self: Plant, name: str, height: float, age_: int) -> None:
        self.name = name.capitalize()
        self._height = height
        self._age_ = age_


    def set_height(self) -> None:
        if height > 0:
            self._height = height + 10

    def set_age(self) -> None:
        if age > 0:
            self._age = age + 20
        
        else:
        print(f"{self.name} Error, height can’t be negative
        Height update rejected") 


    def get_height(self) -> float:
        return self._height
    
    def get_age(self) -> int:
        return self._age

    def show(self: Plant) -> None:
        print(f"{self.name}:  {self._height}cm, {self._age_} days old")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, -10)
    print("Plant created:",end= "  ")
    rose.show()
    rose.set_age()