#!/usr/bin/env python3

# Created By: Jessah
# Date: Oct 4, 2022
# This program calculates the perimeter and area of a heptagon.


import math

math.tan
import fractions


def main():

    # user input for side length of heptagon
    print()
    side_length = int(input("Enter a side length for a heptagon: "))
    rounding = input("Round to 2 decimal? (yes/no): ")

    # Calculation process for area and perimeter of a heptagon
    print()

    half_side = side_length / 2
    height = side_length / math.tan(0.448793964)
    area = 0.5 * half_side * height * 7

    perimeter = side_length * 7

    # if, elif, else statements for if the user wants rounded 2 decimal places
    # Also display area and perimeter to user

    if rounding == "yes":
        print("The area is: {:.2f} cm^2".format(area))
        print("The perimeter is: {} cm".format(perimeter))

    elif rounding == "no":
        print("The area is: {} cm^2".format(area))
        print("The perimeter is: {} cm".format(perimeter))

    elif rounding == "Yes":
        print("The area is: {:.2f} cm^2".format(area))
        print("The perimeter is: {} cm".format(perimeter))

    elif rounding == "No":
        print("The area is: {} cm^2".format(area))
        print("The perimeter is: {} cm".format(perimeter))

    else:
        print("That was not a yes or no")
        print("If it was... Not like that ")


if __name__ == "__main__":
    main()
