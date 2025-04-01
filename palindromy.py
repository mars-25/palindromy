def czy_palindrom(wyraz):
    """
    Sprawdzanie czy wyraz jest palindromem
    
    Argumenty:
        wyraz(str) 
    
    Zwraca:
        wartość boolean
    
    """
    #wszystkie litery zamienione na małe
    wyraz = wyraz.lower()

    #usunięcie spacji z wyrażenia 
    wyraz = wyraz.replace(" ","")

    #sprawdza czy wyrażenie nie zawiera cyfr
    if wyraz.isalpha():
        pass
    else:
        wyraz = 'xy'

    return(wyraz == wyraz[::-1])
            

wyrazenie = 'Kobyla ma maly bok'            
wynik = czy_palindrom(wyrazenie)

#print(wynik)
if wynik:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")

print(f"\nTo jest wyraz zadany: {wyrazenie}\n")
#help(czy_palindrom)
