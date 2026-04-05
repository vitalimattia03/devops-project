
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

## Run locally

```bash
pip install -r requirements.txt
python app.py