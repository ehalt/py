def flick_switch(lst) :
    ans = []
    switch = True
    for item in lst:
        if item == 'flick':
            switch = not switch
        ans.append(switch)
    return ans



lst = ['flick', 'chocolate', 'adventure', 'sunshine']
result = flick_switch(lst)
print(result)