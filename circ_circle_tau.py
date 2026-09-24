#!/usr/bin/env python3
# Created By: Alex OBrien
# Date: Sep 24, 2026
# This program asks the user for the radius of
# a circle in mm. It then calculates and displays
# the circumference using tau
TAU = 6.28


def main():
    # get the radius from user
    radius = float(input("Enter the radius of the circle (mm): "))

    # calculate the circumference
    circumference = TAU * radius

    # display circumference
    print("")
    print("Circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()
