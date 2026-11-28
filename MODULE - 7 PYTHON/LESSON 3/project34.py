def is_armstrong_number(number):
    if number < 0:
        return False

    digits = str(number)
    number_of_digits = len(digits)

    # Raise each digit to the power of the digit count, then add the results.
    total = sum(int(digit) ** number_of_digits for digit in digits)
    return total == number


number = int(input("Enter a number: "))

if is_armstrong_number(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")

        
