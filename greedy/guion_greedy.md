# GUIÓN: Algoritmos Golosos (Greedy)

---

## 🎙️ INTRO

Muy buenas buenas mi gente, ¿cómo están?

Hoy vamos a hablar de algo que, con toda honestidad, es de las cosas más **satisfactorias** que te puede pasar cuando resolvés un problema: darte cuenta de que la solución óptima era, literalmente, hacer lo que **"parece mejor en cada momento"**.

Eso es un **algoritmo Greedy**. O, en español, un **algoritmo goloso**.

Y sí, el nombre es totalmente intencional. La idea es exactamente esa: el algoritmo es "codicioso", mira lo que tiene delante, toma la mejor opción disponible **ahora mismo**, y sigue para adelante. Sin arrepentimientos. Sin volver atrás.

¿Suena peligroso? Un poco. ¿Suena a que puede fallar? Absolutamente puede. Pero —y acá está la magia— hay una cantidad enorme de problemas importantísimos donde esta estrategia tan simple no solo funciona, sino que da la **solución óptima**. Y eso es lo que vamos a explorar hoy.

Antes de arrancar quiero que piensen en esto:

> Están en una fila del supermercado con el changuito lleno, y abren una nueva caja. ¿Qué hacen? ¿Se ponen a calcular cuál de las dos colas va a ser más corta en total considerando el futuro? No. Van a la que parece más corta **ahora**. Eso es greedy puro.

Ahora bien, ¿esa estrategia siempre les da el tiempo de espera mínimo? No necesariamente. Pero hay contextos donde sí. Y ese "sí" con demostración formal es lo que nos interesa.

Vamos.

---
---

## 🏗️ ¿Qué es un Algoritmo Greedy?

### La Idea Central

Un **algoritmo greedy** (o goloso) construye una solución **paso a paso**, y en cada paso elige la alternativa que parece **localmente óptima** según algún criterio, **sin revisar ni modificar decisiones pasadas**.

La definición más limpia que puedo darles es esta:

> **Greedy:** Construir una solución seleccionando en cada paso la "mejor" alternativa disponible, sin considerar (o haciéndolo muy débilmente) las implicancias futuras de esa decisión y sin mirar (o considerar) las decisiones pasadas.

Esto lo opone completamente a lo que vieron antes:
- **Fuerza bruta** explora todas las posibilidades.
- **Backtracking** explora con criterio pero puede retroceder.
- **Programación dinámica** recuerda subproblemas y los combina óptimamente.
- **Greedy** simplemente avanza, sin mirar atrás.

### El Gran Interrogante

La pregunta obvia es: ¿cómo sabemos cuándo confiar en el greedy?

La respuesta honesta es: **no siempre se puede**. Hay problemas donde el greedy falla estrepitosamente. Pero hay problemas que tienen dos propiedades especiales que garantizan que el greedy funciona:

1. **Propiedad de elección greedy (Greedy Choice Property):** Existe siempre una solución óptima que incluye la primera elección que haría el greedy. O sea: el greedy nunca "se equivoca" en su primer paso.

2. **Subestructura óptima (Optimal Substructure):** Una vez que el greedy toma su primera decisión, el subproblema que queda también tiene una solución óptima que el greedy puede encontrar. Es decir, la estrategia codiciosa se puede aplicar recursivamente.

Si un problema tiene ambas propiedades, el greedy es correcto. Y la forma de demostrar que las tiene es usando técnicas formales de prueba, que son exactamente lo que vamos a aprender hoy.

### Pros y Contras

**Pros:**
- Generalmente muy fácil de implementar.
- Complejidad temporal habitualmente muy baja (a menudo $O(n \log n)$ o $O(n)$).
- Cuando funciona, es elegante y eficiente.

**Contras:**
- No siempre da la solución óptima (ni siquiera una solución válida).
- Probar que es correcto requiere trabajo formal (que suele ser complicado).
- Un criterio greedy incorrecto puede dar resultados horribles.

La parte difícil del greedy no es implementarlo. La parte difícil es **saber qué elegir en cada paso** y luego **demostrarlo formalmente**. Eso es lo que vamos a hacer hoy.

---
---

## 🔧 Técnicas de Demostración de Correctitud

Antes de meternos con los problemas, vamos a conocer las dos herramientas que vamos a usar para demostrar que los algoritmos greedy son correctos. Son las dos técnicas estándar en el área:

### Técnica 1: "Greedy Stays Ahead" (El Greedy Se Mantiene Adelante)

La idea de esta técnica es demostrar que, **en cada paso**, la solución greedy está "al menos tan bien posicionada" como cualquier otra solución posible, incluyendo la óptima.

La estructura general de una demostración por Greedy Stays Ahead es:

1. Definir una **medida de progreso** que capture qué tan bien le está yendo al algoritmo.
2. Demostrar (generalmente por inducción) que **el greedy tiene siempre una medida de progreso al menos tan buena** como cualquier otra solución en cada paso.
3. Concluir que al final, si el greedy se "mantiene adelante" en todo momento, termina siendo óptimo.

La usamos cuando podemos comparar el greedy contra cualquier solución óptima paso a paso y demostrar que en cada posición el greedy está igual o mejor.

