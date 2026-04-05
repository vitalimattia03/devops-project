
---

# 7. Badge CI (sembra banale → cambia percezione)

Aggiungi in cima al README:

```markdown
![CI](https://github.com/TUO_USERNAME/devops-project/actions/workflows/pipeline.yml/badge.svg)

# DevOps Project

Simple Python Flask app with CI/CD pipeline using GitHub Actions and Docker.

## Tech Stack
- Python (Flask)
- Docker
- GitHub Actions (CI)

## Features
- Automated tests with pytest
- Dockerized application
- CI pipeline on push to main

## Live API

- / → OK
- /health → status check
- /api → sample endpoint

## Architecture

- Flask API
- Pytest for testing
- GitHub Actions CI
- Docker containerization
- Deployed on Render

## Endpoints

- `/` → basic check
- `/health` → health status
- `/api` → sample API

## Run locally

```bash
pip install -r requirements.txt
python app.py

## CI/CD Flow

1. Push su main
2. GitHub Actions:
   - install dependencies
   - run tests
   - build Docker image
   - run container
   - healthcheck
3. Deploy su Render
4. Test live endpoint

## Live Check

Pipeline verifica automaticamente:

- App builda
- Container parte
- API risponde
- Deploy è funzionante