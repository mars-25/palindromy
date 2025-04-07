def czy_palindrom(zdanie):
    """
    Sprawdzanie czy wyraz jest palindromem
    
    Argumenty:
        wyraz(str) 
    
    Zwraca:
        wartość boolean
    
    """

    znaki =""
    for znak in zdanie.lower():
        if znak.isalpha():
            znaki+=znak
    return znaki == znaki[::-1] 
 
wyrazenie = 'A man, a plan, a canal:Panama'            
wynik = czy_palindrom(wyrazenie)

#print(wynik)
if wynik:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")

print(f"\nTo jest wyraz zadany: {wyrazenie}\n")
#help(czy_palindrom)
