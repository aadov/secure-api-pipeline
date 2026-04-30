# 🔐 Secure API Pipeline

![CI Pipeline](https://github.com/aadov/secure-api-pipeline/actions/workflows/ci.yml/badge.svg)

DevSecOps pipeline: FastAPI + PostgreSQL + Docker + CI/CD + SAST/SCA

## 🏗️ Architecture


## 🛡️ Security Results

| Tool | Target | Result |
|------|--------|--------|
| Bandit | Python code | 0 issues |
| Trivy | Docker image | 2 HIGH, 0 CRITICAL (down from 13) |

## 🚀 Quick Start

```bash
git clone https://github.com/aadov/secure-api-pipeline.git
cd secure-api-pipeline
cp .env.example .env
docker compose up --build
```

API доступен на `http://localhost:8000`

## 📍 Endpoints

| Endpoint | Description |
|----------|-------------|
| GET /health | Health check |
| GET /db-check | Database connectivity check |
| GET /docs | Swagger UI |

## 🔧 Tech Stack

- **API:** FastAPI + Uvicorn
- **DB:** PostgreSQL 15
- **Container:** Docker + Docker Compose (Alpine base)
- **CI/CD:** GitHub Actions
- **SAST:** Bandit
- **SCA:** Trivy
- 
## 🌐 Live Demo
API: http://84.235.251.208:8000/docs
