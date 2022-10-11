.PHONY: homework-i-run
homework-i-run:
	@python grouping_people/main.py

.PHONY: init-dev
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install

.PHONY: d-homework-i-run
d-homework-i-run:
	@make d-run

.PHONY: d-run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose \
			up --build
