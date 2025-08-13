#!/bin/sh

echo "📦 Running migrations..."
python manage.py migrate

PORT=${PORT:-8000}
echo "🚀 Starting Django server on port $PORT"
python manage.py runserver 0.0.0.0:$PORT
