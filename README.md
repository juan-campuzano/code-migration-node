# code-migration-node

This repository contains an Angular 17 application intentionally using outdated packages, created for testing and migration purposes.

## Project Structure

- `angular-app/` - Angular 17 standalone application

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