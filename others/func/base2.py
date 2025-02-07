global_var = 10

def outer_function() :
    outer_var = 20

    def inner_function() :
        inner_var = 30
        print("inner: ", inner_var, outer_var, global_var)

    inner_function()
    print("outer: ", outer_var, global_var)
outer_function()
print("Global:", global_var)