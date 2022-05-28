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
    a0 = (2/T) * f.integrate((x, 0, T))

    pprint(a0)

    # Laufindex für Reihe
    n = 1
    # Fourier-Reihe initialisieren
    four = a0/2
    # Für jedes k ermittle ak und bk und erweitere Fourier Reihe entsprechend
    while n <= order:
        ak = (2/T) * integrate(f * cos(x*2*n*pi/T), (x, 0, T))
        # ak = (2/T) * (f * cos(x*2*n*pi/T)).integrate((x, -T/2, T/2))
        bk = (2/T) * integrate(f * sin(x*2*n*pi/T), (x, 0, T))
        # bk = (2/T) * integrate(f * sin(x*2*n*pi/T), (x, -T/2, T/2)).doit()

        four += ak*cos(x*2*n*pi/T) + bk*sin(x*2*n*pi/T)

        n += 1

    # Gebe erhaltene Fourier Reihe zurück
    return four


"""
Definiere die gegebene Funktion und wende my_fourier() an
"""

# Definiere die gegebene Funktion f
f = Piecewise((x,           x < pi/2),
              (pi - x,      x < pi),
              (0,           x < 2*pi))
# Periodic:
g = Piecewise(((x % (2 * pi)),          (x % (2 * pi)) < pi/2),
              (pi - (x % (2 * pi)),     (x % (2 * pi)) < pi),
              (0,                       (x % (2 * pi)) < 2*pi))


p = plot(g, xlim=[-6, 6], ylim=[-1/2, 2], show=False,
         legend=True, nb_of_points=2048, label="f(x)")

for i in range(1, 6):
    pprint('\n Fourierpolynom vom Grad {}:'.format(i))
    g = my_fourier(f, 2*pi, i)
    pprint(g)
    p1 = plot(g, show=False, legend=True, label="ft{}(x)".format(i))
    p.extend(p1)
    

p.title = 'Fourierreihe'
p.show()
