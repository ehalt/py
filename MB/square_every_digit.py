def square_digits(num):
    numstr = str(num)
    tempstr = ""

    for num in numstr:
        intnum = int(num)
        intsqr = intnum ** 2
        intstr = str(intsqr)
        tempstr += intstr
    
    return(int(tempstr))

print(square_digits(9119))





# ------ better approach ------


def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x) ** 2)
    return int(ret)


