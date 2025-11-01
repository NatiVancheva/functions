def rectangle_area(width, height):
    area = width * height
    return area

width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))
result = rectangle_area(width, height)
print(result)