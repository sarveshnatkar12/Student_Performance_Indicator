# Use the official Python 3.10 base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy all necessary files into the container
COPY . .

# Create virtual environment (optional, containers are isolated already)
# RUN python -m venv venv
# RUN . venv/bin/activate

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port your Flask app runs on (default 5000)
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