### Técnica 2: Argumento de Intercambio (Exchange Argument)

Esta es probablemente la técnica más poderosa y más usada.

La idea es:

1. Suponer que existe una solución óptima $O$ diferente de la solución greedy $G$.
2. Identificar la primera diferencia entre $O$ y $G$.
3. Demostrar que podemos **intercambiar** la elección de $O$ en ese punto por la elección de $G$, **sin empeorar** el valor de $O$.
4. Repetir el proceso hasta que $O$ sea idéntica a $G$.
5. Concluir que $G$ es al menos tan buena como $O$, es decir, $G$ es óptima.

El paso crítico —y el más difícil— es el paso 3: demostrar que el intercambio no empeora la solución. Acá es donde aparece el trabajo algebraico o lógico.

Ahora sí, vamos con los problemas.

---
---

## 🗓️ PROBLEMA 1 — Selección de Actividades

### El Problema

Imagínense que tienen **un aula** y $n$ materias quieren usarla durante el día. Cada actividad $i$ tiene una hora de inicio $s_i$ y una hora de fin $f_i$. Solo puede usarse el aula para una actividad a la vez, y las actividades no se pueden interrumpir.

**¿Cuál es el máximo número de actividades que pueden programar sin que se solapen?**

Por ejemplo, supongamos estas actividades:

| Actividad  | Inicio | Fin  |
|------------|--------|------|
| Matemáticas | 09:00 | 11:00 |
| Física     | 10:00 | 12:00 |
| Historia   | 08:00 | 13:00 |
| Química    | 12:00 | 14:00 |
| Literatura | 10:00 | 16:00 |
| Inglés     | 12:00 | 16:00 |
| Arte       | 14:00 | 17:00 |
| Música     | 18:00 | 20:00 |

¿Cómo elegirían ustedes?

### ¿Qué Criterio Greedy Usar?

Pensemos en candidatos:

1. **Elegir la más corta disponible.** Suena razonable... ¿pero es correcta?
2. **Elegir la que empiece más temprano.** Intuitivo... ¿pero también correcta?
3. **Elegir la que tenga menos conflictos con otras.** Hmm, más sofisticado... ¿pero funciona?
4. **Elegir la que termine más temprano.** Libera el aula antes, ¿no?

Spoiler: los criterios 1, 2 y 3 tienen contraejemplos. El correcto es el **4: siempre elegir la actividad compatible que termine más temprano**.

La intuición detrás es bellísima: al elegir la que termina primero, **liberamos el aula lo antes posible**, dejando la mayor cantidad de tiempo disponible para las actividades futuras.

¿Por qué fallan los otros? Aquí van contraejemplos rápidos:

- **Más corta:** Una actividad de 30 minutos que va de 9:00 a 9:30 podría bloquear dos actividades de 1 hora que van de 9:00 a 10:00 y de 9:30 a 10:30. Si elegimos la corta, solo podemos tomar 1 más. Si elegimos otra, podríamos llegar a 2.
- **Empieza más temprano:** Historia (08:00 a 13:00) empieza antes que todas pero bloquea todo el día. Elegirla sería un desastre.
- **Menos conflictos:** En instancias diseñadas específicamente, esto puede fallar.

### El Pseudocódigo

```python
def seleccion_actividades(actividades):
    # Ordenamos por tiempo de finalización creciente
    actividades_ordenadas = sorted(actividades, key=lambda a: a.fin)
    
    seleccionadas = [actividades_ordenadas[0]]  # elegimos la primera
    fin_ultima = actividades_ordenadas[0].fin
    
    for actividad in actividades_ordenadas[1:]:
        # Solo la tomamos si empieza después (o cuando) terminó la última
        if actividad.inicio >= fin_ultima:
            seleccionadas.append(actividad)
            fin_ultima = actividad.fin
    
    return seleccionadas
```

Complejidad: $O(n \log n)$ por el ordenamiento, luego un solo recorrido lineal.

Aplicado al ejemplo: Música (18:00-20:00), Arte (14:00-17:00) y Química (12:00-14:00), junto con Matemáticas (9:00-11:00) dan 4 actividades. El greedy las encontrará en orden: Matemáticas → Química → Arte → Música.

### Demostración Formal de Correctitud

Vamos con la demostración usando **Greedy Stays Ahead** y **Argumento de Intercambio** combinados.

**Notación:**
- Actividades ordenadas por tiempo de fin: $f_1 \leq f_2 \leq \ldots \leq f_n$
- Solución greedy: $G = \{g_1, g_2, \ldots, g_k\}$ (en orden de selección)
- Solución óptima arbitraria: $O = \{o_1, o_2, \ldots, o_m\}$ (en orden de tiempo de fin)
- Objetivo: demostrar que $|G| = |O|$, es decir, el greedy es óptimo.

**Lema (Greedy Stays Ahead):** Para todo $i \leq \min(|G|, |O|)$, se cumple que $f(g_i) \leq f(o_i)$.

En castellano: la $i$-ésima actividad elegida por el greedy termina no más tarde que la $i$-ésima actividad elegida por cualquier solución óptima.

