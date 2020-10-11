import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError as ex:
    print("Just type numbers")
    sys.exit(1)


try:
    res = x/y
    print(f"{x}/{y}={res}")
except ZeroDivisionError as ex:
    print("Impossible to divide by \"0\"")
finally:
    print('End of program.')
    sys.exit(1)
