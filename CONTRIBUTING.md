# Contributing Guidelines

Thank you for your interest in contributing to the Academic Performance Dashboard project.

This document outlines the development workflow and contribution standards used in this repository.

---

## Development Workflow

We follow a structured feature-branch workflow:

### 1. Create a feature branch from `dev`

Run the following commands:

    git checkout dev
    git pull
    git checkout -b feat/your-feature-name

### 2. Make small, atomic commits

- Write clear and descriptive commit messages.
- Keep each commit focused on one logical change.

### 3. Push your branch and open a Pull Request (PR) into `dev`

    git push -u origin feat/your-feature-name

- Request review from teammates.
- Address feedback before merging.

### 4. Preview deployment

All merges into `dev` automatically update the Posit Connect Cloud preview deployment.

### 5. Milestone releases

- When preparing a milestone release, merge `dev` into `main`.
- Create a GitHub release (e.g., v0.2.0).
- Manually republish the `main` deployment on Posit Connect Cloud.

---

## Code Standards

- Follow consistent naming conventions.
- Keep functions modular and readable.
- Ensure reactive logic is clearly structured.
- Avoid unnecessary dependencies in `requirements.txt`.
- Update documentation (README, CHANGELOG) when adding new features.

---

## Running the App Locally

    conda env create -f environment.yml
    conda activate dsci-532-m1
    cd src
    shiny run --reload app.py

---

## Reporting Issues

If you encounter bugs or have feature suggestions:

- Open an Issue on GitHub.
- Clearly describe the problem and include steps to reproduce.
- Include screenshots if relevant.

---

Thank you for contributing!