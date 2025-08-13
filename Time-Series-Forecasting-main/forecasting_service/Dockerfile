# Stage 1: Build
FROM python:3.13-slim AS builder

WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r /code/requirements.txt

# Stage 2: Runtime
FROM python:3.13-slim

WORKDIR /code

# Clean up unnecessary Python files to reduce image size
RUN find /usr/local -name '*.pyc' -delete && \
    find /usr/local -name '__pycache__' -delete && \
    rm -rf /usr/local/lib/python*/test/

# Copy only the installed dependencies from the builder stage
COPY --from=builder /install /usr/local

# Copy the application code
COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]