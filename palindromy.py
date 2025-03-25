def czy_palindrom(wyraz):
    """
    Funkcja sprawdza czy wyraz jest palindromem
    
    Argumenty:
        wyraz(str) 
    
    Zwraca:
        wartość boolean
    
    """
    dlugosc_slowa = len(wyraz)
    #print(f"Dlugosc slowa = {dlugosc_slowa} {type(dlugosc_slowa)}")
    for litera in wyraz:
        dlugosc_slowa = dlugosc_slowa - 1
        if litera != wyraz[dlugosc_slowa]:
            return False
               
    return True
            
            
wynik = czy_palindrom('kobylamamalybokkobylamamalybokkobylamamalybok')

print(wynik)
if wynik == False:
    print("To nie jest palindrom")
else:
    print("Palindrom to jest")

#help(czy_palindrom)