*Demostración por inducción sobre $i$:*

**Caso base** ($i = 1$): El greedy elige la actividad con menor tiempo de finalización entre **todas** las disponibles. Como $o_1$ también es una actividad disponible, necesariamente $f(g_1) \leq f(o_1)$. ✓

**Paso inductivo:** Supongamos que $f(g_j) \leq f(o_j)$ para todo $j < i$. Queremos probar que $f(g_i) \leq f(o_i)$.

Como $O$ es una solución válida (sin solapamientos), sabemos que:

$$s(o_i) \geq f(o_{i-1})$$

> (la actividad $o_i$ empieza después de que termina $o_{i-1}$, porque no se solapan)

Por hipótesis inductiva:

$$f(g_{i-1}) \leq f(o_{i-1})$$

Entonces por transitividad:

$$s(o_i) \geq f(o_{i-1}) \geq f(g_{i-1})$$

Esto significa que $o_i$ **es compatible** con las actividades $\{g_1, \ldots, g_{i-1}\}$ ya elegidas por el greedy. Es una candidata válida para ser elegida en el paso $i$.

Como el greedy elige la compatible que termina más temprano entre todas las disponibles, y $o_i$ es una de esas disponibles, concluimos:

$$f(g_i) \leq f(o_i)$$

El lema está demostrado. ✓

**Teorema (Optimalidad del Greedy):** El algoritmo greedy produce una solución óptima, es decir, $|G| = |O|$.

*Demostración por contradicción:*

Supongamos que $|G| < |O|$. Entonces existe una actividad $o_{|G|+1} \in O$.

Como $O$ es válida, $o_{|G|+1}$ es compatible con $\{o_1, \ldots, o_{|G|}\}$:

$$s(o_{|G|+1}) \geq f(o_{|G|})$$

Por el Lema (Greedy Stays Ahead):

$$f(g_{|G|}) \leq f(o_{|G|})$$

Entonces:

$$s(o_{|G|+1}) \geq f(o_{|G|}) \geq f(g_{|G|})$$

Esto significa que $o_{|G|+1}$ **también es compatible** con todas las actividades que el greedy eligió. Es decir, el greedy podría haberla agregado a su solución. Pero el greedy se detuvo antes. **Contradicción** con el hecho de que el greedy elige siempre que puede.

Por lo tanto $|G| \geq |O|$. Como $O$ es óptima, $|G| \leq |O|$. Entonces $|G| = |O|$. ✓ 

> Como $O$ es el óptimo, entonces no puede ocurrir que $|G| \geq |O|$ (que la greedy tenga un mayor cantidad de actividades seleccionadas), y como tampoco puede ocurrir que la greedy tenga menos actividades que $O$ (recién demostrado), entonces la greedy tiene que tener la misma cantidad de actividades que $O$

---
---

## ⏰ PROBLEMA 2 — Planificación de Tareas con Deadlines

### El Problema

Tenemos $n$ tareas. Cada tarea $t_i$ requiere exactamente **una unidad de tiempo** para completarse y tiene asociado un **deadline** $d_i$: el tiempo límite antes del cual debe completarse.

Solo podemos ejecutar una tarea a la vez, y una vez iniciada, no se interrumpe.

**¿Cuál es el máximo número de tareas que podemos completar respetando sus deadlines?**

**Ejemplo:** 4 tareas con deadlines $D = \{2, 1, 3, 2\}$.

| Tarea | Deadline |
|-------|----------|
| $t_1$ | 2        |
| $t_2$ | 1        |
| $t_3$ | 3        |
| $t_4$ | 2        |

Una solución óptima sería: ejecutar $t_2$ en $[0,1)$, $t_1$ en $[1,2)$, $t_3$ en $[2,3)$ → 3 tareas completadas. La tarea $t_4$ no puede ejecutarse sin violar su deadline.

### Estrategia Greedy

La estrategia es simple: **ordenar las tareas por deadline creciente** y ejecutar cada una si podemos terminarla antes de su deadline.

```
MaxTareas(T, D):
    Ordenar tareas por deadline: d[i₁] ≤ d[i₂] ≤ ... ≤ d[iₙ]
    S ← {}
    t_actual ← 0
    
    Para cada tarea t_j en orden de deadline creciente:
        Si t_actual + 1 ≤ d[j]:
            S ← S ∪ {t_j}
            t_actual ← t_actual + 1
    
    Retornar |S|
```

**Complejidad:** $O(n \log n)$ por el ordenamiento.

**Traza del ejemplo:**

| Iteración | Tarea | Deadline | Tiempo actual |
|-----------|-------|----------|---------------|
| 1 | $t_2$ | 1 | 0 → 1 |
| 2 | $t_1$ | 2 | 1 → 2 |
| 3 | $t_4$ | 2 | No factible (2 + 1 > 2) |
| 4 | $t_3$ | 3 | 2 → 3 |

Solución: $\{t_2, t_1, t_3\}$ con 3 tareas. ✓

### Demostración Formal: Greedy Stays Ahead

Antes de la demostración, un lema auxiliar importante:

