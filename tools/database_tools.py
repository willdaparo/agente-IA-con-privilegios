from app.services.database_service import get_connection


def consultar_pedido(numero_pedido):
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
            WHERE p.id = %s
        """

        cursor.execute(query, (numero_pedido,))

        resultado = cursor.fetchone()

        return resultado

    except Exception as error:
        raise Exception(
            f"Error al consultar el pedido: {error}"
        )

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()