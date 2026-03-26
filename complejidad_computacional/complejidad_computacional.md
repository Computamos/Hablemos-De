# Repaso complejidad computacional

## ¿Qué es? En castellano

En la práctica es una funcioncita que mide la cantidad de operaciones que puede llegar a tener un algoritmo dada una instancia de entrada.

# La biblia

## Parte 1
Dadas dos funciones $f, g: \mathbb{N} \to \mathbb{R}$, decimos que:

* $f(n) = O(g(n))$ si existen $c \in \mathbb{R}_+$ y $n_0 \in \mathbb{N}$ tales que $f(n) \leq c \, g(n)$ para todo $n \geq n_0$.
* $f(n) = \Omega(g(n))$ si existen $c \in \mathbb{R}_+$ y $n_0 \in \mathbb{N}$ tales que $f(n) \geq c \, g(n)$ para todo $n \geq n_0$.
* $f(n) = \Theta(g(n))$ si $f = O(g(n))$ y $f = \Omega(g(n))$.

### Mejor y peor caso

- **Mejor caso:** nos gusta más asociarlo con $\Omega$
- **Peor caso:** nos gusta más asociarlo con $O$

## Parte 2

* Si un algoritmo es $O(n)$, se dice **lineal**.
* Si un algoritmo es $O(n^2)$, se dice **cuadrático**.
* Si un algoritmo es $O(n^3)$, se dice **cúbico**.
* Si un algoritmo es $O(n^k)$, $k \in \mathbb{N}$, se dice **polinomial**.
* Si un algoritmo es $O(\log n)$, se dice **logarítmico**.
* Si un algoritmo es $O(d^n)$, $d \in \mathbb{R}_{>1}$, se dice **exponencial**.

* Cualquier función exponencial es *peor* que cualquier función polinomial: Si $k \in \mathbb{R}_{>1}$ y $d \in \mathbb{N}$ entonces $k^n$ no es $O(n^d)$. Si no entiendes esto fíjate qué pasa si asignas k=2 y d=2... Te queda que $O(2^n)$ no es $O(n^2)$ (fíjate qué pasa con otros números. Te invito a demostrarlo).
* La función logarítmica es *mejor* que la función lineal (no importa la base), es decir $\log n$ es $O(n)$ pero no a la inversa.
* La función constante es *mejor* que la función lineal (y particularmente de cualquiera), ejemplo: $f(n)=n$ es $\Omega(1)$ pero no a la inversa.
