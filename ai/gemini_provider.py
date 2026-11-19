from google import genai
import json

from app.config.settings import (
    GEMINI_API_KEY,
    AI_MODEL
)

from app.ai.tool_definitions import (
    TOOL_CONSULTAR_BASE_DATOS
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def ejecutar_conversacion(
    pregunta,
    instrucciones,
    ejecutar_tool
):

    interaction = client.interactions.create(
        model=AI_MODEL,
        input=pregunta,
        system_instruction=instrucciones,
        tools=[
            TOOL_CONSULTAR_BASE_DATOS
        ]
    )

    max_iteraciones = 5

    for _ in range(max_iteraciones):

        function_calls = []

        for step in interaction.steps:

            if step.type == "function_call":
                function_calls.append(step)

        # Gemini ya respondió directamente
        if not function_calls:
            return interaction

        resultados = []

        for function_call in function_calls:

            nombre = function_call.name
            argumentos = function_call.arguments

            print("\nTOOL SOLICITADA:")
            print(nombre)

            print("\nARGUMENTOS:")
            print(argumentos)

            resultado = ejecutar_tool(
                nombre,
                argumentos
            )

            print("\nRESULTADO DE LA TOOL:")
            print(resultado)

            resultados.append({
                "type": "function_result",
                "name": nombre,
                "call_id": function_call.id,
                "result": [
                    {
                        "type": "text",
                        "text": json.dumps(
                            resultado,
                            ensure_ascii=False,
                            default=str
                        )
                    }
                ]
            })

        interaction = client.interactions.create(
            model=AI_MODEL,
            previous_interaction_id=interaction.id,
            input=resultados,
            tools=[
                TOOL_CONSULTAR_BASE_DATOS
            ]
        )

    raise Exception(
        "Se alcanzó el máximo de iteraciones "
        "de herramientas."
    )