#.PHONY: homework-i-run
## Run homework.
#homework-i-run:
#	@python manage.py migrate && \
#	python manage.py runserver
#
#.PHONY: homework-i-purge
## Delete all created artifacts, related with homework execution
#homework-i-purge:
#	@echo Goodbye

.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run:
	@make init-config && \
		make d-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge

.PHONY: d-run
# Just run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=full_dev \
		docker-compose \
			up --build

.PHONY: d-run-i-local-dev
# Local run
d-run-i-local-dev:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=local_dev \
			docker-compose \
				up --build


.PHONY: d-purge
# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose \
			down --volumes --remove-orphans --rmi local --timeout 0

.PHONY: init-config
# Init config files
init-config:
	@cp docker-compose.override.dev.yml docker-compose.override.yml && \
		cp .env.example .env


.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install


.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files

.PHONY: migrations
# Make migrations
migrations:
	@python manage.py makemigrations

.PHONY: migrate
# Migrate
migrate:
	@python manage.py migrate

.PHONY: init-dev-i-create-superuser
init-dev-i-create-superuser:
	@DJANGO_SUPERUSER_PASSWORD=admin123 python manage.py createsuperuser --user admin --email admin@gmail.com --no-input