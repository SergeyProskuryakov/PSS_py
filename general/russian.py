def word_form(n, variants=['год', 'года', 'лет']):
    n = n % 100
    if (n < 5) or (n > 20): 
        if (n % 10) in [2,3,4]:
            return variants[1]
        if (n % 10) == 1:
            return variants[0]
    return variants[2]