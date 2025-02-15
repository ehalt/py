try:
    num = int(input('Enter a number:'))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print('Erorr: you cannot divide by zero')
except ValueError:
    print('Error: That was not a valid number!')
finally:
    print("This block always executes!")