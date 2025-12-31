---
id: 1
title: "Create Todo App Constitution"
stage: constitution
date: "2025-01-01"
surface: "agent"
model: "Qwen"
feature: "none"
branch: "main"
user: "Abdullah Ikhlaq"
command: "/sp.constitution # Constitution for Todo In-Memory Python Console App"
labels: ["constitution", "todo-app", "spec-driven"]
spec: "null"
ticket: "null"
adr: "null"
pr: "null"
files:
  - ".specify/memory/constitution.md"
  - ".specify/templates/plan-template.md"
  - ".specify/templates/spec-template.md"
  - ".specify/templates/tasks-template.md"
  - "README.md"
tests: []
outcome: "Successfully created the project constitution for the Todo In-Memory Python Console App, updating dependent templates to align with the new principles."
evaluation: "Constitution created with all required sections, principles, and governance details. Dependent templates updated to reflect the new constitution's requirements."
---

# Create Todo App Constitution

## User Input

```
/sp.constitution # Constitution for Todo In-Memory Python Console App

## Project Overview
This is a spec-driven development project for a basic command-line Todo application. The app stores tasks in memory only (no persistence). It implements five core features: Add Task, Delete Task, Update Task, View Task List, and Mark as Complete. Use Python 3.13+, UV for packaging, and Spec-Kit Plus for generating and validating specs and code.

## Guiding Principles
- **Spec-Driven Approach**: All development starts with specifications. Specs must be written in YAML format, versioned in the 'specs_history' folder (e.g., spec_v1.yaml). Each spec iteration refines the previous one based on feedback or new requirements.
- **Clean Code Standards**: Follow PEP 8. Use meaningful variable names, type hints, docstrings, and modular structure. Avoid global variables; prefer classes (e.g., Task class, TodoManager class).
- **Minimalism**: No external dependencies beyond built-in Python modules unless absolutely necessary. Keep the app lightweight and focused on MVP.
- **Error Handling**: Gracefully handle invalid inputs, non-existent IDs, and edge cases (e.g., empty list). Use try-except where appropriate.
- **Testing**: Specs should include example use cases. Manually test features and document in README.md.
- **AI Assistance Rules**: When using tools like Claude or Qwen:
  - Generate specs first, then code.
  - Ensure outputs align with this constitution.
  - Do not introduce features outside the five core ones.
  - Prioritize readability and simplicity over optimization.

## Feature Specifications Guidelines
- **Task Structure**: Each task has: ID (int, auto-increment), Title (str), Description (str), Completed (bool, default False).
- **CLI Interface**: Use a menu-driven loop (e.g., print options, input choice). Commands: 1=Add, 2=View, 3=Update, 4=Delete, 5=Mark, 0=Exit.
- **Add Task**: Prompt for title and description; assign ID; add to list.
- **Delete Task**: Prompt for ID; remove if exists.
- **Update Task**: Prompt for ID; then new title/description.
- **View Task List**: Print tasks with format: "[ID] [Status] Title: Description" (Status: [X] complete, [ ] incomplete).
- **Mark as Complete**: Prompt for ID; toggle completed flag.

## Project Structure Rules
- Root: constitution.txt, README.md, specs_history/ (with .yaml files), src/ (with .py files).
- src/main.py: Entry point with CLI loop.
- src/todo.py: Core logic (classes/functions for tasks).
- README.md: Include setup (uv init, uv run), usage examples, and feature demos.

## Iteration Process
1. Write/refine spec in specs_history.
2. Use Spec-Kit Plus to generate/validate code.
3. Test and commit.
4. If changes needed, create new spec version.
```

## Response

I've successfully created the constitution for the Todo In-Memory Python Console App and updated the dependent templates to align with the new principles. Here's what was accomplished:

1. Created the constitution file at `.specify/memory/constitution.md` with all the specified principles and guidelines
2. Updated the plan template to include constitution compliance checks
3. Updated the spec template to reflect the functional requirements from the constitution
4. Updated the tasks template to align with the project structure and requirements
5. Created a README.md file that references the constitution and project structure

The constitution includes all the core principles specified by the user:
- Spec-Driven Approach
- Clean Code Standards
- Minimalism
- Error Handling
- Testing
- AI Assistance Rules

It also includes the feature specifications guidelines, project structure rules, and iteration process as specified in the user's request.