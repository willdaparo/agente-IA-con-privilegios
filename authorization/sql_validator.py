import sqlglot
from sqlglot import exp

from app.authorization.database_policy import DATABASE_POLICY


def validar_sql(sql, rol):

    # -----------------------------------
    # 1. Obtener tablas autorizadas
    # -----------------------------------

    politica = DATABASE_POLICY.get(rol)

    if not politica:
        raise PermissionError(
            f"El rol '{rol}' no tiene política de base de datos."
        )

    tablas_autorizadas = set(
        politica.get("tables", {}).keys()
    )

    # -----------------------------------
    # 2. Analizar SQL
    # -----------------------------------

    try:
        expresiones = sqlglot.parse(
            sql,
            read="mysql"
        )

    except Exception as error:
        raise ValueError(
            f"SQL inválido: {error}"
        )

    # -----------------------------------
    # 3. Solo una sentencia
    # -----------------------------------

    if len(expresiones) != 1:
        raise PermissionError(
            "Solo se permite una sentencia SQL."
        )

    sentencia = expresiones[0]

    # -----------------------------------
    # 4. Solo SELECT
    # -----------------------------------

    if not isinstance(sentencia, exp.Select):

        raise PermissionError(
            "Solo se permiten consultas SELECT."
        )

    # -----------------------------------
    # 5. Obtener tablas utilizadas
    # -----------------------------------

    tablas_utilizadas = {
        tabla.name
        for tabla in sentencia.find_all(exp.Table)
    }

    # -----------------------------------
    # 6. Verificar tablas
    # -----------------------------------

    tablas_no_autorizadas = (
        tablas_utilizadas - tablas_autorizadas
    )

    if tablas_no_autorizadas:

        raise PermissionError(
            "La consulta intenta acceder a "
            f"tablas no autorizadas: "
            f"{', '.join(tablas_no_autorizadas)}"
        )

    return True