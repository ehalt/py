import re

def string_clean(s):
    clear = re.sub(r'\d', '', s)
    return clear


# another way to solve it 
def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())