**Lema (Intercambio sin pérdida):** Si en una solución factible ejecutamos la tarea $t_i$ antes que $t_j$ con $d(t_i) > d(t_j)$, podemos intercambiar su orden y la solución sigue siendo factible.

*Demostración:* Si $t_i$ se ejecuta en tiempo $s$ y $t_j$ en tiempo $s' > s$, con $s+1 \leq d(t_i)$ y $s'+1 \leq d(t_j)$, después del intercambio:
- $t_j$ en tiempo $s$: $s + 1 \leq s' + 1 \leq d(t_j)$ ✓
- $t_i$ en tiempo $s'$: $s' + 1 \leq d(t_j) < d(t_i)$ ✓

Esto nos dice que **podemos asumir sin pérdida de generalidad que cualquier solución óptima está ordenada por deadlines crecientes**. Muy útil.

**Lema (Greedy Stays Ahead):** Sea $G = \{g_1, \ldots, g_m\}$ la solución greedy y $O = \{o_1, \ldots, o_n\}$ una solución óptima, ambas ordenadas por deadlines. Para todo $i \leq \min(m, n)$:

$$d(g_i) \leq d(o_i)$$

*Demostración por inducción:*

**Base ($i=1$):** El greedy elige la tarea con menor deadline entre todas las factibles desde $t=0$. Como $o_1$ también es factible, $d(g_1) \leq d(o_1)$. ✓

**Paso inductivo:** Asumimos $d(g_j) \leq d(o_j)$ para todo $j < k$. El greedy ejecutó $k-1$ tareas, con tiempo de finalización $k-1$. La tarea $o_k$ en la solución óptima se ejecuta después de $k-1$ tareas, también con tiempo de finalización $k-1$ en el óptimo. Como el greedy siempre elige la de menor deadline entre las factibles, y por hipótesis inductiva las $k-1$ primeras elecciones del greedy tienen deadlines menores o iguales a las de $O$, el greedy tiene "más margen" para elegir la $k$-ésima tarea que $O$. Formalmente:

$$d(g_k) \leq d(o_k)$$

porque el greedy elige el mínimo deadline disponible y $o_k$ también está disponible. ✓

**Teorema (Optimalidad):** El greedy produce una solución óptima ($m = n$).

*Por contradicción:* Supongamos $m < n$. Por el lema, $d(g_m) \leq d(o_m) \leq d(o_{m+1})$. La tarea $o_{m+1}$ se ejecuta en tiempo $m+1$ en la solución óptima, entonces $m+1 \leq d(o_{m+1})$. Esto significa que después de ejecutar $G$ en tiempo $m$, la tarea $o_{m+1}$ es factible: $m + 1 \leq d(o_{m+1})$. El greedy debería haberla agregado. Contradicción. ✓

---
---

## 🚌 PROBLEMA 3 — El Viaje a Mar del Plata

### El Problema

Tomás quiere viajar de Buenos Aires (km 0) a Mar del Plata (km $M$) en su amado Renault 12. El auto tiene autonomía máxima de $C$ kilómetros con el tanque lleno, y empieza el viaje con el tanque vacío.

Las estaciones de servicio están en las posiciones $0 = x_1 \leq x_2 \leq \ldots \leq x_n \leq M$.

**Objetivo:** Minimizar la cantidad de paradas para cargar nafta.

### Estrategia Greedy

La intuición acá es directa: **siempre avanzar hasta la estación más lejana posible dentro del alcance $C$**.

```
MinParadas(x[], n, C, M):
    posicion_actual ← 0
    estaciones ← {}
    idx ← 1
    
    Mientras posicion_actual + C < M:
        ultima_alcanzable ← idx - 1
        
        Mientras idx ≤ n Y x[idx] ≤ posicion_actual + C:
            ultima_alcanzable ← idx
            idx ← idx + 1
        
        Si ultima_alcanzable == idx - 1:
            Retornar "No hay solución"
        
        estaciones ← estaciones ∪ {x[ultima_alcanzable]}
        posicion_actual ← x[ultima_alcanzable]
    
    Retornar estaciones
```

**Complejidad:** $O(n)$, ya que cada estación se examina a lo sumo una vez.

**Ejemplo:** $M = 400$ km, $C = 150$ km, estaciones en $\{0, 80, 140, 200, 280, 350, 400\}$.

| Iteración | Posición actual | Alcance hasta | Estación elegida |
|-----------|----------------|---------------|-----------------|
| 1 | 0 | 150 | 140 |
| 2 | 140 | 290 | 280 |
| 3 | 280 | 430 | 400 (destino) |

Paradas: 0, 140, 280. Total: **3 paradas**.

### Demostración Formal: Greedy Stays Ahead

**Lema (Greedy Stays Ahead):** Sean $G = \{g_1, \ldots, g_k\}$ la solución greedy y $O = \{o_1, \ldots, o_l\}$ una solución óptima. Para todo $i \leq \min(k, l)$:

$$x_{g_i} \geq x_{o_i}$$

En cristiano: la $i$-ésima parada del greedy está **al menos tan lejos** como la $i$-ésima parada del óptimo.

*Demostración por inducción:*

