import math

choice = input("Cube or Tetrahedon (C/T)? ")
if choice == "T" or choice == "t":
    x = input("Length of tetrahedon (cm): ")
    result = ((float(x) ** 3)/6) * math.sqrt(2)
    print("The volume of the tetrahedon is ", result, " cm^3!")
elif choice == "C" or choice == "c":
    x = input("Length of cube (cm): ")
    result = float(x) ** 3
    print("The volume of the cube is ", result, " cm^3!")