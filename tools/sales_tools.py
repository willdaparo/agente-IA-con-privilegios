from app.services.database_service import get_connection


def consultar_cliente(cliente_id):
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
                telefono,
                activo,
                fecha_registro
            FROM clientes
            WHERE id = %s
        """

        cursor.execute(query, (cliente_id,))

        return cursor.fetchone()

    except Exception as error:
        raise Exception(
            f"Error al consultar cliente: {error}"
        )

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()


def consultar_ventas():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                p.id,
                c.nombre AS cliente,
                p.producto,
                p.estado,
                p.fecha_pedido,
                p.valor
            FROM pedidos p
            INNER JOIN clientes c
                ON p.cliente_id = c.id
            ORDER BY p.fecha_pedido DESC
        """

        cursor.execute(query)

        return cursor.fetchall()

    except Exception as error:
        raise Exception(
            f"Error al consultar ventas: {error}"
        )

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()