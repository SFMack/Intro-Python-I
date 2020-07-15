# Write a function is_even that will return true if the passed-in number is even.
def is_even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print('True')
        return True
    else:
        print('False')
        return False


is_even()


# Print out "Even!" if the number is even. Otherwise print "Odd"
def odd_or_even():
    num = int(input("Enter another number: "))
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")


odd_or_even()
