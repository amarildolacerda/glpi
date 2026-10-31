# Roadmap do projeto

## Visão

Este roadmap centraliza o planejamento presente e futuro do projeto de assistente de IA para suporte no GLPI, mantendo a visão de produto, arquitetura e execução em um único ponto de referência.

## Direção estratégica

- Priorizar a Fase 1: apoio ao agente humano.
- Manter o núcleo compartilhado entre as fases.
- Usar a Fase 2 como evolução do mesmo backend, não como reescrita.
- Conservar guardrails, aprovação humana, auditoria e rastreabilidade como requisitos centrais.

## Fases

### Fase 1 — Apoio ao agente humano

**Objetivo:** reduzir o tempo de primeira resposta e aumentar a qualidade da triagem e do atendimento.

**Entregas prioritárias:**
- painel interno do suporte;
- contexto do ticket e histórico relevante;
- busca por artigos e tickets similares;
- classificação de categoria, urgência e impacto;
- resposta sugerida com nível de confiança;
- aprovação humana antes de ações críticas;
- observabilidade e feedback.

**Critérios de sucesso:**
- tempo de primeira resposta reduzido;
- maior consistência na classificação;
- uso mais efetivo da base de conhecimento;
- ações críticas sempre aprovadas por humano;
- auditabilidade e métricas de qualidade.

### Fase 2 — Portal do cliente via API-only

**Objetivo:** permitir autoatendimento controlado usando o mesmo núcleo do projeto.

**Direção:**
- a Fase 2 não terá interface própria neste projeto;
- o portal GLPI consome a API do mesmo núcleo;
- regras mais rígidas de segurança, identidade e escalonamento;
- expansão gradual após validação do núcleo e do gate de prontidão.

### Fase futura (opcional)

**Objetivo:** atender cenários externos ou complementares sem duplicar a arquitetura principal.

**Direção:**
- qualquer interface complementar deve consumir a mesma API;
- não é prioridade atual;
- não deve ser criada antes da maturidade do núcleo e do gate de transição.

## Consistência com a especificação

- E001 em [specs/00001-contratos-de-erro/spec.md](specs/00001-contratos-de-erro/spec.md) define a base de contrato e segurança das respostas de erro como pré-requisito do núcleo.
- [specs/project-plan.md](specs/project-plan.md) mantém a mesma sequência de execução: E001, E002–E005 como núcleo da Fase 1, depois E006–E008 para a Fase 2 e o gate.
- Este roadmap preserva a mesma ordem, sem introduzir UI própria para cliente antes do gate nem duplicar o núcleo entre fases.

## Roadmap por ondas

### Wave 1 — Núcleo fechado

- contratos de erro e validação da API;
- integração com GLPI real;
- LLM real e adaptável por configuração;
- guardrails efetivos e aprovação humana;
- observabilidade e persistência de feedback.

### Wave 2 — Fase 2 API-only

- contrato estável de atendimento para portal GLPI;
- escalonamento e criação de ticket real;
- reuso do núcleo já validado.

### Wave 3 — Reavaliação e gate

- validar evidências reais de ganho;
- confirmar readiness do suporte ao cliente;
- decidir liberação ou ajustes antes da expansão.

## Roadmap por prioridade

1. Apoio ao agente de suporte
2. Resposta sugerida com contexto e base de conhecimento
3. Classificação confiável de categoria e urgência
4. Observabilidade e feedback
5. Autoatendimento via API para portal GLPI

## Dependências de execução

- E001: contratos de erro e API
- E002: integração real com GLPI
- E003: LLM real
- E004: guardrails efetivos
- E005: observabilidade e feedback
- E006: contrato de atendimento para portal GLPI
- E007: escalonamento com ticket real
- E008: gate de prontidão da Fase 2

## Critérios de pronto do roadmap

- alinhamento com specs/prd.md, specs/sad.md e specs/project-plan.md;
- decisões registradas e revisáveis;
- entregas priorizadas por valor para clientes e operação;
- execução em ondas compatíveis com o fluxo lean SDDP;
- evidência objetiva antes de avançar para cada etapa.

## Observações

- Este arquivo funciona como o mapa central do planejamento presente e futuro.
- Deve ser revisado sempre que houver mudança de direção de produto, prioridade ou arquitetura.
- A implementação deve seguir o fluxo lean: spec → plan → implement → QC → commit.
