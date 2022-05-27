"""
@ authors: 
    
Autor:
Matr.Nr.:

Autor:
Matr.Nr.:

Autor:
Matr.Nr.:

Autor:
Matr.Nr.:

Aufgabe 34.3 der Aufgabensammlung
"""

# Importiere notwendige packages
from sympy import symbols, factorial, ln, sin, exp, diff, plot
from sympy import init_printing, pprint
init_printing(pretty_print=True)
"""
Definition der Variablen und Symbole
"""
x = symbols('x')

"""
Funktion zum Erstellen einer Taylor-Reihe
Parameter:
f... zu approximierende Funktion
x0... Startpunkt um den entwickelt werden soll
order... Grad der Taylor-Reihe, bis zu welchem diese entwickelt werden sollte
"""

def my_taylor(f, x0, order):
    # Überprüfe ob gegebener Grad passt
    if order < 0:
        raise ValueError("Gegebene Ordnung muss mindestens 0 sein")

    # Ermittle 0tes Glied der Taylorreihe
    tay = TODO
    k = 1               # Laufindex k für die Taylorreihe
    # Modelliere Taylor-Reihe über while-Schleife
    while k <= order:
        # Ermittle aktuelle Ableitung
        df = TODO
        # Erweitere Taylorreihe um aktuelles Glied
        tay += TODO
        # Erhöhe Laufindex
        TODO
    # Gebe Taylor-Reihe zurück
    return tay


"""
Implementiere gegebene Funktion und wende my_taylor() an
"""

# Definiere die gegebene Funktion f
f = ln(x)*sin(exp(x-1))

p = plot(f, xlim = [0,4], ylim = [-3,3], show = False, legend = True, nb_of_points = 2048, label = "f(x)")
for i in range(1,6): 
    pprint('\n Taylorpolynom vom Grad {}:{}'TODO)
    p1 = TODO
    p.extend(p1)
p.title = 'Taylorreihe'
p.show()

