FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Cloud Run expects
EXPOSE 8080

# Command to run your application
CMD ["python", "main.py"]
