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
a_n = Sum(1 / k,                    (k, 1, n))
b_n = Sum(2**k / factorial(k),      (k, 1, n))
c_n = Sum((k**2 + 1) / k**4,        (k, 1, n))
d_n = Sum((-1)**k*(k+1) / 2**k,     (k, 1, n))


"""
Überprüfung auf Konvergenz/Divergenz
"""
for serie in [a_n, b_n, c_n, d_n]:
    if serie.is_convergent():
        # pprint("Die Reihe {} konvergiert gegen {}.".format(serie, serie.doit()))
        pprint("Die Reihe ")
        pprint(serie)
        pprint(" konvergiert gegen ")
        pprint(serie.subs(n, oo).doit())

    else:
        # pprint("Die Reihe {} ist divergent.".format(serie))
        pprint("Die Reihe ")
        pprint(serie)
        pprint("ist divergent.")
    pprint("------------------")

"""
Darstellung der ersten 20 Partialsummen
"""
i = 1
valA = []
valB = []
valC = []
valD = []

while i < 21:
    valA.append(a_n.subs(n, i).doit())
    valB.append(b_n.subs(n, i).doit())
    valC.append(c_n.subs(n, i).doit())
    valD.append(d_n.subs(n, i).doit())
    i += 1

pA = plt.plot(range(1, 21), valA, 'bo', label='a_n')
pB = plt.plot(range(1, 21), valB, 'ro', label='b_n')
pC = plt.plot(range(1, 21), valC, 'go', label='c_n')
pD = plt.plot(range(1, 21), valD, 'yo', label='d_n')
plt.legend(loc=4, ncol=2)

# %%