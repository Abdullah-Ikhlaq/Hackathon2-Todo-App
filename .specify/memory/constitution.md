<!-- SYNC IMPACT REPORT:
Version change: N/A (initial creation) → 1.0.0
Added sections: All sections as this is initial creation
Removed sections: N/A
Templates requiring updates: 
- ✅ .specify/templates/plan-template.md - updated to align with principles
- ✅ .specify/templates/spec-template.md - updated to align with principles  
- ✅ .specify/templates/tasks-template.md - updated to align with principles
- ⚠ .specify/templates/commands/*.md - review for any outdated references
- ⚠ README.md - update references to principles if they exist
Follow-up TODOs: None
-->

# Todo In-Memory Python Console App Constitution

## Core Principles

### Spec-Driven Approach
All development starts with specifications. Specs must be written in YAML format, versioned in the 'specs_history' folder (e.g., spec_v1.yaml). Each spec iteration refines the previous one based on feedback or new requirements.

### Clean Code Standards
Follow PEP 8. Use meaningful variable names, type hints, docstrings, and modular structure. Avoid global variables; prefer classes (e.g., Task class, TodoManager class).

### Minimalism
No external dependencies beyond built-in Python modules unless absolutely necessary. Keep the app lightweight and focused on MVP.

### Error Handling
Gracefully handle invalid inputs, non-existent IDs, and edge cases (e.g., empty list). Use try-except where appropriate.

### Testing
Specs should include example use cases. Manually test features and document in README.md.

### AI Assistance Rules
When using tools like Claude or Qwen:
- Generate specs first, then code.
- Ensure outputs align with this constitution.
- Do not introduce features outside the five core ones.
- Prioritize readability and simplicity over optimization.

## Feature Specifications Guidelines

### Task Structure
Each task has: ID (int, auto-increment), Title (str), Description (str), Completed (bool, default False).

### CLI Interface
Use a menu-driven loop (e.g., print options, input choice). Commands: 1=Add, 2=View, 3=Update, 4=Delete, 5=Mark, 0=Exit.

### Add Task
Prompt for title and description; assign ID; add to list.

### Delete Task
Prompt for ID; remove if exists.

### Update Task
Prompt for ID; then new title/description.

### View Task List
Print tasks with format: "[ID] [Status] Title: Description" (Status: [X] complete, [ ] incomplete).

### Mark as Complete
Prompt for ID; toggle completed flag.

## Project Structure Rules

### Directory Structure
- Root: constitution.txt, README.md, specs_history/ (with .yaml files), src/ (with .py files).
- src/main.py: Entry point with CLI loop.
- src/todo.py: Core logic (classes/functions for tasks).
- README.md: Include setup (uv init, uv run), usage examples, and feature demos.

## Iteration Process

### Development Cycle
1. Write/refine spec in specs_history.
2. Use Spec-Kit Plus to generate/validate code.
3. Test and commit.
4. If changes needed, create new spec version.

## Governance

### Amendment Process
Changes to this constitution require explicit documentation and approval. Any modifications to core principles must be justified with clear rationale and impact assessment.

### Versioning Policy
This constitution follows semantic versioning:
- MAJOR: Backward incompatible governance/principle removals or redefinitions
- MINOR: New principle/section added or materially expanded guidance
- PATCH: Clarifications, wording, typo fixes, non-semantic refinements

### Compliance Review
All code submissions must be reviewed for compliance with these principles. Code reviews should verify adherence to the specified architecture, error handling, and testing requirements.

**Version**: 1.0.0 | **Ratified**: 2025-01-01 | **Last Amended**: 2025-01-01