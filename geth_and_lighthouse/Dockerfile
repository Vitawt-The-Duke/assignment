# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY health.py requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the API port
EXPOSE 5000

# Run the Flask app
CMD ["python", "health.py"]
