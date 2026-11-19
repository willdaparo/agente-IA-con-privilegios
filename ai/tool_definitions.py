TOOL_CONSULTAR_BASE_DATOS = {
    "type": "function",

    "name": "consultar_base_datos",

    "description": """
    Consulta información de la base de datos empresarial.

    Utiliza esta herramienta cuando la pregunta del usuario
    requiera información almacenada en la base de datos.

    Debes generar únicamente una consulta SQL SELECT.
    La aplicación se encargará de validar los permisos
    antes de ejecutar la consulta.
    """,

    "parameters": {
        "type": "object",

        "properties": {
            "sql": {
                "type": "string",
                "description": """
                Consulta SQL SELECT necesaria para responder
                la pregunta del usuario.
                """
            }
        },

        "required": ["sql"]
    }
}