class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

def main():
    dog = Dog()
    cat = Cat()
    cow = Cow()

    animals = [dog, cat, cow]

    for animal in animals:
        print(f"{animal.__class__.__name__} says: {animal.make_sound()}")

if __name__ == "__main__":
    main()