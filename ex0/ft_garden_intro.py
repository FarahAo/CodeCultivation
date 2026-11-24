def garden_intro(name: str, height: int, age: int) ->None:
    print(f"Plant: {name}")
    print(f"Height:  {height}cm")
    print(f"Age:  {age} days")

if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    garden_intro("Rose", 25, 30)
    print("=== End of Program ===")
