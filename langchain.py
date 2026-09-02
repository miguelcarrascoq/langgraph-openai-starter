# -*- coding: utf-8 -*-
"""Ejemplo LangGraph con OpenAI (ejecución local).

Setup (macOS con Python de Homebrew requiere un venv):

    python3 -m venv .venv
    source .venv/bin/activate
    pip install langgraph langchain-openai python-dotenv

Configura OPENAI_API_KEY en .env o como variable de entorno.
"""

# https://www.aluracursos.com/blog/langgraph-que-es-como-usarlo-y-sus-funcionalidades

import os
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    raise RuntimeError(
        "OPENAI_API_KEY no configurada. Define la variable en .env o en el entorno."
    )

# Proyecto LangGraph
# Importaciones principales
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from typing import TypedDict
# Definición del estado global
class Estado(TypedDict):
    pregunta: str
    respuesta: str
# Iniciando el modelo LLM
modelo = ChatOpenAI(model="gpt-4o-mini")
# Nodo 1: Recibe y muestra la pregunta
def nodo_recibir_pregunta(state: Estado):
    print("🔹 Pregunta recibida:", state["pregunta"])
    return state
# Nodo 2: Genera la respuesta vía LLM y la guarda en el estado
def nodo_generar_respuesta(state: Estado):
    pregunta = state["pregunta"]
    respuesta = modelo.invoke(pregunta)  # Llamada al LLM
    state["respuesta"] = respuesta.content
    print("🔹 Respuesta generada con éxito.")
    return state
# Construyendo el grafo
grafo = StateGraph(Estado)
grafo.add_node("recibir_pregunta", nodo_recibir_pregunta)
grafo.add_node("generar_respuesta", nodo_generar_respuesta)
grafo.add_edge("recibir_pregunta", "generar_respuesta")
grafo.add_edge("generar_respuesta", END)
# Definiendo el inicio del flujo
grafo.set_entry_point("recibir_pregunta")
# Compila el grafo
app = grafo.compile()

try:
    with open("graph.png", "wb") as f:
        f.write(app.get_graph().draw_mermaid_png(max_retries=3, retry_delay=1.0))
    print("Grafo guardado en graph.png")
except Exception as e:
    print(f"No se pudo guardar graph.png: {e}")

# Ejecutando el grafo
estado_inicial = {
    "pregunta": "Explica qué es LangGraph de forma sencilla.",
    "respuesta": ""
}
resultado = app.invoke(estado_inicial)
print("\n===== Respuesta del agente =====")
print(resultado["respuesta"])