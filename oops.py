# ==========================================
# 1. Multilevel Inheritance
# ==========================================
print("--- 1. Multilevel Inheritance ---")
class Vehicle:
    def start(self):
        print("Vehicle starts moving.")

class Car(Vehicle):
    def drive(self):
        print("Car is being driven on road.")

class ElectricCar(Car):
    def charge(self):
        print("Electric car battery is charging.")

ev = ElectricCar()
ev.start()
ev.drive()
ev.charge()


# ==========================================
# 2. Multiple Inheritance
# ==========================================
print("\n--- 2. Multiple Inheritance ---")
class Teacher:
    def teach(self):
        print("Teaching students in the classroom.")

class Researcher:
    def research(self):
        print("Conducting research and publishing papers.")

class Professor(Teacher, Researcher):
    def profile(self):
        print("Professor role: Teaching + Researching.")

prof = Professor()
prof.teach()
prof.research()
prof.profile()


# ==========================================
# 3. Hierarchical Inheritance
# ==========================================
print("\n--- 3. Hierarchical Inheritance ---")
class Shape:
    def display(self):
        print("This is a geometrical shape.")

class Circle(Shape):
    def area_circle(self, r):
        print("Area of Circle:", 3.1416 * r * r)

class Rectangle(Shape):
    def area_rect(self, l, w):
        print("Area of Rectangle:", l * w)

class Triangle(Shape):
    def area_tri(self, b, h):
        print("Area of Triangle:", 0.5 * b * h)

c = Circle()
c.display()
c.area_circle(5)

r = Rectangle()
r.area_rect(4, 6)


# ==========================================
# 4. Method Overriding
# ==========================================
print("\n--- 4. Method Overriding ---")
class Animal:
    def make_sound(self):
        print("Some generic animal sound...")

class Dog(Animal):
    def make_sound(self):
        print("Dog says: Bark! Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow! Meow!")

animal = Animal()
animal.make_sound()

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()


# ==========================================
# 5. Operator Overloading (Add Two Complex Numbers)
# ==========================================
print("\n--- 5. Operator Overloading ---")
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overloading the '+' operator
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def show(self):
        print(self.real, "+", self.imag, "i")

c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 4)
c3 = c1 + c2  # Calls __add__ method automatically

print("First Complex Number:")
c1.show()
print("Second Complex Number:")
c2.show()
print("Sum of Complex Numbers:")
c3.show()


# ==========================================
# 6. Private Variable (__salary)
# ==========================================
print("\n--- 6. Private Variable ---")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private variable

    def get_salary(self):
        # Getter method to access private variable safely
        return self.__salary

emp = Employee("Rohit", 50000)
print("Employee Name:", emp.name)
print("Employee Salary (Accessed via method): ₹", emp.get_salary())


# ==========================================
# 7. ATM System Using Encapsulation
# ==========================================
print("\n--- 7. ATM System Encapsulation ---")
class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin          # Private PIN
        self.__balance = balance  # Private Balance

    def withdraw(self, entered_pin, amount):
        if entered_pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful! Remaining Balance: ₹", self.__balance)
            else:
                print("Insufficient balance!")
        else:
            print("Incorrect PIN! Access denied.")

my_atm = ATM(1234, 10000)
my_atm.withdraw(1234, 2000)


# ==========================================
# 8. Game Character Design
# ==========================================
print("\n--- 8. Game Character Design ---")
class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(self.name, "attacks the enemy!")

class Warrior(GameCharacter):
    def attack(self):
        print(self.name, "attacks with a heavy sword! ⚔️")

class Mage(GameCharacter):
    def attack(self):
        print(self.name, "casts a magical fireball! 🔥")

w = Warrior("Thor", 100)
w.attack()

m = Mage("Gandalf", 80)
m.attack()