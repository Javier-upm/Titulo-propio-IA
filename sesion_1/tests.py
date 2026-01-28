# tests.py
# Tests opacos para Sesión 1 · Python básico

# --------------------------------------------------
# Utilidades internas
# --------------------------------------------------

def _assert(cond, msg):
    if not cond:
        raise AssertionError(msg)


# --------------------------------------------------
# Ejercicio 1
# --------------------------------------------------

def check_ej1(edad, altura, nombre, es_estudiante):
    _assert(isinstance(edad, int), "edad debe ser int")
    _assert(isinstance(altura, float), "altura debe ser float")
    _assert(isinstance(nombre, str), "nombre debe ser str")
    _assert(isinstance(es_estudiante, bool), "es_estudiante debe ser bool")


# --------------------------------------------------
# Ejercicio 2
# --------------------------------------------------

def check_ej2(slug):
    _assert(isinstance(slug, str), "slug debe ser str")
    _assert(slug == slug.lower(), "slug debe estar en minúsculas")
    _assert(" " not in slug, "slug no debe contener espacios")
    _assert("--" not in slug, "slug mal formateado")
    _assert(len(slug) > 0, "slug vacío")


# --------------------------------------------------
# Ejercicio 3
# --------------------------------------------------

def check_ej3(media, min_nota, max_nota, notas):
    _assert(isinstance(notas, list) and len(notas) > 0, "notas debe ser lista no vacía")

    for v in (media, min_nota, max_nota):
        _assert(isinstance(v, (int, float)), "valores deben ser numéricos")

    _assert(min_nota <= media <= max_nota, "orden incorrecto (min ≤ media ≤ max)")

    ref_media = sum(notas) / len(notas)
    _assert(abs(media - ref_media) < 1e-9, "media incorrecta")
    _assert(min_nota in notas, "min_nota no coincide con los datos")
    _assert(max_nota in notas, "max_nota no coincide con los datos")


# --------------------------------------------------
# Ejercicio 4
# --------------------------------------------------

def check_ej4(func):
    _assert(callable(func), "contar_aprobados debe ser una función")

    _assert(func([]) == 0, "caso lista vacía incorrecto")
    _assert(func([4, 5, 6]) == 2, "conteo incorrecto")
    _assert(func([5, 5, 5]) == 3, "conteo incorrecto")
    _assert(func([0, 10]) == 1, "conteo incorrecto")


# --------------------------------------------------
# Ejercicio 5
# --------------------------------------------------

def check_ej5(func):
    _assert(callable(func), "normalizar_lista debe ser una función")

    v = [1, 2, 3, 4, 5]
    nv = func(v)

    _assert(isinstance(nv, list), "salida debe ser lista")
    _assert(len(nv) == len(v), "longitud incorrecta")

    mean = sum(nv) / len(nv)
    var = sum((x - mean) ** 2 for x in nv) / len(nv)
    std = var ** 0.5

    _assert(abs(mean) < 1e-9, "media no es 0")
    _assert(abs(std - 1) < 1e-9, "desviación no es 1")

    _assert(func([3, 3, 3]) == [0.0, 0.0, 0.0], "caso desviación cero incorrecto")


# --------------------------------------------------
# Ejercicio 6
# --------------------------------------------------

def check_ej6(ranking, ventas):
    _assert(isinstance(ranking, list), "ranking debe ser lista")
    _assert(len(ranking) == len(ventas), "tamaño incorrecto")

    productos = [p for p, _ in ranking]
    _assert(set(productos) == set(ventas.keys()), "productos incorrectos")

    unidades = [u for _, u in ranking]
    _assert(unidades == sorted(unidades, reverse=True), "orden incorrecto")


# --------------------------------------------------
# Ejercicio 7
# --------------------------------------------------

def check_ej7(func):
    _assert(callable(func), "get_safe debe ser una función")

    d = {"a": 1}
    _assert(func(d, "a") == 1, "valor existente incorrecto")
    _assert(func(d, "b") is None, "default None incorrecto")
    _assert(func(d, "b", 0) == 0, "default personalizado incorrecto")


# --------------------------------------------------
# Mini-reto
# --------------------------------------------------

def check_mini_reto(f_filtrar, f_media, f_topk, data):
    _assert(callable(f_filtrar), "filtrar_por_nota debe ser función")
    _assert(callable(f_media), "media_notas debe ser función")
    _assert(callable(f_topk), "top_k debe ser función")

    filtrados = f_filtrar(data, 7)
    _assert(all(x["nota"] >= 7 for x in filtrados), "filtrado incorrecto")

    m = f_media(data)
    ref = sum(x["nota"] for x in data) / len(data)
    _assert(abs(m - ref) < 1e-9, "media_notas incorrecta")

    top2 = f_topk(data, 2)
    _assert(len(top2) == 2, "top_k tamaño incorrecto")
    _assert(top2[0]["nota"] >= top2[1]["nota"], "orden top_k incorrecto")

    _assert(f_topk(data, 0) == [], "caso k=0 incorrecto")


# --------------------------------------------------
# Ejercicio 8 (NumPy)
# --------------------------------------------------

def check_ej8_numpy(X, primera_col, fila_2):
    import numpy as np

    _assert(isinstance(X, np.ndarray), "X debe ser np.ndarray")
    _assert(X.shape == (3, 2), "shape de X incorrecto")

    _assert(isinstance(primera_col, np.ndarray), "primera_col debe ser array")
    _assert(isinstance(fila_2, np.ndarray), "fila_2 debe ser array")

    _assert((primera_col == X[:, 0]).all(), "primera_col incorrecta")
    _assert((fila_2 == X[1]).all(), "fila_2 incorrecta")
