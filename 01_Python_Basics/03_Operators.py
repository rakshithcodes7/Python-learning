# Python Operators Example

a = 10
b = 3

# Arithmetic Operators
print("Arithmetic Operators")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division
print("a // b =", a // b) # Floor Division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation

# Comparison Operators
print("\nComparison Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Logical Operators
print("\nLogical Operators")
x = True
y = False
print("x and y =", x and y)
print("x or y =", x or y)
print("not x =", not x)

# Assignment Operators
print("\nAssignment Operators")
c = 5
c += 2
print("c += 2 ->", c)

c -= 1
print("c -= 1 ->", c)

c *= 3
print("c *= 3 ->", c)

# Bitwise Operators
print("\nBitwise Operators")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)

# Membership Operators
print("\nMembership Operators")
nums = [1, 2, 3, 4, 5]
print("3 in nums =", 3 in nums)
print("7 not in nums =", 7 not in nums)

# Identity Operators
print("\nIdentity Operators")
p = [1, 2, 3]
q = p
r = [1, 2, 3]

print("p is q =", p is q)
print("p is r =", p is r)
print("p is not r =", p is not r)