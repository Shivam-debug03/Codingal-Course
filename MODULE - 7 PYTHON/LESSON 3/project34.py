def is_armstrong_number(number):
    if number < 0:
        return False

    digits = str(number)
    number_of_digits = len(digits)

    # Raise each digit to the power of the digit count, then add the results.
    total = sum(int(digit) ** number_of_digits for digit in digits)
    return total == number


number = int(input("Enter a number: "))

if number < 0:
    print("\n==============================")
    print("  INVALID ARMSTRONG CHECK")
    print("==============================")
    print("Negative numbers cannot be Armstrong numbers.")
else:
    digits = str(number)
    power = len(digits)
    breakdown = " + ".join(
        f"{digit}^{power}" for digit in digits
    )
    calculation = sum(int(digit) ** power for digit in digits)

    print("\n==============================")
    print("  ARMSTRONG NUMBER REPORT")
    print("==============================")
    print("Number:", number)
    print("Digit count:", power)
    print("Calculation:", breakdown)
    print("Result:", calculation)

    if is_armstrong_number(number):
        print("Verdict: YES - it is an Armstrong number!")
    else:
        print("Verdict: NO - it is not an Armstrong number.")
    print("==============================")

        
