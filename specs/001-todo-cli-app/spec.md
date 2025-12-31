# Feature Specification: Todo CLI App

**Feature Branch**: `001-todo-cli-app`
**Created**: 2025-01-01
**Status**: Draft
**Input**: User description: "Todo In-Memory Python Console App – Phase I Basic Level Target audience: Hackathon developers using Spec-Kit Plus with Qwen/Claude for spec-driven code generation Focus: Implement a menu-driven command-line Todo app with exactly the five required basic features using in-memory storage Success criteria: Fully working console app with menu loop and clear prompts Implements all 5 features correctly: • Add: title + description, auto ID, completed=False • View: lists tasks with ID, [ ]/[X] status, title, description; handles empty list • Update: modify title/description by ID (Enter to skip) • Delete: remove by ID with confirmation • Mark: toggle completion by ID with feedback Robust error handling (invalid ID/input, no crashes) Clean, modular code with type hints, docstrings, dataclasses Required project structure: constitution.txt, specs_history/ (versioned YAMLs), src/ (main.py + modules) README.md with UV setup and usage examples Constraints: Python 3.13+, managed with UV (no pip) No external dependencies (stdlib only) In-memory only (list of tasks, lost on exit) Text-based menu CLI with numbered options Menu redisplays after operations (except exit) Title non-whitespace; description optional Not building: Persistence (files/DB) Due dates, priorities, search, sorting GUI or web interface Unit tests or argparse Extra features beyond the 5 basics Guidelines: Use dataclass for Task TodoManager class for operations/ID handling Separate CLI logic from business logic Consistent feedback messages and status indicators ([ ] / [X])"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add New Tasks (Priority: P1)

As a user, I want to add new tasks to my todo list so that I can keep track of things I need to do. When I select the 'Add Task' option from the menu, I should be prompted to enter a title and description for the task. The system should automatically assign an ID to the task and set its completion status to 'not completed'.

**Why this priority**: This is the most fundamental feature of a todo app - without the ability to add tasks, the app has no value.

**Independent Test**: Can be fully tested by selecting option 1 from the menu, entering a title and description, and verifying that the task appears in the list with an auto-assigned ID and 'not completed' status.

**Acceptance Scenarios**:

1. **Given** I am at the main menu, **When** I select option 1 to add a task and enter a valid title and description, **Then** the task should be added to the list with an auto-incremented ID and 'not completed' status, and the menu should reappear.

2. **Given** I am adding a task, **When** I enter a title with only whitespace, **Then** the system should display an error message and prompt me to enter a valid title.

---

### User Story 2 - View Task List (Priority: P1)

As a user, I want to view my list of tasks so that I can see what I need to do and track my progress. When I select the 'View Tasks' option from the menu, I should see a list of all tasks with their ID, completion status, title, and description.

**Why this priority**: This is the second most fundamental feature - users need to see their tasks to manage them effectively.

**Independent Test**: Can be fully tested by selecting option 2 from the menu and verifying that all tasks are displayed with proper formatting, including ID, status indicator, title, and description.

**Acceptance Scenarios**:

1. **Given** I have tasks in my list, **When** I select option 2 to view tasks, **Then** all tasks should be displayed with format "[ID] [Status] Title: Description" where status is [ ] for incomplete and [X] for complete.

2. **Given** I have no tasks in my list, **When** I select option 2 to view tasks, **Then** the system should display a message indicating that the list is empty and return to the main menu.

---

### User Story 3 - Mark Tasks as Complete (Priority: P2)

As a user, I want to mark tasks as complete so that I can track my progress and know what I've already done. When I select the 'Mark Task Complete' option from the menu, I should be prompted to enter a task ID, and the system should toggle the completion status of that task.

**Why this priority**: This is essential functionality that allows users to track their progress and maintain an up-to-date todo list.

**Independent Test**: Can be fully tested by selecting option 5 from the menu, entering a valid task ID, and verifying that the task's completion status is toggled.

**Acceptance Scenarios**:

1. **Given** I have tasks in my list, **When** I select option 5 to mark a task complete and enter a valid task ID, **Then** the task's status should toggle between complete and incomplete, and appropriate feedback should be provided.

2. **Given** I have tasks in my list, **When** I select option 5 to mark a task complete and enter an invalid task ID, **Then** the system should display an error message and return to the main menu.

---

### User Story 4 - Update Task Details (Priority: P3)

