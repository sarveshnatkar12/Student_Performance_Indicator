FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# (Make sure 'artifacts/' folder will exist or be created by the script)
RUN python -m src.pipeline.data_ingestion


EXPOSE 6120

CMD ["python", "app.py"]
