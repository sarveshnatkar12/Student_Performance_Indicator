FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ✅ Generate artifacts before starting the app
RUN python -m src.components.data_ingestion

EXPOSE 6120

CMD ["python", "app.py"]
