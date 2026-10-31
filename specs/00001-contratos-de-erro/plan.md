# Implementation Plan: Contratos de erro e validação da API

**Branch**: `00001-contratos-de-erro` | **Date**: 2026-10-31 | **Spec**: [spec.md](./spec.md)

## Summary

**Goal**: Definir e aplicar um contrato de erro padronizado para falhas de validação e falhas internas na API do GLPI, preservando o comportamento atual de sucesso.  
**Approach**: centralizar o tratamento de erros em `main.py`, introduzir um modelo `ErrorResponse` em `core/schemas.py` e validar com testes negativos de contrato.  
**Key Constraint**: a solução deve manter compatibilidade com endpoints existentes e nunca expor detalhes internos do servidor.

## Technical Context

**Language/Version**: Python 3.11+  
**Primary Dependencies**: FastAPI, Pydantic, pytest  
**Storage**: N/A  
**Testing**: pytest  
**Target Platform**: Linux/Windows local execution  
**Project Type**: web API  
**Project Mode**: greenfield within existing project  
**Performance Goals**: sem regressão funcional; resposta de erro em tempo equivalente ao fluxo atual  
**Constraints**: responder com estrutura previsível e sem stack trace  
**Scale/Scope**: endpoints de suporte da API atual e testes de regressão

## Instructions Check

*GATE: must pass before implementation. Shared project instructions already reviewed; this plan is aligned with the lean pipeline `spec -> plan -> implement -> QC -> commit` and the project’s current architecture.*

## Architecture

```mermaid
C4Container
  User[Cliente/Agente] --> API[FastAPI endpoints]
  API --> Schemas[core/schemas.py: ErrorResponse]
  API --> Handlers[main.py: exception handlers]
  Handlers --> Responses[422/400/500 standard payloads]
  API --> Tests[tests/test_error_contracts.py]
```

## Architecture Decisions

| ID | Decision | Options Considered | Chosen | Rationale |
|----|----------|--------------------|--------|-----------|
| AD-001 | Centralizar tratadores de exceção em `main.py` | handler por endpoint vs handler global | Global | reduz duplicação e garante contrato uniforme |
| AD-002 | Usar `ErrorResponse` como resposta padrão | texto puro vs estrutura JSON | Estrutura JSON | melhora consumo por clientes e observabilidade |
| AD-003 | Não expor detalhes internos | stack trace em body vs mensagem genérica | Mensagem genérica | preserva segurança operacional |

## Data Model Summary

N/A — no persistent data model required for this feature.

## API Surface Summary

N/A — no new public API routes. The feature adjusts existing error handling behavior of current endpoints.

## Testing Strategy

| Tier | Tool | Scope | Mock Boundary | Install |
|------|------|-------|---------------|---------|
| Unit | pytest | validação de requests inválidos e erros globais | FastAPI TestClient | configured |
| Integration | pytest | endpoints da API com payloads válidos/inválidos | app em memória | configured |
| Security | grep/static review | garantir ausência de stack trace e dados sensíveis nos erros | n/a | configured |
| Coverage | pytest --cov (opcional) | medir regressão do contrato de erro | n/a | configured |

## Acceptance Test Stubs

| Req ID | Test File | Stub Blocks (framework-native) | RED Status |
|--------|-----------|----------------------------------|------------|
| TR-001 | tests/test_error_contracts.py | `def test_invalid_payload_returns_standardized_422_response()` | pending |
| TR-002 | tests/test_error_contracts.py | `def test_invalid_payload_returns_standardized_422_response()` | pending |
| TR-003 | tests/test_error_contracts.py | `def test_unexpected_error_returns_standardized_500_response()` | pending |
| TR-004 | tests/test_health.py | `def test_health()`, `def test_sugerir_v1()` | passing |
| TR-005 | tests/test_error_contracts.py | `def test_invalid_payload_returns_standardized_422_response()` | pending |

## Error Handling Strategy

| Error Category | Pattern | Response | Retry |
|----------------|---------|----------|-------|
| Validation | `RequestValidationError` | `422` + `ErrorResponse` | no |
| Bad request | `ValueError` | `400` + `ErrorResponse` | no |
| Internal server error | generic exception | `500` + generic message | no |

## Integration Points

| Spec Reference | System/Service | Technical Approach | Contract |
|----------------|----------------|--------------------|----------|
| TR-001 | FastAPI validation layer | use `RequestValidationError` handler | `ErrorResponse` + HTTP 422 |
| TR-003 | app exception layer | catch unexpected exceptions globally | HTTP 500 + generic message |
| TR-005 | pytest suite | add negative coverage | tests/test_error_contracts.py |

## Risk Mitigation

| Risk (from spec) | Likelihood | Impact | Mitigation | Owner |
|-------------------|------------|--------|------------|-------|
| regressão no contrato de sucesso | medium | high | manter handlers concentrados e validar suíte completa | API layer |
| vazamento de stack trace | low | high | mensagem genérica e sem detalhes internos | app layer |

## Requirement Coverage Map

| Req ID | Component(s) | File Path(s) | Function(s)/Symbol(s) | Notes |
|--------|--------------|--------------|------------------------|-------|
| TR-001 | Error schema | `core/schemas.py` | `ErrorResponse` | central model |
| TR-002 | validation handling | `main.py` | `validation_exception_handler` | 422 handler |
| TR-003 | generic internal exception handling | `main.py` | `generic_exception_handler` | 500 handler |
| TR-004 | endpoint compatibility | `interfaces/v1_agent_api.py`, `interfaces/v2_client_api.py` | route functions | preserved behavior |
| TR-005 | negative tests | `tests/test_error_contracts.py` | `test_invalid_payload_returns_standardized_422_response`, `test_unexpected_error_returns_standardized_500_response` | validation coverage |

## Project Structure

### Source Code

```text
core/
  schemas.py
interfaces/
  v1_agent_api.py
  v2_client_api.py
main.py
tests/
  test_error_contracts.py
  test_health.py
```

## Implementation Hints

- **HINT-001**: use `RequestValidationError` before custom exceptions to preserve the FastAPI validation contract.
- **HINT-002**: generic exception handlers should not re-expose internal data; keep messages external-safe.
- **HINT-003**: validate the whole suite after each correction to guard against regressions in existing endpoints.