**Base ($i=1$):** El greedy elige la estación más lejana alcanzable desde el origen. Como $o_1$ también debe ser alcanzable, $x_{g_1} \geq x_{o_1}$. ✓

**Paso inductivo:** Asumimos $x_{g_i} \geq x_{o_i}$. Queremos probar $x_{g_{i+1}} \geq x_{o_{i+1}}$.

Sabemos que $o_{i+1}$ es alcanzable desde $o_i$:

$$x_{o_{i+1}} - x_{o_i} \leq C$$

Por hipótesis inductiva $x_{g_i} \geq x_{o_i}$, entonces:

$$x_{o_{i+1}} - x_{g_i} \leq x_{o_{i+1}} - x_{o_i} \leq C$$

Esto significa que $o_{i+1}$ **también es alcanzable desde $g_i$**. Como el greedy elige la más lejana entre las alcanzables:

$$x_{g_{i+1}} \geq x_{o_{i+1}}$$

✓

**Teorema (Optimalidad):** El greedy usa el mínimo número de paradas.

*Por contradicción:* Sea $G$ la solución greedy con $k$ paradas y $O$ óptima con $l$ paradas. Supongamos $k > l$.

Por el lema, $x_{g_l} \geq x_{o_l}$. Como la solución óptima llega a $M$ desde $o_l$, sabemos que $M - x_{o_l} \leq C$. Por lo tanto:

$$M - x_{g_l} \leq M - x_{o_l} \leq C$$

Esto significa que desde $g_l$ se puede llegar directamente a $M$, por lo que el greedy no haría más paradas después de $g_l$. Esto contradice que $k > l$. ✓

---
---

## 🪙 PROBLEMA 4 — El Problema del Cambio

### El Problema

Un clásico de la vida real: tenemos monedas de ciertos valores, y queremos dar un vuelto de valor $t$ usando el **mínimo número de monedas**.

**Algoritmo greedy:** Siempre usar la moneda de mayor valor que no exceda la cantidad restante por devolver.

```
Cambio(denominaciones[], t):
    s ← 0
    i ← 1  # empezamos por la moneda más grande
    mientras s < t:
        c ← ⌊(t - s) / denominaciones[i]⌋
        Agregar c monedas de tipo i a la solución
        s ← s + c * denominaciones[i]
        i ← i + 1
    retornar solución
```

### ¿Cuándo Funciona?

Acá viene algo **muy importante** que los va a salvar en un examen:

> El greedy del cambio **no siempre funciona**.

Ejemplo: si tenemos monedas de $\{12, 10, 5, 1\}$ centavos y queremos dar $21$ centavos:
- El greedy elige: 1 moneda de 12, 1 de 5, 4 de 1 → **6 monedas**.
- La solución óptima: 2 monedas de 10 y 1 de 1 → **3 monedas**.

¡El greedy fracasó!

Pero para el sistema monetario estándar $\{25, 10, 5, 1\}$ centavos (y sistemas similares), sí funciona. La condición formal es:

**Teorema:** Si existen $m_2, \ldots, m_k \in \mathbb{Z}_{\geq 2}$ tales que $a_i = m_{i+1} \cdot a_{i+1}$ para todo $i$ (es decir, cada denominación es un múltiplo entero de la siguiente), entonces el greedy produce la solución óptima. 
> A un sistema de este estilo se le suele decir que es un sistema de monedas "canónico".

Desde un punto de vista más simple: si ordenan las monedas por denominación ascendentemente, entonces "cada moneda tiene que valer al menos el doble que la anterior". Un poco más formal sería:
* Sea $M$ el conjunto de monedas.
* Sea la función:

$$
esCanónico(m, M) = \begin{cases}
True & \text{, si } M=\emptyset \\ 
False & \text{, si } m > 2*min({M}) \\ 
esCanónico(min(M), M - \{m\}) & \text{caso contrario} \\ \end{cases}
$$

Si $M$ es un sistema de monedas canónico, entonces $esCanónico(min(M), M-min(M)) = True$

La moraleja es: **el greedy es contexto-dependiente**. Siempre hay que verificar que funciona para el problema específico.

---
---

## 🎒 PROBLEMA 5 — La Mochila Fraccionaria

### El Problema

Recordemos el problema de la mochila: capacidad $C$, $n$ objetos con peso $p_i$ y beneficio $b_i$, queremos maximizar el beneficio total sin exceder la capacidad.

Ya vieron que en la versión **entera** (cada objeto va entero o no va), greedy **no** funciona con ninguna estrategia simple, y la solución requiere fuerza bruta o programación dinámica.

Pero existe una variante: la **mochila fraccionaria**, donde podemos poner **una fracción** de cada objeto.

### Estrategia Greedy para la Mochila Fraccionaria

El criterio correcto es ordenar los objetos por **cociente beneficio/peso** ($b_i / p_i$) de mayor a menor, y agregar objetos completos hasta que no quede espacio. Si no entra el siguiente objeto completo, tomamos la fracción que quepa.

