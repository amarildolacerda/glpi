# Tasks: Contratos de erro e validação da API

**Input**: spec.md, plan.md
**Prerequisites**: plan.md (required), spec.md (required)
**Project Mode**: Brownfield

## Phase 1: Work Item 1 - Contratos de erro e validação (Priority: P1) 🎯 MVP

- [ ] T001 [OBJ1] {TR-001,TR-002} Create acceptance test stub in tests/test_error_contracts.py ← plan:AcceptanceTestStubs
- [ ] T002 [OBJ1] {TR-003} Create acceptance test stub in tests/test_error_contracts.py ← plan:AcceptanceTestStubs
- [ ] T003 [OBJ1] {TR-005} Create acceptance test stub in tests/test_error_contracts.py ← plan:AcceptanceTestStubs
- [ ] T004 [OBJ1] {TR-001} Add ErrorResponse schema in core/schemas.py → exports: ErrorResponse(code,message,details)
- [ ] T005 [OBJ1] {TR-002} Add RequestValidationError handler in main.py → exports: validation_exception_handler(request, exc) [VERIFY: grep "RequestValidationError" main.py]
- [ ] T006 [OBJ1] {TR-003} Add generic exception handler in main.py → exports: generic_exception_handler(request, exc) [VERIFY: grep "HTTP_500" main.py]
- [ ] T007 [OBJ1] {TR-004} Verify compatibility for existing success endpoints in interfaces/v1_agent_api.py and interfaces/v2_client_api.py after:T005 ← T005:validation_exception_handler
- [ ] T008 [OBJ1] {TR-005} Add negative regression tests in tests/test_error_contracts.py after:T001 ← T001:AcceptanceTestStubs [VERIFY: pytest tests/test_error_contracts.py]

## Dependencies

- Tasks T001-T003 create red acceptance stubs before implementation.
- T004 defines the common error contract consumed by handlers and tests.
- T005 and T006 implement the validation and generic error handlers.
- T007 validates compatibility after error handling changes.
- T008 closes the regression coverage for invalid payloads and internal errors.
