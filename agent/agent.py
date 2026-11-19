from app.authorization.query_context import (
    obtener_contexto_sql
)


def construir_contexto_agente(contexto_usuario):

    contexto_sql = obtener_contexto_sql(
        contexto_usuario
    )

    contexto = {
        "usuario": {
            "id": contexto_usuario["usuario"]["id"],
            "nombre": contexto_usuario["usuario"]["nombre"]
        },

        "roles": [
            rol["nombre"]
            for rol in contexto_usuario["roles"]
        ],

        "permisos": [
            permiso["nombre"]
            for permiso in contexto_usuario["permisos"]
        ],

        "database": contexto_sql
    }

    return contexto


def construir_instrucciones_agente(contexto):

    instrucciones = f"""
Eres un agente empresarial.

Tu función es ayudar al usuario utilizando
únicamente los recursos autorizados.

USUARIO:
{contexto["usuario"]["nombre"]}

ROLES:
{contexto["roles"]}

PERMISOS:
{contexto["permisos"]}

BASE DE DATOS AUTORIZADA:
{contexto["database"]}

REGLAS DE BASE DE DATOS:

1. Solo puedes utilizar las tablas indicadas
   en BASE DE DATOS AUTORIZADA.

2. Solo puedes utilizar las columnas indicadas
   para cada tabla.

3. Nunca inventes tablas.

4. Nunca inventes columnas.

5. Nunca supongas que existen tablas que no
   aparecen en el esquema autorizado.

6. Cuando necesites información de la base de datos,
   utiliza consultar_base_datos.

7. Genera únicamente consultas SELECT.

8. No inventes información.

9. Si no puedes responder utilizando los recursos
   autorizados, informa que no tienes acceso
   a esa información.
"""

    return instrucciones