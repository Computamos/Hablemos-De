# ¿Qué es?

Tienes un problema que si lo divides de alguna manera (el concepto de "división" depende de las propiedades del problema) entonces te quedan problemas que tienen exactamente las mismas propiedades que el problema original (antes de ser dividido) y que puedes -nuevamente- volver a dividir, luego cuando ya tienes un resultado al que sí le puedes calcular la solución de forma "directa" (ya sabes la respuesta por alguna propiedad o porque el enunciado del problema te la dice) entonces solo devuelves esa respuesta, luego, a partir de ese resultado "atómico" puedes empezar a reconstruir a la solución del problema "anterior" (o sea, el problema que era un poco más grande y que llamó al problema más pequeño -al cual ya te sabías la solución-) a partir de las soluciones de ambos subproblemas resueltos.

# Observaciones
- Como nuestro input se puede dividir en "partes iguales" entonces podemos graficarlo con árbol.
    - Ejemplo:
        ```mermaid
        graph TD
        A((8^4))
        B((8^2))
        B'((8^2))
        C((8^1))
        C'((8^1))
        C''((8^1))
        C'''((8^1))
        A---B
        A---B'
        B---C
        B---C'
        B'---C''
        B'---C'''
        ```

# ¿Cómo calculamos la complejidad

El costo de un algoritmo D&C de tamaño $n$ se puede expresar como $T(n)$, que debe considerar:
    ...

$T(n) \leq a*T(n/c) + b'n^d$

Nosotros lo que queremos hacer es hallarnos una función más fácil de manejar que nos sirva como techo o piso según lo que necesitemo, a esa función la vamos a llamar $g(n)$

Es decir, queremos encontrar algo del estilo: $T(I)\leq g(I)$ (si queremos hablar de $O()$)

Formalmente: queremos que $T(n) \leq a*T(n/c) + b'n^d \leq g(n) = a*g(n/c) + bn^d$

## Ejemplito

Nos dan por input que: $T(n) = T(n/2) + 1$, queremos calcular su complejidad complejidad computacional. Sabemos que $n$ es par y natural.

Vamos a asumir que $T(1)$ es el caso base y $T(1) = 1$.

$T(n) \leq T(n/2) + 1$

Vamos a definir a nuestra $g$ como $g(n) = g(n/2) + 1$

Luego, queremos ver que: 

$T(n) \leq T(n/2) + 1 \leq g(n)$

$T(n) \leq g(n)$

Pues sabememos que $T(n) \leq g(n) \implies O(T(n)) \leq O(g(n))$

Veamos la complejidad de $g(n)$

$g(n) \leq 1*g(n/2) + 1$

$g(n) \leq 1*(1*g(n/4) + 1) + 1$

$g(n) \leq 1*(1*(1*g(n/8) + 1) + 1) + 1$
<br>
.
<br>
.
<br>
.
<br>

$g(n) \leq \log_{2}{(n)}$

$O(g(n)) \leq O(\log{(n)})$

## Ejemplito maestro

Nos dan por input que: $T(n) = a*T(n/c) + b'n^d$, queremos calcular su complejidad complejidad computacional.


## Teorema maestro (tu mantra de D&C):

* Permite resolver relaciones de recurrencia de la forma:
$$T(n) = \begin{cases} a \, T(n/c) + f(n) & \text{si } n > 1 \\ 1 & \text{si } n = 1 \end{cases}$$

* Si $f(n) = O(n^{((\log_c a) - \epsilon)})$ para $\epsilon > 0$, entonces $T(n) = \Theta(n^{\log_c a})$
* Si $f(n) = \Theta(n^{\log_c a})$, entonces $T(n) = \Theta(n^{\log_c a} \log n)$
* Si $f(n) = \Theta(n^{\log_c a} \log^k n)$ para algún $k \geq 0$, entonces $T(n) = \Theta(n^{\log_c a} \log^{k+1} n)$ (generalización del caso anterior)
* Si $f(n) = \Omega(n^{((\log_c a) + \epsilon)})$ para $\epsilon > 0$ y $a f(n/c) < k f(n)$ para $k < 1$ y $n$ suficientemente grandes, entonces $T(n) = \Theta(f(n))$

### Ejemplito de uso del Teo Maestro

Nos dan por input que: $T(n) = T(n/2) + 1$, queremos calcular su complejidad complejidad computacional. Sabemos que $n$ es par y natural.

Sabemos que $T(1)$ es el caso base y $T(1) = 1$.

1. Identificar a: $a$, $c$, $f(n)$
    - $a=1$, $c=2$, $f(n)=1$
2. Calcular $n^{log_c{a}}$
    - $n^{log_2{1}} = n^0  = 1$
2. Queremos hacer match entre nuestro f(n) con algún caso del Teo. Maestro, hacemos eso.
    - $1 = \Theta(n^{log_2{1}}) = \Theta(1)$. **¡Hace match!** 
    - $\Theta(n^{log_2{1}} * \log{n}) = \Theta(1 * \log{n}) = \Theta(\log{n})$


# Algoritmo de Karatsuba

Es básicamente la misma multiplicación que te enseñan en el cole pero con un modificación que le reduce la complejidad temporal (a través de una maravillosa observación matemática que no es trivial).

