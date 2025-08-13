# Use an official Python runtime
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app
COPY app.py .

# Expose port 80
EXPOSE 80

# Run the app
CMD ["python", "app.py"]