# DevOps Monitoring Project

![CI](https://github.com/vitalimattia03/devops-project/actions/workflows/pipeline.yml/badge.svg)

## Overview

This project demonstrates a **complete DevOps workflow** using a Python Flask application with:

- CI pipeline (GitHub Actions)
- Docker containerization
- Monitoring with Prometheus
- Visualization with Grafana
- Alerting system (Grafana Alerts)
- Deployment on Render

The system is not only deployable, but also **observable and reactive**.

---

## Tech Stack

- Python (Flask)
- Docker / Docker Compose
- GitHub Actions (CI)
- Prometheus (metrics collection)
- Grafana (dashboard + alerting)
- Render (deployment)

---

## Project Structure
devops-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
│
├── tests/
│ └── test_app.py
│
├── .github/workflows/
│ └── pipeline.yml
│
└── README.md

---

## Features

### API Endpoints

| Endpoint      | Description |
|--------------|------------|
| `/`          | Web UI |
| `/health`    | Health check (status + uptime) |
| `/metrics`   | Prometheus metrics |
| `/api`       | Sample API |
| `/fail`      | Simulated error (500) |
| `/dashboard` | Real-time requests chart |

---

## CI Pipeline

Triggered on every push to `main`.

### Steps:
1. Install dependencies
2. Run unit tests (`pytest`)
3. Build Docker image
4. Run container
5. Health check (`/health`)
6. Metrics check (`/metrics`)
7. Test deployed app (Render)

---

## Run Locally

### 1. Virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

