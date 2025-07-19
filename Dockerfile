FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run data_ingestion.py to generate artifacts (model.pkl, etc.)
RUN python src/pipeline/data_ingestion.py

EXPOSE 6120

CMD ["python", "app.py"]