```
MochilaFraccionaria(objetos, C):
    Ordenar objetos por b_i/p_i de mayor a menor
    espacio_restante ← C
    i ← 1
    
    mientras espacio_restante > 0 y i ≤ n:
        fraccion ← min(1, espacio_restante / p[i])
        Agregar fracción `fraccion` del objeto i
        espacio_restante ← espacio_restante - fraccion * p[i]
        i ← i + 1
    
    retornar solución
```

**Teorema:** El algoritmo greedy por cocientes produce la solución óptima del problema de la mochila **fraccionaria**.

La demostración es por argumento de intercambio: si la solución óptima toma menos del primer objeto (el de mayor cociente) que el greedy, podemos intercambiar esa fracción por fracción de otro objeto que esté de más en el óptimo, y el beneficio total no decrece (porque el primer objeto tiene el mayor cociente). Aplicando este argumento sucesivamente, la solución óptima se puede transformar en la greedy sin empeorar el valor.

> **Ojo:** Para la mochila **entera**, esto no funciona. Prueben con $C=10$, objetos $\{(6, 6), (5, 5), (5, 5)\}$ (peso, beneficio): el cociente sugiere tomar el objeto de peso 6 primero (cociente 1 igual a los demás), pero la solución óptima entera es tomar los dos de peso 5 para beneficio 10, mientras que el greedy tomaría el de peso 6 y uno de peso 5 para... esperar, todos tienen cociente 1. Ejemplo más ilustrativo: $C=10$, $\{(6, 9), (5, 7), (5, 7)\}$, cocientes $1.5, 1.4, 1.4$. Greedy entera toma el de 6 y... no puede agregar ninguno de 5 (6+5=11>10). Beneficio: 9. Óptimo: tomar los dos de 5. Beneficio: 14. El greedy falló.

---
---

## ⏱️ PROBLEMA 6 — Minimizar el Tiempo de Espera Total

### El Problema

Un servidor tiene $n$ clientes para atender. El tiempo de atención del cliente $i$ es $t_i$. Los clientes pueden ser atendidos en cualquier orden.

Si el orden de atención es $I = (i_1, i_2, \ldots, i_n)$, el tiempo total de espera es:

$$T = t_{i_1} + (t_{i_1} + t_{i_2}) + (t_{i_1} + t_{i_2} + t_{i_3}) + \ldots = \sum_{k=1}^{n} (n-k) \cdot t_{i_k}$$

> Esta fórmula puede asustar, pero entendámosla con calma. El cliente atendido primero espera $0$ (lo atendemos de una), pero **contribuye** a la espera de todos los que siguen: los restantes $n-1$ clientes ya llevaban esperando su tiempo. El segundo cliente espera $t_{i_1}$ y contribuye a $n-2$ más. En general, el $k$-ésimo en la cola "cuesta" $t_{i_k}$ al total por cada uno de los $(n-k)$ clientes que vienen después.

**Objetivo:** Determinar el orden de atención que minimiza $T$.

### Estrategia Greedy

La estrategia es atender primero al cliente con **menor tiempo de atención** (Shortest Job First).

**Teorema:** El algoritmo greedy por menor tiempo de atención produce la solución óptima.

*Demostración por Argumento de Intercambio:*

Sea $I = (i_1, \ldots, i_n)$ cualquier permutación. Supongamos que existe una posición $j$ tal que $t_{i_j} > t_{i_{j+1}}$ (o sea, no está ordenada de menor a mayor).

Calculemos el impacto de intercambiar $i_j$ e $i_{j+1}$ en el tiempo total $T$. Solo cambian dos términos:

**Antes del intercambio:**

$$\text{Aporte}_{antes} = (n - j) \cdot t_{i_j} + (n - j - 1) \cdot t_{i_{j+1}}$$

**Después del intercambio:**

$$\text{Aporte}_{despues} = (n - j) \cdot t_{i_{j+1}} + (n - j - 1) \cdot t_{i_j}$$

**Diferencia** (después $-$ antes):

$$\Delta = (n-j)(t_{i_{j+1}} - t_{i_j}) + (n-j-1)(t_{i_j} - t_{i_{j+1}})$$

$$= (t_{i_{j+1}} - t_{i_j})\big[(n-j) - (n-j-1)\big]$$

$$= (t_{i_{j+1}} - t_{i_j}) \cdot 1$$

$$= t_{i_{j+1}} - t_{i_j}$$

> El álgebra se simplifica lindísimo: el coeficiente de la diferencia es exactamente 1. Esto hace que la demostración sea muy limpia.

Como asumimos $t_{i_j} > t_{i_{j+1}}$, tenemos $\Delta = t_{i_{j+1}} - t_{i_j} < 0$. Es decir, el intercambio **reduce** el tiempo total.

Conclusión: si en alguna permutación hay un par de elementos "desordenados" (el de mayor tiempo va antes del de menor tiempo), podemos intercambiarlos y mejorar la solución. Por lo tanto, **ninguna permutación con elementos desordenados puede ser óptima**, y la permutación óptima es exactamente la que ordena de menor a mayor tiempo de atención. Que es exactamente lo que hace el greedy. ✓

---
---

## 📐 PROBLEMA 7 — Minimización del Producto Escalar

### El Problema

