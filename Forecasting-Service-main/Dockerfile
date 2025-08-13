FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies for Prophet and others
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    g++ \
    curl \
    libatlas-base-dev \
    libblas-dev \
    liblapack-dev \
    libgfortran5 \
    libffi-dev \
    libpython3-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Optional: run migrations here or in entrypoint
# RUN python forecast_system/manage.py migrate

# Copy and set permissions for entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]
