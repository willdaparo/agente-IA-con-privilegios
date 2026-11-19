from app.authorization.database_policy import DATABASE_POLICY


def obtener_contexto_sql(contexto_usuario):

    tablas = {}

    for rol in contexto_usuario["roles"]:

        nombre_rol = rol["nombre"]

        politica = DATABASE_POLICY.get(
            nombre_rol,
            {}
        )

        tablas_rol = politica.get(
            "tables",
            {}
        )

        for tabla, columnas in tablas_rol.items():

            tablas[tabla] = columnas

    return {
        "tables": tablas
    }