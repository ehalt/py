# global keyword 

x = 5
def change_x() :
    global x
    x = 10
    print("inside function", x)
change_x()
print("outside function", x) 