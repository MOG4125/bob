.PHONY: test clean install update

# Install the package
install:
	pip install -e .

# Update all packages in requirements.bob
update:
	@echo "Updating packages from requirements.bob..."
	@while read p; do pip install --upgrade $$p; done < requirements.bob

# Run tests
test:
	pytest

# Clean artifacts
clean:
	rm -rf build/ dist/ *.egg-info .bob_update_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
