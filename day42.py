# Write a program that uses a try-except block to handle division by zero.


def main():
    """
    This function uses a try-except block to handle division by zero.
    """
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print(a / b)
    except ZeroDivisionError:
        print("You can't divide by zero.")


if __name__ == "__main__":
    main()
