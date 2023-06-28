def year():
    while True:
        try:
            years = int(input("Introduzca un año: "))
            if years < 0: 
               print("Introduzca un año válido") 
               continue
            else:
               break
        except ValueError:
            print ("Ingrese un valor válido")
            continue
    return years

def leap_year(years):
    if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
        print ("Es un año bisiesto")
    else:
        print("No es un año bisiesto")
    return years



years = year()
(leap_year(years))

