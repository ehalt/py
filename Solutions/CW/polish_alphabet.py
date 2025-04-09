# https://www.codewars.com/kata/57ab2d6072292dbf7c000039

def correct_polish_letters(st): 
    d = {
    "ą" : "a",
    "ć" : "c",
    "ę" : "e",
    "ł" : "l",
    "ń" : "n", 
    "ó" : "o",
    "ś" : "s",
    "ź" : "z",
    "ż" : "z"
    }
    replaced_str = map(lambda char : d.get(char, char), st)
    return ''.join(replaced_str)

# the short version 
def correct_polish_letters(st): 
    d={'ą':'a',
    'ć':'c',
    'ę':'e',
    'ł':'l',
    'ń':'n',
    'ó':'o',
    'ś':'s',
    'ź':'z',
    'ż':'z'}
    return "".join(d[c] if c in d else c for c in st)



#  another effective approach 
def correct_polish_letters(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))



# another one 
def correct_polish_letters(st):
    l = "ąćęłńóśźż"
    lt = "acelnoszz"
    for i in range(len(l)):
        st = st.replace(l[i], lt[i])
    return st



