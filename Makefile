# Makefile for running Flask API

.PHONY: run

# Run the Flask API
run:
	@echo "Running the Flask API..."
	flask run

.PHONY: test clean

# Run the tests
test:
	pytest --disable-warnings --cov=app tests/

# Run cache clean
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +


