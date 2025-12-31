# Research Summary: Todo CLI App

## Decision: Task ID Management
**Rationale**: After reviewing the specification and considering best practices, the decision is to continue incrementing IDs (next ID is always highest used + 1). This approach is simpler to implement, avoids potential confusion if users remember specific IDs, and prevents issues with concurrent operations.
**Alternatives considered**: Reusing deleted IDs (filling gaps in sequence) was considered but rejected due to complexity in implementation and potential for confusion.

## Decision: Input Validation Approach
**Rationale**: Using a loop-based validation approach where the system continues to prompt the user until valid input is received. This ensures robust error handling as required by the specification.
**Alternatives considered**: Single validation with immediate return to menu was considered but rejected as it would be less user-friendly.

## Decision: Menu Structure
**Rationale**: Implementing a simple numeric menu system (1-5 for features, 0 to exit) as specified in the requirements. This provides a clear, easy-to-use interface for the command-line application.
**Alternatives considered**: Command-based input (typing commands like "add", "view") was considered but rejected as the specification specifically calls for numbered options.

## Decision: Data Storage Approach
**Rationale**: Using a simple in-memory list to store Task objects as specified in the requirements. This meets the "in-memory only" constraint and is efficient for the application's scope.
**Alternatives considered**: Other in-memory structures like dictionaries were considered but the list approach is simpler and sufficient for this use case.