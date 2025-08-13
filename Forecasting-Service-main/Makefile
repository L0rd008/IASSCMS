# Makefile for Forecasting Service

.PHONY: setup install run migrate test help

# Variables
PYTHON = python
VENV = venv
MANAGE = $(PYTHON) manage.py
PIP = pip
DIR = cd forecast_system

help:
	@echo "Available commands:"
	@echo "  setup           - Create virtual environment"
	@echo "  install         - Install dependencies"
	@echo "  run             - Run development server"
	@echo "  migrate         - Run database migrations"
	@echo "  test            - Run tests"
	@echo "  lint            - Run linting checks"
	@echo "  coverage        - Run tests with coverage report"
	@echo "  clean           - Remove cached files"

setup:
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created. Activate with:"
	@echo "  source $(VENV)/bin/activate (Linux/macOS)"
	@echo "  .\\$(VENV)\\Scripts\\activate (Windows)"

install:
	$(PIP) install -r requirements.txt

run:
	$(DIR) && $(MANAGE) runserver

migrate:
	$(DIR) && $(MANAGE) makemigrations
	$(DIR) && $(MANAGE) migrate

test:
	$(DIR) && $(MANAGE) test
