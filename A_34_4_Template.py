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

Aufgabe 34.4 der Aufgabensammlung
"""


# Importiere notwendige packages
from sympy import symbols, integrate, Piecewise, pi, cos, sin
from sympy import init_printing, pprint, plot
init_printing(pretty_print=True)
"""
Definition der Variablen und Symbole
"""
x = symbols('x')

"""
Funktion zum Erstellen einer Fourier-Reihe
Parameter:
f... zu approximierende Funktion
T... Periodendauer der gegebenen Funktion
order... Grad der Fourier-Reihe, bis zu welchem diese entwickelt werden sollte
"""


def my_fourier(f, T, order):
    # Überprüfe ob gegebener Grad passt
    if order < 1:
        raise ValueError("Gegebene Ordnung muss mindestens 1 sein")

    # Definiere a0
    a0 = TODO

    # Laufindex für Reihe
    k = 1
    # Fourier-Reihe initialisieren
    four = TODO
    # Für jedes k ermittle ak und bk und erweitere Fourier Reihe entsprechend
    while k <= order:
        ak = TODO
        bk = TODO
        four += TODO
        k += TODO
    # Gebe erhaltene Fourier Reihe zurück
    return four

"""
Definiere die gegebene Funktion und wende my_fourier() an
"""

# Definiere die gegebene Funktion f
f = Piecewise(TODO)

p = plot(f, xlim = [-6,6], ylim = [-1/2,2], show = False, legend = True, nb_of_points = 2048, label = "f(x)")
for i in range(1,6): 
    pprint('\n Fourierpolynom vom Grad {}:{}'.TODO)
    p1 = plot(TODO)
    p.extend(p1)
p.title = 'Fourierreihe'
p.show()



