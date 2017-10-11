"""
class c:
    dangerous = 2

c1 = c()
c2 = c()
print(c1.dangerous)

c1.dangerous = 3
print(c1.dangerous)
print(c2.dangerous)

del c1.dangerous
print(c1.dangerous)

c.dangerous = 3
print(c2.dangerous)
print(c1.dangerous)
"""

list = ['a', 'b','c', 'd', 'e', 'f']
print(list[1:0])