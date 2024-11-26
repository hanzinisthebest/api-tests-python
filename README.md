# API Testing Framework

This project is a Python-based API testing framework that tests the JSONPlaceholder and Fake Store APIs.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

- `tests/` - Contains test files for both APIs
- `test_data/` - Test data and models
- `utils/` - Helper functions and utilities
- `conftest.py` - PyTest fixtures and configuration

## Running Tests

Run all tests:
```bash
pytest
```

Run tests in parallel:
```bash
pytest -n auto
```

Generate a test report:
```bash
pytest --html=report.html
start report.html
``` 
