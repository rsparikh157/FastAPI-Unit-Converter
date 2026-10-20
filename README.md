# Unit Converter API

A REST API built with **FastAPI** that converts values between supported units of length, mass, temperature, and digital storage.

The project focuses on learning API development, request validation, response models, error handling, and automated testing with pytest.

## Features

- Convert units of length: km, m, cm
- Convert units of mass: kg, g
- Convert temperature: Celsius, Fahrenheit, Kelvin
- Convert digital storage units: B, kB, MB, GB, KiB, MiB, GiB
- Interactive unit dropdowns in Swagger UI using Python enums
- Request validation and structured JSON responses
- HTTP error handling for invalid and incompatible units
- Automated tests using pytest

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- HTTPX

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Replace the placeholders with your actual repository URL and folder name.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Start the API

```bash
uvicorn codebase:unit_converter --reload
```

### 4. Explore the API

Open the interactive API documentation in your browser:

http://127.0.0.1:8000/docs

Use the `/convert` endpoint to select units, enter a value, and view the conversion result.

## Example Request

```http
GET /convert?value=5&from_unit=km&to_unit=m
```

Example JSON response:

```json
{
  "value": 5.0,
  "from_unit": "km",
  "to_unit": "m",
  "result": 5000.0
}
```

## Running Tests

Run the automated test suite with:

```bash
python -m pytest -v
```

The project currently has 17 passing tests.

## Notes

- Decimal digital storage units use factors of 1000.
- Binary digital storage units use factors of 1024.
- Invalid enum values are rejected by FastAPI request validation.
- Negative values are currently accepted; the API does not enforce physical-domain restrictions on lengths or masses.

## Future Improvements

- Deploy the API publicly.
- Expand the supported units.
- Improve validation and error handling as the project evolves.
