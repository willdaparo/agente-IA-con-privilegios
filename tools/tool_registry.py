from app.authorization.policy_engine import tiene_permiso

from app.tools.database_tools import consultar_pedido

from app.tools.sales_tools import (
    consultar_cliente,
    consultar_ventas
)

from app.tools.database_query import (
    ejecutar_consulta_lectura
)


TOOLS = {

    "consultar_pedido": {
        "funcion": consultar_pedido,
        "permiso": "consultar_pedidos"
    },

    "consultar_cliente": {
        "funcion": consultar_cliente,
        "permiso": "consultar_clientes"
    },

    "consultar_ventas": {
        "funcion": consultar_ventas,
        "permiso": "consultar_ventas"
    },

    "consultar_base_datos": {
        "funcion": ejecutar_consulta_lectura,
        "permiso": "consultar_ventas"
    }

}


def ejecutar_tool(
    nombre_tool,
    contexto,
    argumentos
):

    # 1. Verificar que la herramienta existe
    if nombre_tool not in TOOLS:

        raise Exception(
            f"La herramienta '{nombre_tool}' no existe."
        )


    # 2. Obtener configuración de la herramienta
    tool = TOOLS[nombre_tool]


    # 3. Obtener permiso requerido
    permiso_requerido = tool["permiso"]


    # 4. Verificar permiso
    if not tiene_permiso(
        contexto,
        permiso_requerido
    ):

        raise PermissionError(
            f"Acceso denegado. "
            f"Se requiere el permiso: "
            f"{permiso_requerido}"
        )


    # 5. Obtener función
    funcion = tool["funcion"]


    # 6. Ejecutar herramienta
    if nombre_tool == "consultar_base_datos":

        roles = contexto["roles"]

        if not roles:

            raise PermissionError(
                "El usuario no tiene un rol autorizado."
            )

        rol = roles[0]["nombre"]

        return funcion(
            rol=rol,
            **argumentos
        )


    # 7. Ejecutar herramientas normales
    return funcion(
        **argumentos
    )