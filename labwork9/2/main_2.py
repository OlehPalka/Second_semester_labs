"""
Main module.
"""
from ecosystem_2 import River
from animals_2 import Bear, Fish

if __name__ == "__main__":
    size = int(input("Enter the size of the ecosystem: "))
    ecosystem = River(size)
    print("These are the comands? you can use, to comunicate with system:")
    print("""Enter move, to move the animal
Enter refresh to check changes in the ecosystem
Enter add, to add animal
Enter count, to count animals.
Enter exit to exit).""")
    print("This is an original ecosystem.")
    print(ecosystem.check_in_string())
    while True:
        choice = input("enter your action: ")
        if choice == "count":
            letter = input("enter a letter of the animal.")
            print(ecosystem.count_anim(letter))
        elif choice == "move":
            position = int(input("enter a position of the animal: "))
            next_position = int(input("enter next position: "))
            print(ecosystem.move_animal(position, next_position))
        elif choice == "check":
            print(ecosystem.check_in_string())
        elif choice == "add":
            animal = input(
                "enter a first letter of the animal you want to add: ")
            position = int(input("enter a position of the animal: "))
            gender = bool(
                input("enter gender of the animal (M, F): "))
            power = float(input("enter power of your animal from 0 to 100: "))
            if animal.lower() == "b":
                animal = Bear(gender, power)
                print(ecosystem.adding_animal(animal, position))
            elif animal.lower() == "f":
                animal = Fish(gender, power)
                print(ecosystem.adding_animal(animal, position))
        elif choice == "exit":
            break
