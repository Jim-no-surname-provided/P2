# %%
"""
@ authors: 
    
Autor: Helmut Joaquín Pfeffer
Matr.Nr.: k12105862

Autor: Rainer Grobauer
Matr.Nr.: k1238053

Autor: Hannes Maislinger
Matr.Nr.: k01455994

Autor: Zinedin Puškar
Matr.Nr.: k12043388

Aufgabe 34.3 der Aufgabensammlung
"""

# Importiere notwendige packages
from sympy import factor, symbols, factorial, ln, sin, exp, diff, plot
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
    tay = f.subs(x, x0)
    k = 1               # Laufindex k für die Taylorreihe
    factk = 1
    f_differentiated = f
    # Modelliere Taylor-Reihe über while-Schleife
    while k <= order:
        # Ermittle aktuelle Ableitung
        factk *= k
        f_differentiated = diff(f_differentiated, x)

        # df = diff(f, x, k).subs(x, x0) * (x - x0)**k / factorial(k)

        df = f_differentiated.subs(x, x0) * (x - x0)**k / factk

        # Erweitere Taylorreihe um aktuelles Glied
        tay += df
        # Erhöhe Laufindex
        k += 1
    # Gebe Taylor-Reihe zurück
    return tay


"""
Implementiere gegebene Funktion und wende my_taylor() an
"""

# Definiere die gegebene Funktion f
f = ln(x)*sin(exp(x-1))

p = plot(f, xlim=[0, 4], ylim=[-3, 3], show=False,
         legend=True, nb_of_points=2048, label="f(x)")
for i in range(1, 6):
    pprint('\n Taylorpolynom vom Grad {}:'.format(i))
    pprint(my_taylor(f, 1, i))
    p1 = plot(my_taylor(f, 1, i), show=False,
              legend=True, label="f{}(x)".format(i))
    p.extend(p1)
p.title = 'Taylorreihe'
p.show()