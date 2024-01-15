def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def print_numbers(number):
    for i in range(1, number + 1):
        print(i, end=" ")
    print()  # For a newline after printing all numbers

# Main program
try:
    user_number = int(input("Enter a number: "))
    if is_even(user_number):
        print(f"{user_number} is an even number.")
    else:
        print(f"{user_number} is an odd number.")

    print("Numbers from 1 to", user_number, ":")
    print_numbers(user_number)

except ValueError:
    print("Please enter a valid number.")
