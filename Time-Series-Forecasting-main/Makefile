# # Run docker-compose up from forecasting_service directory
# run:
# 	cd Data/Database && docker-compose up -d

# # Stop and remove containers from forecasting_service directory
# stop:
# 	cd Data/Database && docker-compose down

# # View logs of running containers
# logs:
# 	cd Data/Database && docker-compose logs -f

# # List running containers
# ps:
# 	cd Data/Database && docker-compose ps

# # Access forecasting_serviceQL shell
# psql:
# 	cd Data/Database && docker-compose exec database psql -U induwara -d initial_db

# # Rebuild containers
# build:
# 	cd Data/Database && docker-compose build

# # Clean up volumes and networks (full cleanup)
# clean:
# 	cd Data/Database && docker-compose down -v --remove-orphans
# 	rm -rf Data/Database/db-data
# 	rm -rf Data/Database/pgadmin-data
    
# # Restart containers
# restart:
# 	cd Data/Database && docker-compose restart

# Django Commands
run-server:
	cd forecasting_service && \
	echo "Starting Django server..." && \
	echo "Create migrations" && \
	python manage.py makemigrations forecastApp && \
	echo "==========================" && \
	echo "Migrate" && \
	python manage.py migrate && \
	echo "==========================" && \
	echo "Run server" && \
	python manage.py runserver 0.0.0.0:8000

shell:
	cd forecasting_service && python manage.py shell

test:
	cd forecasting_service && python manage.py test forecastApp

clear-migrations:
	@echo "WARNING: This will delete all migrations (except __init__.py)!" && \
	read -p "Are you sure? (y/N): " confirm && \
	if [ "$$confirm" = "y" ]; then \
		cd forecasting_service && \
		echo "Clearing migrations..." && \
		find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && \
		find . -path "*/migrations/*.pyc"  -delete && \
		echo "==========================" && \
		echo "Create migrations" && \
		python manage.py makemigrations forecastApp && \
		echo "==========================" && \
		echo "Migrate" && \
		python manage.py migrate; \
	else \
		echo "Aborted."; \
	fi

run-server-fake:
	cd forecasting_service && \
	echo "Starting Django server..." && \
	echo "Create migrations" && \
	python manage.py makemigrations forecastApp && \
	echo "==========================" && \
	echo "Migrate with fake-initial" && \
	python manage.py migrate --fake-initial && \
	echo "==========================" && \
	echo "Run server" && \
	python manage.py runserver 0.0.0.0:8000


