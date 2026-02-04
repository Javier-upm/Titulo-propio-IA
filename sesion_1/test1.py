# test1.py
# Tests (caja negra) para Sesion_1_basicas_1.ipynb

def _assert(cond, msg):
    if not cond:
        raise AssertionError(msg)

def check_ej1(a, b, b_cap, suma):
    _assert(isinstance(a, int), "a debe ser int")
    _assert(isinstance(b, str), "b debe ser str")
    _assert(isinstance(b_cap, str), "b_cap debe ser str")
    _assert(isinstance(suma, int), "suma debe ser int")
    _assert(suma == a + 10, "suma incorrecta")
    _assert(b_cap == b.capitalize(), "b_cap incorrecta")

def check_ej2(sublista, ultimo, reversa, lista):
    _assert(isinstance(lista, list), "lista debe ser list")
    _assert(isinstance(sublista, list), "sublista debe ser list")
    _assert(ultimo == lista[-1], "ultimo incorrecto")
    _assert(sublista == lista[1:3], "sublista incorrecta")
    _assert(reversa == list(reversed(lista)), "reversa incorrecta")

def check_ej3(lista, lista_copia):
    _assert(isinstance(lista, list) and isinstance(lista_copia, list), "deben ser listas")
    _assert(len(lista) == 3 and len(lista_copia) == 3, "longitud incorrecta")
    _assert(lista[0] == 999, "no se ha modificado lista[0] a 999")
    _assert(lista_copia[0] == 1, "lista_copia cambió: no es copia independiente")
    _assert(lista_copia is not lista, "lista_copia no puede ser la misma referencia")

def check_ej4(pi_val, claves, dicc):
    _assert(isinstance(dicc, dict), "dicc debe ser dict")
    _assert(abs(pi_val - dicc["pi"]) < 1e-12, "pi_val incorrecto")
    _assert(isinstance(claves, list), "claves debe ser list")
    _assert(claves == sorted(list(dicc.keys())), "claves debe estar ordenada alfabéticamente")

def check_ej5(n, suma_multiplos):
    _assert(n == 45, "n debe ser 45 en este ejercicio")
    _assert(isinstance(suma_multiplos, int), "suma_multiplos debe ser int")
    ref = sum(i for i in range(n + 1) if i % 3 == 0)
    _assert(suma_multiplos == ref, "suma_multiplos incorrecta")

def check_ej6(funcion):
    _assert(callable(funcion), "funcion debe ser callable")

    # Caso positivo
    x = 4
    y = funcion(x)
    _assert(isinstance(y, (int, float)), "para x>=0 debe devolver número")
    ref = (x ** 0.5) + (x ** 2)
    _assert(abs(y - ref) < 1e-9, "valor incorrecto para x=4")

    # Caso borde x=0
    y0 = funcion(0)
    _assert(isinstance(y0, (int, float)), "para x=0 debe devolver número")
    _assert(abs(y0 - 0.0) < 1e-9, "valor incorrecto para x=0")

    # Negativo: debe devolver None
    _assert(funcion(-1) is None, "para x<0 debe devolver None")

def check_ej7(primo):
    _assert(callable(primo), "primo debe ser callable")

    # Caso positivo
    y = primo(23)
    _assert(y is True, "para n=23 debe devolver True")

    # Caso borde
    y0 = primo(1)
    _assert(y0 is False, "para n=1 debe devolver False")

    # Caso negativo
    y = primo(87)
    _assert(y is False, "para n=87 debe devolver False")
