# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port 8080 (Cloud Run uses 8080 by default)
EXPOSE 8080

# Use Gunicorn to serve the app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
