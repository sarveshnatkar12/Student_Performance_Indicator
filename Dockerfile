FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Copy entire project
COPY . /app

# Install AWS CLI (optional but was in your course)
RUN apt update -y && apt install -y awscli

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run data_ingestion to create model.pkl and other artifacts
RUN python -m src.components.data_ingestion

# Expose port used by your Flask app
EXPOSE 6120

# Start the app
CMD ["python3", "app.py"]
