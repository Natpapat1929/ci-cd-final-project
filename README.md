# CI/CD Tools and Practices Final Project

**Project name:** ci-cd-final-project - Counter Service

This repository contains the final project for the IBM CI/CD Tools and Practices course. It is a small Python Flask counter REST service with a CI pipeline built using GitHub Actions and a CD pipeline built using Tekton on OpenShift.

## Contents

- `service/` - Flask application source code
- `tests/` - unit tests run with nose
- `.github/workflows/workflow.yml` - GitHub Actions CI workflow (Lint with flake8, Run unit tests with nose)
- `.tekton/tasks.yml` - Tekton tasks (cleanup, nose)
- `.tekton/pipeline.yml` - Tekton CD pipeline

## Run locally

```bash
pip install -r requirements.txt
nosetests -v
gunicorn --bind=0.0.0.0:8000 service:app
```
