DATABASE_POLICY = {
    "ventas": {
        "tables": {
            "clientes": [
                "id",
                "nombre",
                "email",
                "telefono",
                "activo",
                "fecha_registro"
            ],

            "pedidos": [
                "id",
                "cliente_id",
                "producto",
                "estado",
                "fecha_pedido",
                "valor"
            ]
        }
    },

    "rrhh": {
        "tables": {
            # Más adelante agregaremos
            # las tablas de RRHH.
        }
    },

    "finanzas": {
        "tables": {
            # Más adelante agregaremos
            # las tablas financieras.
        }
    }
}