Dados dos vectores $v, w \in \mathbb{R}^n$, queremos encontrar permutaciones de sus coordenadas que **minimicen el producto escalar**:

$$\langle v_\sigma, w_\tau \rangle = \sum_{i=1}^{n} v_{\sigma(i)} \cdot w_{\tau(i)}$$

### Estrategia Greedy

**Estrategia:** Ordenar $v$ de menor a mayor y $w$ de mayor a menor (o viceversa), luego emparejar elemento a elemento.

**Ejemplo:** $v = (3, 1, 4, 2)$ y $w = (5, 2, 8, 1)$.

- $v$ ordenado creciente: $(1, 2, 3, 4)$
- $w$ ordenado decreciente: $(8, 5, 2, 1)$
- Producto escalar mínimo: $1 \cdot 8 + 2 \cdot 5 + 3 \cdot 2 + 4 \cdot 1 = 8 + 10 + 6 + 4 = 28$

Con el orden original: $3 \cdot 5 + 1 \cdot 2 + 4 \cdot 8 + 2 \cdot 1 = 51$.

### Demostración Formal

**Teorema:** El producto escalar se minimiza emparejando el menor elemento de $v$ con el mayor de $w$, el segundo menor con el segundo mayor, y así sucesivamente.

*Demostración por Argumento de Intercambio:*

Sin pérdida de generalidad, supongamos $v_1 \leq v_2 \leq \ldots \leq v_n$ y $w_1 \geq w_2 \geq \ldots \geq w_n$. Queremos probar que esta configuración minimiza el producto escalar.

Supongamos que existe otra permutación donde hay índices $i < j$ con $\hat{v}_i > \hat{v}_j$ (las coordenadas de $v$ no están en orden creciente). Calculemos el efecto de intercambiarlos:

**Antes del intercambio** (posiciones $i$ y $j$):

$$S_{antes} = \hat{v}_i \cdot \hat{w}_i + \hat{v}_j \cdot \hat{w}_j$$

**Después del intercambio:**

$$S_{despues} = \hat{v}_j \cdot \hat{w}_i + \hat{v}_i \cdot \hat{w}_j$$

**Diferencia:**

$$S_{despues} - S_{antes} = \hat{v}_j \cdot \hat{w}_i + \hat{v}_i \cdot \hat{w}_j - \hat{v}_i \cdot \hat{w}_i - \hat{v}_j \cdot \hat{w}_j$$

$$= (\hat{v}_j - \hat{v}_i)(\hat{w}_i - \hat{w}_j)$$

> Este paso algebraico es la "magia": factorizamos la diferencia como un producto de dos factores.

Ahora bien, para que la permutación sea óptima, el intercambio no debería mejorar la solución, es decir, deberíamos tener $S_{despues} - S_{antes} \geq 0$.

Eso requiere que $(\hat{v}_j - \hat{v}_i)(\hat{w}_i - \hat{w}_j) \geq 0$.

Como $\hat{v}_i > \hat{v}_j$, el primer factor es **negativo**. Para que el producto sea no-negativo, el segundo factor debe ser **no-positivo**: $\hat{w}_i \leq \hat{w}_j$.

En conclusión: en cualquier solución óptima, si $\hat{v}_i > \hat{v}_j$ (coordenadas de $v$ fuera de orden creciente), entonces $\hat{w}_i \leq \hat{w}_j$ (coordenadas de $w$ en orden no-decreciente en esas posiciones). Esto significa que los elementos de $v$ y $w$ están emparejados en **órdenes opuestos**, que es exactamente lo que produce el greedy. ✓

---
---

## 🛠️ LAS DOS CARAS DE DEMOSTRAR GREEDY

Ya vimos dos técnicas en acción con varios ejemplos. Vamos a consolidar:

### Greedy Stays Ahead — Cuándo Usarla

Usala cuando podés definir una **medida de progreso cuantificable** (posición, deadline acumulado, tiempo de finalización, etc.) y demostrar que en cada paso el greedy tiene una medida al menos tan buena como cualquier solución óptima.

**Estructura tipo:**
1. Ordenar ambas soluciones (greedy $G$ y óptima $O$) cronológicamente.
2. Demostrar por inducción que $\text{medida}(g_i) \geq \text{medida}(o_i)$ (o $\leq$, según corresponda).
3. Concluir por contradicción que $|G| = |O|$.

### Argumento de Intercambio — Cuándo Usarlo

Usalo cuando podés tomar cualquier solución óptima $O$ e ir transformándola en la solución greedy $G$, un intercambio a la vez, sin empeorar el valor.

**Estructura tipo:**
1. Tomar una solución óptima $O$ diferente de $G$.
2. Identificar la primera posición donde difieren.
3. Demostrar que intercambiar la elección de $O$ por la de $G$ en esa posición no empeora $O$.
4. Concluir que $G$ es óptima por construcción inductiva.

### ¿Cuál Usar?

En la práctica:
- Si el problema es "¿cuántas cosas puedo meter/seleccionar?", suele funcionar mejor **Greedy Stays Ahead**.
- Si el problema es "¿cuál es el mejor orden/emparejamiento?", suele funcionar mejor el **Argumento de Intercambio**.
- Muchas veces se combinan ambas en la misma demostración (como vimos en la selección de actividades con deadlines).

