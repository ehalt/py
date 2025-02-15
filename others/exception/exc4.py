try:
    num = int(input('Enter a number:'))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Error: you cannot divide by zero!")
except ValueError:
    print("Error: That wa not a valid number!")

