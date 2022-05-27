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

Aufgabe 34.1 der Aufgabensammlung
"""
# TODO: delete pprint
from sympy import pprint
from sympy import Sum, factorial, symbols, oo, pi, plot

# Setze verwendete Symbole
k, x, n = symbols('k x n')

"""
Berechnung des Grenzwerts der Reihe
"""
# Definition der Reihe, sowie der Partialsummen
# Hinweis: subs erlaubt eine Substitution von Ausdrücken
s = ((-1)**k)*(x**(2*k+1))/(factorial(2*k + 1))
a_n = Sum(s, (k, 0, n))
a = a_n.subs(n, oo)

# Auusgabe des Grenzwerts
print("Grenzwert a(x) der Reihe ist:", a.doit(), "\n")


"""
Graphische Darstellung der ersten 10 Partialsummen
"""

p1 = plot(a, xlim=[0, 2*pi], ylim=[-1, 1],
          legend=True, label="a", line_color="blue", show=False)
for i in range(11):
    p = plot(a_n.subs(n, i), xlim=[0, 2*pi], ylim=[-1, 1], show=False, legend=True,
             line_color=(i/10, 1-i/10, i/10), label="a{}".format(i))
    p1.extend(p)
p1.title = "Funktionenapproximation"
p1.show()


"""
Berechnung der minimalen n0 
"""
# Berechnung n₀ für x = π, 2π

for x0 in [pi, 2*pi]:
    a_partial_x0 = a_n.subs(x, x0)
    a_real_X0 = a.subs(x, x0).doit().evalf()
    for k in range(1, 4):
        n0 = 0
        an0 = abs(a_partial_x0.subs(n, n0).doit().evalf() - a_real_X0)

        while an0 > 10**(-k):
            n0 += 1
            an0 = abs(a_partial_x0.subs(n, n0).doit().evalf() - a_real_X0)

        print("Ab n₀={} ist |an₀({})-a({})| <= {}".format(n0, x0, x0, 10**(-k)))
    print("\n")