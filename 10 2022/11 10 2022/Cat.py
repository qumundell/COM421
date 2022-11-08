class Cat:
    def __init__(self, name, age, weight):
        self.age = age
        self.weight = weight
        self.name = name

    def eat(self):
        self.weight += 1

    def walk(self):
        if self.weight >= 1:
            self.weight -= 1
        else:
            print("Error: Your cat is weightless")


cat1 = Cat("Binnie", 4, 4)
cat2 = Cat("Clyde", 1, 2)
cat3 = Cat("Old Tom", 10, 6)

print(f"{cat1.name}'s weight is {cat1.weight}, {cat2.name}'s weight is {cat2.weight}, {cat3.name}'s "
      f"weight is {cat3.weight} ")
cat3.eat()
cat1.walk()
cat2.walk()
cat3.walk()

print(f"{cat1.name}'s weight is {cat1.weight}, {cat2.name}'s weight is {cat2.weight}, {cat3.name}'s "
      f"weight is {cat3.weight} ")

