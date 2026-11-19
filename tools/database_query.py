from app.services.database_service import get_connection

from app.authorization.sql_validator import (
    validar_sql
)


def ejecutar_consulta_lectura(sql, rol):

    # -----------------------------------
    # Validar SQL
    # -----------------------------------

    validar_sql(
        sql,
        rol
    )

    connection = None
    cursor = None

    try:

        connection = get_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        cursor.execute(sql)

        return cursor.fetchall()

    except Exception as error:

        raise Exception(
            f"Error ejecutando consulta: {error}"
        )

    finally:

        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()