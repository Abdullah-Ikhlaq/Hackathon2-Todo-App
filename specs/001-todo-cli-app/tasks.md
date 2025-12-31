---

description: "Task list for Todo CLI App implementation"
---

# Tasks: Todo CLI App

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan with src/ and specs_history/ directories
- [ ] T002 Initialize Python 3.13+ project with UV packaging
- [ ] T003 [P] Configure linting and formatting tools for PEP 8 compliance
- [x] T004 Create initial YAML specification in specs_history/ following spec-driven approach

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 [P] Create src/__init__.py to make src a Python package
- [x] T006 [P] Create Task dataclass in src/todo.py with id, title, description, completed attributes
- [x] T007 Create TodoManager class in src/todo.py with tasks list and next_id tracking
- [x] T008 Implement basic CLI menu structure in src/main.py with options 0-5
- [x] T009 Create src/cli.py for input/output handling functions
- [x] T010 Configure error handling infrastructure with try-except patterns

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Implement the ability to add new tasks with title and description, assigning auto-incremented IDs

**Independent Test**: Can be fully tested by selecting option 1 from the menu, entering a title and description, and verifying that the task appears in the list with an auto-assigned ID and 'not completed' status.

### Implementation for User Story 1

- [x] T011 [US1] Implement add_task method in TodoManager class with title validation
- [x] T012 [US1] Create add_task CLI function in src/cli.py with input prompts
- [x] T013 [US1] Integrate add_task functionality with menu option 1 in src/main.py
- [x] T014 [US1] Add validation for non-empty/non-whitespace title in src/todo.py
- [x] T015 [US1] Add type hints and docstrings to add_task functionality

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Implement the ability to view all tasks with proper formatting [ID] [Status] Title: Description

**Independent Test**: Can be fully tested by selecting option 2 from the menu and verifying that all tasks are displayed with proper formatting, including ID, status indicator, title, and description.

### Implementation for User Story 2

- [x] T016 [US2] Implement get_all_tasks method in TodoManager class
- [x] T017 [US2] Create view_tasks CLI function in src/cli.py with proper formatting
- [x] T018 [US2] Integrate view_tasks functionality with menu option 2 in src/main.py
- [x] T019 [US2] Handle empty task list case with appropriate message
- [x] T020 [US2] Add type hints and docstrings to view_tasks functionality

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks as Complete (Priority: P2)

**Goal**: Implement the ability to toggle completion status of tasks by ID

**Independent Test**: Can be fully tested by selecting option 5 from the menu, entering a valid task ID, and verifying that the task's completion status is toggled.

### Implementation for User Story 3

- [x] T021 [US3] Implement mark_task_complete method in TodoManager class
- [x] T022 [US3] Create mark_task_complete CLI function in src/cli.py with ID input
- [x] T023 [US3] Integrate mark_task_complete functionality with menu option 5 in src/main.py
- [x] T024 [US3] Add validation for valid task ID in src/todo.py
- [x] T025 [US3] Add type hints and docstrings to mark_task_complete functionality

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Details (Priority: P3)

**Goal**: Implement the ability to update task title and description by ID with Enter-to-skip functionality

**Independent Test**: Can be fully tested by selecting option 3 from the menu, entering a valid task ID, modifying the title/description, and verifying that the changes are saved.

### Implementation for User Story 4

- [x] T026 [US4] Implement update_task method in TodoManager class
- [x] T027 [US4] Create update_task CLI function in src/cli.py with ID and field inputs
- [x] T028 [US4] Integrate update_task functionality with menu option 3 in src/main.py
- [x] T029 [US4] Add Enter-to-skip functionality for title/description updates
- [x] T030 [US4] Add type hints and docstrings to update_task functionality

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

**Goal**: Implement the ability to delete tasks by ID with confirmation prompt

**Independent Test**: Can be fully tested by selecting option 4 from the menu, entering a valid task ID, confirming the deletion, and verifying that the task is removed from the list.

### Implementation for User Story 5

- [x] T031 [US5] Implement delete_task method in TodoManager class
- [x] T032 [US5] Create delete_task CLI function in src/cli.py with ID input and confirmation
- [x] T033 [US5] Integrate delete_task functionality with menu option 4 in src/main.py
- [x] T034 [US5] Add validation for valid task ID in src/todo.py
- [x] T035 [US5] Add type hints and docstrings to delete_task functionality

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T036 [P] Update README.md with UV setup and usage examples
- [x] T037 Add comprehensive error handling for all user inputs
- [x] T038 Validate all edge cases (empty list, invalid IDs, etc.)
- [x] T039 [P] Add docstrings to all functions and classes
- [x] T040 Run quickstart.md validation to ensure all features work
- [x] T041 Final code review for PEP 8 compliance and clean architecture

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement add_task method in TodoManager class with title validation"
Task: "Create add_task CLI function in src/cli.py with input prompts"
Task: "Integrate add_task functionality with menu option 1 in src/main.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence