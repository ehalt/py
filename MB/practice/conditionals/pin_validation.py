def validate_pin(pin):
    # return true or false
    return(len(pin) == 4 or len(pin) == 6) and pin.isdigit()
    


print(validate_pin('12'))





## better approach 

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

