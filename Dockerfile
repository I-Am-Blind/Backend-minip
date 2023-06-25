# Use the official Python base image
FROM python:3.9-slim

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port that the Flask app will run on
EXPOSE 5000

# Set the environment variables
ENV FLASK_APP=app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start the Flask application
CMD ["flask", "run"]
