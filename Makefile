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