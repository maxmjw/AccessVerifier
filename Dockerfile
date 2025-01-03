FROM python:3.12-slim

WORKDIR /accessverification

COPY requirements.txt .
COPY main.py .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /accessverification/app

CMD ["python", "main.py"]