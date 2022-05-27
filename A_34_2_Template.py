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

Aufgabe 34.2 der Aufgabensammlung
"""


import matplotlib.pyplot as plt
from sympy import symbols, Sum, factorial, oo
from sympy import init_printing, pprint

init_printing(pretty_print=True)

"""
Definition der Reihen und Symbole
"""
(k, n) = symbols('k n')
a_n = Sum(1/k, (k, 1, n))
b_n = Sum(2**k/factorial(k), (k, 1, n))
c_n = Sum(k, (k, 1, n))
d_n = Sum(k, (k, 1, n))


"""
Überprüfung auf Konvergenz/Divergenz
"""
for serie in [a_n, b_n, c_n, d_n]:
    if serie.is_convergent():
        pprint("Die Reihe {} konvergiert gegen {}.".format(serie, serie.doit()))
    else:
        pprint("Die Reihe {} ist divergent.".format(serie))


"""
Darstellung der ersten 20 Partialsummen
"""
i = 1
valA = []
valB = []
valC = []
valD = []

while i < 21:
    TODO

pA = plt.plot(range(1, 21), valA, 'bo', label='a_n')
pB = TODO
pC = TODO
pD = TODO
plt.legend(loc=4, ncol=2)
