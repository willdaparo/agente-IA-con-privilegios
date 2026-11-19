from app.services.database_service import get_connection


def obtener_usuario_por_email(email):
    connection = None
    cursor = None

    try:
        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                id,
                nombre,
                email,
                password_hash,
                activo
            FROM usuarios
            WHERE email = %s
            LIMIT 1
        """

        cursor.execute(query, (email,))

        return cursor.fetchone()

    except Exception as error:
        raise Exception(
            f"Error al obtener usuario: {error}"
        )

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()


def obtener_roles_usuario(usuario_id):
    connection = None
    cursor = None

    try:
        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                r.id,
                r.nombre,
                r.descripcion
            FROM roles r
            INNER JOIN usuario_roles ur
                ON r.id = ur.rol_id
            WHERE ur.usuario_id = %s
        """

        cursor.execute(query, (usuario_id,))

        return cursor.fetchall()

    except Exception as error:
        raise Exception(
            f"Error al obtener roles del usuario: {error}"
        )

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()


def obtener_permisos_usuario(usuario_id):
    connection = None
    cursor = None

    try:
        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT DISTINCT
                p.id,
                p.nombre,
                p.descripcion
            FROM permisos p
            INNER JOIN rol_permisos rp
                ON p.id = rp.permiso_id
            INNER JOIN usuario_roles ur
                ON rp.rol_id = ur.rol_id
            WHERE ur.usuario_id = %s
        """

        cursor.execute(query, (usuario_id,))

        return cursor.fetchall()

    except Exception as error:
        raise Exception(
            f"Error al obtener permisos del usuario: {error}"
        )

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()