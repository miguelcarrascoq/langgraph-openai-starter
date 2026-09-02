# LangGraph + OpenAI (ejemplo local)

Ejemplo mínimo de un grafo con [LangGraph](https://github.com/langchain-ai/langgraph) y [OpenAI](https://platform.openai.com/) via LangChain. El flujo tiene dos nodos: recibir una pregunta y generar una respuesta con un LLM.

## Requisitos

- Python 3.10+
- Cuenta OpenAI con API key

## Setup local (macOS / Homebrew)

En macOS con Python gestionado por Homebrew, usa un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuración de la API key

1. Copia la plantilla de variables de entorno:

   ```bash
   cp .env.example .env
   ```

2. Edita `.env` y define tu clave:

   ```
   OPENAI_API_KEY=sk-...
   ```

**Importante:** nunca subas `.env` al repositorio. Solo commitea `.env.example`.

## Ejecución

Con el venv activado:

```bash
python langchain.py
```

El script invoca el grafo con una pregunta de ejemplo y muestra la respuesta del modelo (`gpt-4o-mini`).

## Notebook (Google Colab)

[`langchain.ipynb`](langchain.ipynb) es la versión original para Colab. Si lo abres en Colab, configura el secret `OPENAI_API_KEY` en el panel de Secrets del notebook. Para uso local, adapta la celda de secrets y usa `.env` como en el script.

## Estructura del proyecto

| Archivo            | Descripción                                      |
|--------------------|--------------------------------------------------|
| `langchain.py`     | Script principal (grafo LangGraph + OpenAI)      |
| `langchain.ipynb`  | Notebook original (Colab)                        |
| `requirements.txt` | Dependencias Python                              |
| `.env.example`     | Plantilla para `OPENAI_API_KEY`                  |

## Referencia

Basado en el artículo de Alura sobre LangGraph: [LangGraph: qué es, cómo usarlo y sus funcionalidades](https://www.aluracursos.com/blog/langgraph-que-es-como-usarlo-y-sus-funcionalidades).
