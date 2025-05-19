# 1.Given a side of square. Find its perimeter and area.
side = float(input("Enter the side length of the square: "))

perimeter = side * 4
area = side ** 2

print('Perimeter of square ', perimeter)
print('Area of square ', area)

# 2.Given diameter of circle. Find its length.
diameter = float(input("Enter the diameter of the circle: "))
length = 3.14159 * diameter

print('Lenght of circle is ',length)

# 3.Given two numbers a and b. Find their mean.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
mean = (a + b) / 2

print("Mean:", mean)

# 4.Given two numbers a and b. Find their sum, product and square of each number.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2

print("Sum:", sum_ab)
print("Product:", product_ab)
print("Square of first number:", square_a)
print("Square of second number:", square_b)