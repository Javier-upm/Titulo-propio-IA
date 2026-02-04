# tests2.py
# Tests (caja negra) para Sesion_1_basicas_2.ipynb

def _assert(cond, msg):
    if not cond:
        raise AssertionError(msg)


def check_ej1_vectoriza(A, B, C_loop, C_vec):
    import numpy as np
    _assert(isinstance(C_vec, np.ndarray), "C_vec debe ser np.ndarray")
    _assert(C_vec.shape == A.shape, "shape incorrecta en C_vec")
    _assert(np.allclose(C_vec, C_loop), "C_vec no coincide con el resultado del bucle")


def check_ej2a_A3(A3):
    import numpy as np
    _assert(isinstance(A3, np.ndarray), "A3 debe ser np.ndarray")
    _assert(A3.shape == (2, 3, 4), "A3 debe tener shape (2,3,4)")

    ii = np.arange(1, 3)[:, None, None]
    jj = np.arange(1, 4)[None, :, None]
    kk = np.arange(1, 5)[None, None, :]
    ref = 100 * ii + 10 * jj + kk

    _assert(np.array_equal(A3, ref), "A3 no cumple la fórmula indicada")


def check_ej2b_mask(A3, X, A_masked):
    import numpy as np
    _assert(isinstance(A_masked, np.ndarray), "A_masked debe ser np.ndarray")
    _assert(A_masked.shape == (2, 3, 4), "A_masked debe tener shape (2,3,4)")

    ref = A3 * X
    _assert(np.array_equal(A_masked, ref), "A_masked incorrecto (debe ser A3 * X)")

    for t in range(2):
        M = A_masked[t]
        nz = np.argwhere(M != 0)
        _assert(nz.shape[0] == 3, "deben quedar exactamente 3 elementos no nulos por matriz")
        _assert(set(map(tuple, nz)) == {(0,0), (1,1), (2,2)}, "posiciones no nulas incorrectas")


def check_ej3_fillna_mean(df2, df_filled):
    import pandas as pd
    import numpy as np

    _assert(isinstance(df_filled, pd.DataFrame), "df_filled debe ser DataFrame")
    _assert(df_filled.shape == df2.shape, "shape de df_filled incorrecta")
    _assert(df_filled.isna().sum().sum() == 0, "df_filled no debe contener NaN")

    means = df2.mean(numeric_only=True)
    for r, c in [(1, "edad"), (2, "nota")]:
        _assert(abs(df_filled.loc[r, c] - means[c]) < 1e-12, f"NaN en {c} no rellenado con la media correcta")

    _assert((df_filled["nombre"] == df2["nombre"]).all(), "columna 'nombre' no debe cambiar")
    _assert((df_filled["grupo"] == df2["grupo"]).all(), "columna 'grupo' no debe cambiar")



def check_ej4_miniscaler(MiniScaler):
    import numpy as np
    _assert(callable(MiniScaler), "MiniScaler debe ser una clase/constructor")

    X = np.array([[1.0, 10.0],
                  [2.0, 20.0],
                  [3.0, 30.0]])

    sc = MiniScaler()
    _assert(hasattr(sc, "fit") and hasattr(sc, "transform") and hasattr(sc, "fit_transform"),
            "MiniScaler debe tener fit/transform/fit_transform")

    Xs = sc.fit_transform(X)
    _assert(isinstance(Xs, np.ndarray), "fit_transform debe devolver np.ndarray")
    _assert(Xs.shape == X.shape, "shape de salida incorrecta")

    mean = X.mean(axis=0)
    std = X.std(axis=0)
    std = np.where(std == 0, 1.0, std)
    ref = (X - mean) / std

    _assert(np.allclose(sc.mean_, mean), "mean_ incorrecta tras fit")
    _assert(np.allclose(sc.std_, std), "std_ incorrecta tras fit")
    _assert(np.allclose(Xs, ref), "transformación incorrecta")

    X2 = np.array([[5.0, 1.0],
                   [5.0, 2.0],
                   [5.0, 3.0]])
    sc2 = MiniScaler()
    X2s = sc2.fit_transform(X2)
    _assert(np.isfinite(X2s).all(), "no debe producir inf/NaN")
    _assert(np.allclose(X2s[:, 0], 0.0), "columna constante debe quedar a ceros tras escalado")
