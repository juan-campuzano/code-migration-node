# python-app

A Python Flask application intentionally using outdated packages, created for testing and migration purposes.

## Getting Started

```bash
cd python-app
pip install -r requirements.txt
python app.py        # Start dev server at http://localhost:5000
pytest tests/        # Run unit tests
```

## Endpoints

| Route      | Description                                         |
|------------|-----------------------------------------------------|
| `/`        | Returns a welcome message and a unique UUID         |
| `/data`    | Returns unique values and summary statistics        |
| `/config`  | Returns parsed YAML configuration                   |
| `/db`      | Demonstrates SQLAlchemy with an in-memory SQLite DB |
| `/image`   | Generates a PNG image with Pillow                   |
| `/encrypt` | Encrypts and decrypts a message with cryptography   |
| `/fetch`   | Makes an outbound HTTP GET request with requests    |

## Outdated Dependencies

The following dependencies are **intentionally pinned** to outdated versions for testing code migration tooling:

| Package        | Pinned Version | Notes                    |
|----------------|---------------|--------------------------|
| `flask`        | 2.3.3         | Old Flask (2.x) version  |
| `requests`     | 2.28.2        | Old requests version     |
| `numpy`        | 1.26.4        | Old numpy (1.x) version  |
| `pandas`       | 2.1.4         | Old pandas version       |
| `sqlalchemy`   | 1.4.54        | Old SQLAlchemy (1.x) version |
| `Pillow`       | 10.0.1        | Old Pillow version       |
| `PyYAML`       | 5.1           | Old PyYAML version       |
| `cryptography` | 38.0.4        | Old cryptography version |
