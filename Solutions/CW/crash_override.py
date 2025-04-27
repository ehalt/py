def alias_gen(f_name, l_name):
    if not (f_name[0].isalpha() and l_name[0].isalpha()):
        return "Your name must start with a letter from A - Z."
    
    first_letter = f_name[0].upper()
    last_letter = l_name[0].upper()

    return f"{FIRST_NAME[first_letter]} {SURNAME[last_letter]}"





# better approach 

def alias_gen(f_name, l_name):
    try:
    	return FIRST_NAME[f_name.upper()[0]]+' '+SURNAME[l_name.upper()[0]]
    except:
    	return 'Your name must start with a letter from A - Z.'




