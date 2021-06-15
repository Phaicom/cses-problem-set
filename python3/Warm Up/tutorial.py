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
