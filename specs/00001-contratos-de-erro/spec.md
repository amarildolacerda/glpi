---
feature_branch: "00001-contratos-de-erro"
created: "2026-10-31"
input: "E001 Contratos de erro e validação"
spec_type: "technical"
spec_maturity: "draft"
epic_id: "E001"
epic_sources: "{PRD:CAP-005}"
---

# Feature Specification: Contratos de erro e validação da API

**Feature Branch**: `00001-contratos-de-erro`  
**Created**: 2026-10-31  
**Status**: Draft  
**Spec Type**: technical  
**Spec Maturity**: draft  
**Epic ID**: E001  
**Epic Sources**: {PRD:CAP-005}  
**Product Document**: specs/prd.md

## Problem Statement

A API atual expõe respostas de sucesso, mas não define um padrão consistente para falhas de entrada e erros inesperados. Isso torna a depuração mais difícil para agentes e integrações, pode mascarar problemas reais e dificulta a operação segura do assistente de suporte no GLPI.

## Scope

### Included

- Padronização do corpo de erro para validações e falhas internas
- Tratamento global de 400/422/500 em FastAPI
- Registro de resposta de erro sem exposição de stack trace ou detalhes sensíveis
- Cobertura de testes negativos para payloads inválidos e erros inesperados
- Alinhamento do comportamento com o contrato da API e requisitos do projeto

### Excluded

- Autenticação e autorização de usuários — fora do escopo desta feature
- Alteração do banco de dados do GLPI ou do núcleo da aplicação
- Introdução de novos endpoints ou mudanças de contrato de sucesso já existentes

### Edge Cases & Boundaries

- Payloads com campos obrigatórios ausentes ou tipos inválidos
- Requisições que acionam exceções internas e precisam retornar erro seguro
- Casos em que a resposta não pode expor detalhes técnicos do servidor

## Technical Objectives

### Objective 1 - Padrão de erro para todas as respostas de falha (Priority: P1)

Definir e validar um contrato único `ErrorResponse` para erros de contrato, validação e falha interna.

**Why this priority**: sem uma resposta estruturada, cada endpoint pode comunicar falhas de forma incompatível e difícil de consumir.

**Rationale**: o assistente e qualquer cliente do GLPI precisam interpretar erros de forma previsível, sem depender de mensagens não padronizadas.

**Deliverables**:
- Modelo `ErrorResponse` em `core/schemas.py`
- Manipulação de exceções globais em `main.py`
- Cobertura de testes de contrato em `tests/`

**Validation Criteria**:
1. **Given** um payload inválido em um endpoint, **When** a validação do FastAPI falha, **Then** a API retorna HTTP 422 com corpo `ErrorResponse`.
2. **Given** uma exceção inesperada no fluxo da aplicação, **When** o erro atinge a camada global, **Then** a API retorna HTTP 500 com mensagem genérica e sem stack trace.

### Objective 2 - Garantia de compatibilidade com o restante da API (Priority: P1)

Manter a compatibilidade com respostas de sucesso e não quebrar os comportamentos existentes em endpoints já validados.

**Why this priority**: a correção de erros não pode transformar o comportamento funcional em regressão.

**Rationale**: a feature precisa priorizar estabilidade do contrato atual e maior previsibilidade operacional.

**Deliverables**:
- Suite existente dos testes de saúde e orquestração preservada
- Testes adicionais para exceções de validação e erro interno

**Validation Criteria**:
1. **Given** os testes de regressão existentes, **When** a suíte é executada, **Then** ela continua com resultado positivo.
2. **Given** um endpoint com payload válido, **When** a rota é chamada, **Then** o contrato antigo de sucesso permanece inalterado.

### Technical Constraints

- Não expor stack trace nem detalhes internos em respostas públicas
- O formato de erro deve ser consistente entre endpoints da API
- A correção deve respeitar o driver atual da aplicação e o modo mock do cliente GLPI

## Integration Points

- **IP-001**: `main.py` depende do modelo `ErrorResponse` para tratar exceções globais e manter resposta padrão
- **IP-002**: endpoints em `interfaces/v1_agent_api.py` e `interfaces/v2_client_api.py` dependem do contrato de erro para falhas de entrada e validação
- **IP-003**: integrações com GLPI e LLM continuam funcionando sem mudança de contrato de sucesso

## Requirements

### Technical Requirements

- **TR-001** [OBJ1]: O sistema MUST expor um modelo `ErrorResponse` com `code`, `message` e `details` padronizados.
- **TR-002** [OBJ1]: O sistema MUST tratar `RequestValidationError` como HTTP 422 com `ErrorResponse`.
- **TR-003** [OBJ1]: O sistema MUST tratar exceções inesperadas como HTTP 500 com resposta segura e sem revelar stack trace.
- **TR-004** [OBJ1]: O sistema MUST manter o comportamento atual dos endpoints de sucesso sem regressões.
- **TR-005** [OBJ2]: O sistema MUST ter testes negativos cobrindo payload inválido e falha interna simulada.

## Assumptions & Risks

### Assumptions

- As rotas atuais permanecem compatíveis com clientes já em uso
- O ambiente de execução tem acesso à suíte de testes e às dependências do projeto
- A aplicação não expõe segredos em erros de runtime

### Risks

- **Risco de regressão de contrato** *(likelihood: medium, impact: high)*: alterações no handler global podem afetar todos os endpoints e clientes
- **Risco de vazamento de detalhes internos** *(likelihood: low, impact: high)*: resposta com stack trace ou dados sensíveis pode comprometer segurança operacional

## Implementation Signals

- `NEW-API`
- `NEW-CONFIG`
- `NEW-ENTITY` — `ErrorResponse`

## Success Criteria

### Measurable Outcomes

- **SC-001** [OBJ1]: toda requisição inválida retorna 422 com corpo `ErrorResponse` consistente
- **SC-002** [OBJ1]: qualquer falha inesperada retorna 500 com mensagem genérica e sem vazamento interno
- **SC-003** [OBJ2]: a suíte atual de testes continua passando sem regressões
