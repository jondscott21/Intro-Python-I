# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num1):
    if num1 % 2 == 0:
        return True
    return False
    #     print('Even!')
    # else:
    #     print('Odd')

print(is_even(1))
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def print_if_even(num1):
    if num1 % 2 == 0:
        print('Even!')
    else:
        print('Odd')
print_if_even(num)
