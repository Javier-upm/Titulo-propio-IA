def _assert(cond, msg):
    if not cond:
        raise AssertionError(msg)

def check_1(df, shape, columnas, nulos):
    _assert(shape == df.shape, "shape incorrecto")
    _assert(isinstance(columnas, list), "columnas debe ser una lista")
    _assert(columnas == list(df.columns), "lista de columnas incorrecta (orden)")
    _assert(isinstance(nulos, dict), "nulos debe ser un diccionario")
    ref = df.isna().sum().to_dict()
    _assert(nulos == ref, "diccionario de nulos incorrecto")

def check_2(df, cols_notas, media_asignaturas, num_aprobados_todo):
    import pandas as pd
    import numpy as np
    _assert(isinstance(media_asignaturas, pd.Series), "media_asignaturas debe ser pd.Series")
    _assert(list(media_asignaturas.index) == cols_notas, "índices de media_asignaturas incorrectos")
    ref_media = df[cols_notas].mean()
    _assert(np.allclose(media_asignaturas.values, ref_media.values, equal_nan=True), "medias incorrectas")

    ref_aprobados = ((df[cols_notas] > 5).all(axis=1)).sum()
    _assert(num_aprobados_todo == ref_aprobados, "num_aprobados_todo incorrecto")

    _assert("Nota media" in df.columns, "falta la columna 'Nota media' en df")
    ref_nm = df[cols_notas].mean(axis=1)
    _assert(np.allclose(df["Nota media"].values, ref_nm.values, equal_nan=True), "'Nota media' incorrecta")

def check_3(df, media_mate_por_procedencia, media_mate_por_padres):
    import pandas as pd
    import numpy as np
    _assert(isinstance(media_mate_por_procedencia, pd.Series), "media_mate_por_procedencia debe ser Series")
    _assert(isinstance(media_mate_por_padres, pd.Series), "media_mate_por_padres debe ser Series")

    ref1 = df.groupby("procedencia")["nota_matematicas"].mean()
    ref2 = df.groupby("nivel_educativo_padres")["nota_matematicas"].mean()

    # Alineación por índice (puede haber NaN en procedencia)
    _assert(media_mate_por_procedencia.index.equals(ref1.index), "índices procedencia incorrectos")
    _assert(np.allclose(media_mate_por_procedencia.values, ref1.values, equal_nan=True), "medias por procedencia incorrectas")

    _assert(media_mate_por_padres.index.equals(ref2.index), "índices padres incorrectos")
    _assert(np.allclose(media_mate_por_padres.values, ref2.values, equal_nan=True), "medias por padres incorrectas")

def check_4(df, cols_notas, df_dropna, df_clean, df_sin_nulos):
    import pandas as pd
    import numpy as np

    _assert(isinstance(df_dropna, pd.DataFrame), "df_dropna debe ser DataFrame")
    _assert(df_dropna.isna().sum().sum() == 0, "df_dropna no debe tener NaN (usa dropna)")

    _assert(isinstance(df_clean, pd.DataFrame), "df_clean debe ser DataFrame")
    _assert(all(c in df_clean.columns for c in cols_notas), "df_clean debe contener las columnas de notas")
    _assert("Nota media" in df_clean.columns, "df_clean debe contener 'Nota media'")

    # Outliers corregidos: ninguna nota > 10
    _assert((df_clean[cols_notas] <= 10).all().all(), "quedan outliers > 10 sin corregir")

    # Notas sin NaN tras imputación
    _assert(df_clean[cols_notas].isna().sum().sum() == 0, "quedan NaN en notas tras imputación")

    # Nota media recalculada correctamente
    ref_nm = df_clean[cols_notas].mean(axis=1)
    _assert(np.allclose(df_clean["Nota media"].values, ref_nm.values, equal_nan=True), "'Nota media' no recalculada correctamente")

    _assert(isinstance(df_sin_nulos, pd.DataFrame), "df_sin_nulos debe ser DataFrame")
    _assert(df_sin_nulos.isna().sum().sum() == 0, "df_sin_nulos no debe tener NaN")

def check_5(df_encoded):
    import pandas as pd
    _assert(isinstance(df_encoded, pd.DataFrame), "df_encoded debe ser DataFrame")
    _assert(df_encoded.select_dtypes(include="object").shape[1] == 0, "quedan columnas categóricas (object)")

    # columnas esperadas (al menos)
    for col in ["come_en_centro", "curso_preparacion", "nivel_educativo_padres"]:
        _assert(col in df_encoded.columns, f"falta columna {col}")

    # binarios 0/1
    for col in ["come_en_centro", "curso_preparacion"]:
        vals = set(df_encoded[col].dropna().unique().tolist())
        _assert(vals.issubset({0, 1}), f"{col} debe ser 0/1")

    # ordinal padres 0..3
    vals = set(df_encoded["nivel_educativo_padres"].dropna().unique().tolist())
    _assert(vals.issubset({0, 1, 2, 3}), "nivel_educativo_padres debe estar en {0,1,2,3}")

    # dummies procedencia
    dummy_cols = [c for c in df_encoded.columns if c.startswith("procedencia_")]
    _assert(len(dummy_cols) >= 3, "faltan columnas one-hot de procedencia (procedencia_*)")

def check_6(df_final, num_cols):
    import pandas as pd
    import numpy as np
    _assert(isinstance(df_final, pd.DataFrame), "df_final debe ser DataFrame")
    for c in num_cols:
        _assert(c in df_final.columns, f"falta {c} en df_final")

    mu = df_final[num_cols].mean()
    sigma = df_final[num_cols].std(ddof=0)

    _assert(np.allclose(mu.values, 0, atol=1e-6), "media no ~0 (estandarización)")
    _assert(np.allclose(sigma.values, 1, atol=1e-6), "std no ~1 (usa std(ddof=0))")
