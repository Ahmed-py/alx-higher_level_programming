#!/usr/bin/python3
def fizzbuzz():
    for itr in range(1, 101):
        if itr % 3 == 0 and itr % 5 == 0:
            print("FizzBuzz", end='')
        elif itr % 3 == 0:
            print("Fizz", end='')
        elif itr % 5 == 0:
            print("Buzz", end='')
        else:
            print(itr, end='')

        print(" ", end='')
