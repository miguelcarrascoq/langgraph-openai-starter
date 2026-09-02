FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY langchain.py .
COPY langchain_docker.ipynb langchain_local.ipynb langchain_colab.ipynb .

EXPOSE 8888

CMD ["python", "langchain.py"]
