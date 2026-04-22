# Use a lightweight official Python base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency list and install before copying app code
# This layer is cached separately so rebuilds are faster
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run with gunicorn for production-grade serving
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]