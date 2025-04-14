# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose Cloud Run port
EXPOSE 8080

# Start Gunicorn server
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