---
---

## ⚠️ CUANDO EL GREEDY FALLA — Contraejemplos Importantes

Para que quede claro que el greedy no es la solución a todo:

### Mochila Entera

Ya lo vimos: el cociente $b_i/p_i$ falla porque no podemos fraccionar objetos.

### Problema del Cambio con Denominaciones Raras

Monedas $\{12, 10, 5, 1\}$, cambio de 21:
- Greedy: 12 + 5 + 1 + 1 + 1 + 1 = **6 monedas**
- Óptimo: 10 + 10 + 1 = **3 monedas**

### El Viajante de Comercio (TSP)

El greedy "siempre ir a la ciudad más cercana no visitada" produce rutas que pueden ser más largas que la óptima.

### La Lección

Un algoritmo greedy sin demostración de correctitud es simplemente **una heurística**: puede dar buenos resultados en promedio pero no garantiza la solución óptima. La demostración formal es lo que lo transforma en un algoritmo con garantías reales.

---
---

## 📋 MANDAMIENTOS DEL GREEDY

Para cerrar, les dejo los mandamientos que tienen que tener siempre presentes:

**1. SIEMPRE definí claramente el criterio de elección.** No basta con decir "elijo el mejor"; hay que precisar qué significa "mejor" en el contexto del problema.

**2. NUNCA asumas que un criterio greedy funciona sin demostrarlo.** El hecho de que "suene lógico" no es demostración. Necesitás o Greedy Stays Ahead o Argumento de Intercambio (o ambos).

**3. BUSCÁ contraejemplos primero.** Antes de perder tiempo demostrando, intentá romper la estrategia. Si encontrás un contraejemplo, cambiás de enfoque. Si no podés encontrar uno, probablemente sea correcto.

**4. USÁ el ordenamiento a tu favor.** La mayoría de los algoritmos greedy empiezan con un ordenamiento por algún criterio. Ese paso es casi siempre $O(n \log n)$ y es la clave del algoritmo.

**5. RECORDÁ que el greedy no vuelve atrás.** Esto es una restricción y también una ventaja: la implementación es simple y la complejidad baja. Pero implica que la elección local debe ser siempre correcta.

**6. CUANDO probes correctitud, siempre asumí que la solución óptima puede ser cualquier cosa.** No la fijés artificialmente. La demostración tiene que funcionar para toda solución óptima posible.

**7. EL argumento de intercambio es tu mejor amigo.** Internalizalo: tomo el óptimo, le cambio algo para hacerlo más parecido al greedy, demuestro que no empeoró, repito.

---
---

## 🎬 CIERRE

Bueno mi gente, eso fue todo lo que teníamos para hoy sobre algoritmos greedy.

Recapitulando: vimos que los algoritmos greedy son poderosos y eficientes, pero que su verdadero valor solo aparece cuando podemos **demostrar** que son correctos. Para eso tenemos dos herramientas fundamentales:

- **Greedy Stays Ahead:** demostramos que en cada paso el greedy está al menos tan bien posicionado como cualquier solución óptima.
- **Argumento de Intercambio:** demostramos que cualquier solución óptima puede transformarse en la greedy sin empeorar.

Vimos estos conceptos en acción en seis problemas: selección de actividades, planificación con deadlines, el viaje a Mar del Plata, el cambio de monedas, la mochila fraccionaria, la minimización del tiempo de espera, y la minimización del producto escalar.

Y aprendimos que el greedy falla cuando el problema no tiene la "propiedad de elección greedy" o la "subestructura óptima". El contraejemplo siempre existe si fallamos.

Lo más importante que me pueden llevar de acá es esto:

> En algoritmos, **"parece correcto"** no es lo mismo que **"es correcto"**. El trabajo formal es lo que hace la diferencia.

Los veo en el próximo. Cuídense.

---

## 📚 CONTENIDO EXTRA

### Ejercicios para practicar:

- **Selección de actividades:** Implementar la solución y verificar con casos de prueba propios.
- **Problema de Huffman:** Un algoritmo greedy clásico para compresión de datos. Busquen "Huffman coding" y traten de entender por qué es óptimo.
- **Árboles de expansión mínima (Prim y Kruskal):** Dos algoritmos greedy clásicos sobre grafos que van a ver más adelante.
- **Problema de la estación de servicio:** Implementar el viaje a Mar del Plata con verificación de si existe solución.

### Recursos recomendados:

- El capítulo de Greedy del libro "Algorithm Design" de Kleinberg & Tardos es, sin dudas, el mejor tratamiento del tema que existe. Los argumentos de intercambio están explicados con una claridad brutal.
- Para practicar problemas de Greedy en competitive programming: Codeforces tiene categoría "greedy" con cientos de problemas ordenados por dificultad.

### Un último pensamiento:

Los algoritmos Greedy son la puerta de entrada a resultados mucho más profundos en teoría de algoritmos: teoría de matroides (una estructura algebraica que caracteriza exactamente cuándo el greedy funciona), algoritmos de aproximación, y más. Si este tema les gustó, el camino está abierto.
