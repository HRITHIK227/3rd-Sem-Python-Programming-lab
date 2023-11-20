def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("It's a right-angled triangle.")
    else:
        print("It's not a right-angled triangle.")

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("Area of the triangle:", area)

side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

is_right_triangle(side_a, side_b, side_c)

calculate_area(side_a, side_b, side_c)