As a user, I want to update the details of my tasks so that I can modify titles or descriptions as needed. When I select the 'Update Task' option from the menu, I should be prompted to enter a task ID and then allowed to modify the title and description.

**Why this priority**: This allows users to refine their tasks as their needs change, improving the app's utility.

**Independent Test**: Can be fully tested by selecting option 3 from the menu, entering a valid task ID, modifying the title/description, and verifying that the changes are saved.

**Acceptance Scenarios**:

1. **Given** I have tasks in my list, **When** I select option 3 to update a task and enter a valid task ID, **Then** I should be prompted to enter new title and description values, with the option to press Enter to skip updating each field.

2. **Given** I am updating a task, **When** I enter an invalid task ID, **Then** the system should display an error message and return to the main menu.

---

### User Story 5 - Delete Tasks (Priority: P3)

As a user, I want to delete tasks that I no longer need so that I can keep my todo list clean and focused. When I select the 'Delete Task' option from the menu, I should be prompted to enter a task ID and confirm the deletion.

**Why this priority**: This allows users to remove completed or irrelevant tasks, keeping the list manageable.

**Independent Test**: Can be fully tested by selecting option 4 from the menu, entering a valid task ID, confirming the deletion, and verifying that the task is removed from the list.

**Acceptance Scenarios**:

1. **Given** I have tasks in my list, **When** I select option 4 to delete a task and enter a valid task ID, **Then** I should be prompted to confirm the deletion, and if confirmed, the task should be removed from the list.

2. **Given** I am deleting a task, **When** I enter an invalid task ID, **Then** the system should display an error message and return to the main menu.

### Edge Cases

- What happens when the user enters invalid input (non-numeric ID, empty title, etc.)?
- How does the system handle an empty task list when trying to view, update, delete, or mark tasks?
- What happens when a user tries to access a task ID that doesn't exist?
- How does the system handle very long titles or descriptions?
- What happens when the user enters only whitespace for a title?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST implement a menu-driven command-line interface with numbered options (1-5 for features, 0 to exit)
- **FR-002**: System MUST store tasks in memory only (no persistence to files or databases)
- **FR-003**: System MUST implement Add Task feature that accepts title and description, assigns auto-incremented ID, and sets completed=False
- **FR-004**: System MUST implement View Task List feature that displays tasks with format "[ID] [Status] Title: Description"
- **FR-005**: System MUST implement Update Task feature that allows modification of title/description by ID with Enter-to-skip functionality
- **FR-006**: System MUST implement Delete Task feature that removes tasks by ID with confirmation prompt
- **FR-007**: System MUST implement Mark as Complete feature that toggles completion status by ID with feedback
- **FR-008**: System MUST handle empty task lists gracefully across all operations
- **FR-009**: System MUST validate input and handle invalid IDs without crashing
- **FR-010**: System MUST use dataclass for Task entity with ID, Title, Description, and Completed attributes
- **FR-011**: System MUST use TodoManager class for operations and ID handling
- **FR-012**: System MUST separate CLI logic from business logic
- **FR-013**: System MUST provide consistent feedback messages and status indicators ([ ] / [X])
- **FR-014**: System MUST use only built-in Python modules (no external dependencies)
- **FR-015**: System MUST require Python 3.13+ and be managed with UV package manager
- **FR-016**: System MUST implement robust error handling for invalid input without crashing
- **FR-017**: System MUST ensure title is non-whitespace (description optional)
- **FR-018**: System MUST display menu after each operation (except exit)

### Key Entities

- **Task**: Represents a single todo item with ID (int, auto-incremented), Title (str), Description (str), and Completed (bool, default False)
- **TodoManager**: Manages the collection of tasks, handles operations (add, update, delete, mark complete), and manages ID assignment

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully add, view, update, delete, and mark tasks complete without application crashes
- **SC-002**: All five core features are implemented and accessible through the menu interface
- **SC-003**: Application handles invalid inputs gracefully without crashing (e.g., invalid IDs, empty titles)
- **SC-004**: Task list displays correctly with proper formatting: "[ID] [Status] Title: Description"
- **SC-005**: Menu redisplays after each operation (except exit) providing continuous user interaction
- **SC-006**: Code includes type hints, docstrings, and follows PEP 8 standards for maintainability
- **SC-007**: Application is built with clean, modular architecture separating CLI from business logic
