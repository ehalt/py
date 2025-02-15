# debugging during development with assert 

number = 1
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number =})")
print(number)
