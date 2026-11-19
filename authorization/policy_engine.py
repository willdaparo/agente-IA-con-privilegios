from app.identity.users import (
    obtener_roles_usuario,
    obtener_permisos_usuario
)


def obtener_contexto_usuario(usuario):
    """
    Construye el contexto de seguridad del usuario.

    El contexto contiene:
    - usuario
    - roles
    - permisos
    """

    if not usuario:
        raise Exception("Usuario no válido")

    if not usuario["activo"]:
        raise Exception("El usuario está inactivo")

    roles = obtener_roles_usuario(usuario["id"])
    permisos = obtener_permisos_usuario(usuario["id"])

    contexto = {
        "usuario": usuario,
        "roles": roles,
        "permisos": permisos
    }

    return contexto


def tiene_permiso(contexto, permiso):
    """
    Determina si el usuario posee un permiso específico.
    """

    permisos = contexto["permisos"]

    for item in permisos:
        if item["nombre"] == permiso:
            return True

    return False