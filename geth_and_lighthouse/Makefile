# Variables
APP_NAME = health_api
DOCKER_IMAGE = health_api

# Commands
build:
	docker build -t $(DOCKER_IMAGE) .

clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache *.pyc *.pyo *.log *.egg-info dist

run:
	python3 health.py

lint:
	flake8 --max-line-length=88 .

test:
	~/.local/bin/pytest --maxfail=1 --disable-warnings -q

docker-run:
	docker run -p 5000:5000 $(DOCKER_IMAGE)

docker-test:
	docker run --entrypoint pytest $(DOCKER_IMAGE)
