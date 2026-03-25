# code-migration-node

This repository contains sample applications intentionally using outdated packages, created for testing and migration purposes.

## Project Structure

- `angular-app/` - Angular 17 standalone application
- `python-app/` - Python Flask application

## Angular App

The Angular app (`angular-app/`) is scaffolded with Angular CLI 17 and includes several **intentionally outdated** dependencies for testing code migration tooling:

| Package   | Pinned Version | Current Version |
|-----------|---------------|-----------------|
| `lodash`  | 4.17.15       | Latest          |
| `moment`  | 2.24.0        | Latest          |
| `axios`   | 0.19.0        | Latest          |
| `express` | 4.17.1        | Latest          |
| `uuid`    | 3.4.0         | Latest          |

### Getting Started

```bash
cd angular-app
npm install
npm start        # Start dev server at http://localhost:4200
npm run build    # Production build
npm test         # Run unit tests
```

## Python App

The Python app (`python-app/`) is a Flask application that includes several **intentionally outdated** dependencies for testing code migration tooling:

| Package        | Pinned Version | Current Version |
|----------------|---------------|-----------------|
| `flask`        | 2.3.3         | Latest          |
| `requests`     | 2.28.2        | Latest          |
| `numpy`        | 1.26.4        | Latest          |
| `pandas`       | 2.1.4         | Latest          |
| `sqlalchemy`   | 1.4.54        | Latest          |
| `Pillow`       | 12.1.1        | Latest          |
| `PyYAML`       | 6.0.1         | Latest          |
| `cryptography` | 46.0.5        | Latest          |

### Getting Started

```bash
cd python-app
pip install -r requirements.txt
python app.py        # Start dev server at http://localhost:5000
pytest tests/        # Run unit tests
```