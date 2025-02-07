# nonlocal

def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

