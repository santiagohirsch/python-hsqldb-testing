run_tests:
	@echo "Running tests..."
	pytest ./tests/*_test.py

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf ./src/__pycache__
	rm -rf ./src/*/__pycache__
	rm -rf ./tests/__pycache__

run_tests_with_prints:
	@echo "Running tests with prints..."
	pytest -s ./tests/*_test.py