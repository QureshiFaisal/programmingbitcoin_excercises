# ==== Exercise 4

# For the curve __y__^2^ = __x__^3^ + 7 over __F__~223~, find:

# * 2 ⋅ (192,105)
# * 2 ⋅ (143,98)
# * 2 ⋅ (47,71)
# * 4 ⋅ (47,71)
# * 8 ⋅ (47,71)
# * 21 ⋅ (47,71)
from field_element import FieldElement
from point import Point

prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x1 = FieldElement(num=192, prime=prime)
y1 = FieldElement(num=105, prime=prime)
p = Point(x1, y1, a, b)
print(p+p)
