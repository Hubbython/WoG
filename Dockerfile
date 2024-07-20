# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory into the container at /app
COPY . .

# Copy Scores.txt to /Scores.txt in the container
COPY Scores.txt /Scores.txt

# Expose port 5000 for Flask app (adjust if your Flask app runs on a different port)
EXPOSE 5000
EXPOSE 5001
# Command to run the Flask application
CMD ["python", "app.py"]
