from math import inf

"""
Resolvemos el ejercicio https://codeforces.com/problemset/gymProblem/102961/H
"""

"""
Queremos D&C: la idea es dividir en dos partes y buscar los indices donde se encuentra 
el subarray de suma máxima, luego queremos combinar el menor del "lado izquierdo" con el
mayor índice del "lado derecho"

Ejemplo:

8
[-1 3 -2 5] [3 -5 2 2]
    |        |            
    i        j

return max(suma_izq, suma_der, suma_medio)
"""

def tomar_entrada()->tuple[int, list[int]]:

    n:int = int(input())
    array:list[int] = list(map(int, input().split(" ")))

    return n, array

def maximo_subarray(i:int, j:int, array:list[int]):
    
    # Conquistar
    if i == j:
        return array[i]
    
    # Dividir
    medio:int = (i + j) // 2
    mitad_izquierda:int = maximo_subarray(i, medio, array)
    mitad_derecho:int = maximo_subarray(medio+1, j, array)

    acc:int = 0
    suma_izquierda:int = -inf
    for k in range(medio, i-1, -1):
        acc +=  array[k]
        suma_izquierda = max(suma_izquierda, acc)
    
    acc:int = 0
    suma_derecha:int = -inf
    for k in range(medio+1, j+1):
        acc +=  array[k]
        suma_derecha = max(suma_derecha, acc)

    suma_medio:int = suma_izquierda + suma_derecha

    # Combine
    return max(mitad_izquierda, mitad_derecho, suma_medio)

def main():
    n, array = tomar_entrada()
    print(maximo_subarray(0, n-1, array))

if __name__ == "__main__":
    main()