import math
import os

# Basic print screen
print("Hello, World!")


# Operator and type convertion
a = 5
print("a = ", 5)
print(5 // 2)
print(2 ** 3)

int_plus = 1 + int("2")
print(type(int_plus), int_plus)
str_plus = str(1) + "2"
print(type(str_plus), str_plus)
print(type(True), True)


# List - Mutable
my_list = ["Banana", 1, False]
my_list[0] = "Orange"
print(my_list, my_list[0], my_list[-1])
del my_list[0]
print(my_list, my_list[0], my_list[-1])
print(list())

# Tuple - Immutable
basket = (1, "apple", True)
# basket[1] = "Coconut" - Cannot modify or delete the value
# del basket[1] - Cannot modify or delete the value
print(basket, basket[1])
del basket
# print(type(basket)) - NameError: name 'basket' is not defined
t1 = tuple()
print("t1 =", t1)


# String - sequence of characters
name = '"John"'
print(name)
name = """Jame
, Dean"""
print(name)
name = "Jimmy Johnson"
print(name[0] + ".", name[6:])
print((name + " ") * 2)

# Sets - unordered unique list
scores = {1, 2, 3}
print(scores)
scores.add(5)
print(scores)
scores.remove(2)
print(scores)
scores.update((4, 7))
scores.update([99])
print(scores)

A = {1, 2, 3}
B = {2, 3, 4, 5}

print("A: ", A)
print("B: ", B)
print(A | B)
print(A & B)
print(A - B)
print(A ^ B)

# Dictionaries - key-value pair
my_dict = {"name": "John", "age": 25, "isAvailable": True}
del my_dict["isAvailable"]
print(my_list)

# range

numbers = range(1, 6)
print(list(numbers))
print(tuple(numbers))
print(set(numbers))
print(dict.fromkeys(numbers, int()))

# print(str())
# print(float())
# print(bool())
# print(complex())
# print(list())
# print(tuple())

# control flow
# if else
num = 3
if num % 2 == 2:
    print("Even")
else:
    print("Odd")

# while

i = 0
while i < 5:
    i += 1
print(i)


# for
numbers = list(range(1, 5))
sum = 0
for number in numbers:
    sum += number
print(sum)

# break
for c in "hello":
    if c == "l":
        break
    print(c)

# continue
for c in "world":
    if c == "l":
        continue
    print(c)

# pass inside for loop for future implementation (it does nothing)
numbers = set(range(1, 5))
for number in numbers:
    pass


# Function


def say_hello(name):
    return "Hello " + name + "!"


hello = say_hello("Helen")
print(hello)


circle = lambda r: round((math.pi * r) ** 2, 2)
print(circle(2))


# I/O
path = os.path.dirname(__file__)
f = open(os.path.join(path, "test.txt"), encoding="utf-8")
for line in f.readlines():
    print(line)
f.close()

# OOP
# class
class MyClass:
    a = 10

    def func(self):
        print("Hello")


print(MyClass.a)
print(MyClass.func)
print(MyClass.__doc__)


obj = MyClass()
print(obj.a)
print(obj.a + 5)


class ConplexNumber:
    def __init__(self, r=0, i=0) -> None:
        self.real = r
        self.image = i

    def getData(self):
        print("{0}+{1}j".format(self.real, self.image))


c1 = ConplexNumber(5, 10)
c1.getData()
c2 = ConplexNumber()
c2.getData()

# Inheritance
class Dog:
    def __init__(self, color: str = str()) -> None:
        self.leg = 4
        self.color = color

    def bark(self):
        print("bow-how!")

    def getData(self):
        print("The {0} dog have {1} legs.".format(self.color.title(), self.leg))


class Greyhound(Dog):
    def bark(self):
        print("Woof!!")


dog1 = Greyhound("black")
dog1.getData()
dog1.bark()


# Iterators -  an object that can be iterated upon
numbers = [4, 7, 1, 88]
my_iter = iter(numbers)
print(next(my_iter))
print(next(my_iter))

# Generators - simple way of creating iterators.


def rev_str(str):
    for i in range(len(str) - 1, -1, -1):
        yield str[i]


for c in rev_str("hello"):
    print(c, end="")
print()
print("".join(list("hello")[::-1]))

# Decorators
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

# is equivalent to
# def printer(msg):
#     print(msg)
# printer = star(percent(printer))
