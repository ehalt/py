def get_drink_by_profession(param):
    prof = param.lower()
    drinksMap = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }
    return drinksMap.get(prof, "Beer
