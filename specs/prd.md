---
document_type: product-requirements
product: "Assistente de IA para Suporte GLPI"
created: 2026-10-30
updated: 2026-10-30
prd_maturity: planning-ready
---

# Product Requirements Document: Assistente de IA para Suporte GLPI

> Canonical Product Document

## Product Overview

Assistente de IA para suporte em GLPI que apoia o agente humano na Fase 1 — sugestão de resposta, classificação de ticket, artigos da base de conhecimento e criação de ticket somente após aprovação — e prepara o mesmo núcleo para o autoatendimento do cliente na Fase 2, com guardrails mais rígidos e escalonamento automático. O produto serve agentes de suporte, gestores de atendimento e, numa segunda fase, clientes finais que interagem direto com o assistente. A proposta central é usar a mesma base arquitetural nas duas fases, preservando o núcleo de orquestração, RAG, integração GLPI e guardrails, variando apenas interface e políticas por perfil.

Proveniência: [README](../README.md) (visão geral e público-alvo) e [Especificação Técnica — Assistente de IA](../docs/legacy/spec/Especificação Técnica — Assistente de IA.md) §1–2.

## Vision and Why Now

A equipe de suporte usa o GLPI para gestão de tickets, ativos e base de conhecimento, e o volume e a repetitividade dos atendimentos consomem tempo dos agentes. A visão é construir um assistente de suporte inteligente, seguro e extensível, capaz de acelerar o atendimento em GLPI e preparar a organização para um modelo de suporte mais escalável e automatizado no futuro. A urgência vem da pressão por primeira resposta rápida somada à necessidade de manter qualidade, segurança e rastreabilidade: enquanto isso não é endereçado, o custo operacional cresce e a base de conhecimento continua subutilizada. A mudança pretendida é reduzir o tempo de primeira resposta em −30% e elevar a acurácia de classificação para ≥85%, sem substituir a decisão humana.

Proveniência: [Especificação Técnica](../docs/legacy/spec/Especificação Técnica — Assistente de IA.md) §1.1–1.2; [README](../README.md) (objetivo de longo prazo).

## Problem Statement

O suporte no GLPI frequentemente lida com tickets repetitivos e com necessidade de resposta rápida, mas a equipe também precisa manter qualidade, segurança e rastreabilidade. Os agentes perdem tempo com atendimentos repetitivos, a classificação de categoria/urgência é inconsistente e os artigos da base de conhecimento não são reaproveitados na hora do atendimento. Sem apoio, o tempo de primeira resposta permanece alto, a acurácia da classificação cai e a organização não constrói a base necessária para um futuro autoatendimento. O assistente atua como apoio cognitivo: sugere respostas, identifica artigos relevantes da base, classifica o ticket e reduz a carga operacional sem substituir a decisão humana.

Proveniência: [README](../README.md) (problema que resolve); [Especificação Técnica](../docs/legacy/spec/Especificação Técnica — Assistente de IA.md) §1.1.

## Background and Evidence

Não há discovery formal registrado (sem ledger EVD-### neste bootstrap). Fontes concretas desta baseline, com evidência distinguida de premissa:

- **Evidência documental**: [Especificação Técnica §1.1](../docs/legacy/spec/Especificação Técnica — Assistente de IA.md) declara volume e repetitividade como causa do consumo de tempo; [README](../README.md) descreve o mesmo problema; [Backlog Inicial — MVP Fase 1](../docs/legacy/plan/Backlog Inicial — MVP Fase 1.md) e [Checklist de Entregáveis](../docs/legacy/plan/Checklist de Entregáveis — Assistente de IA para GLPI.md) documentam a sequência de entregáveis acordada.
- **Premissa (não medida)**: não há baseline de tempo de primeira resposta, taxa de acerto de classificação ou cobertura de KB registrada — os alvos da §1.2 são metas de negócio assumidas, não medições atuais.
- **Evidência de implementação**: núcleo existente (`core/`, `interfaces/`, `tests/`) com 8 arquivos de teste e rastreador de etapas em [Especificações por precedência — SP1 a SP11](../docs/legacy/spec/Especificações por precedência — SP1 a SP11.md).

## Target Users, Stakeholders, and Core Personas

### Target Users

- Agentes de suporte do GLPI — usuário primário da Fase 1, atende tickets pelo fluxo do GLPI e usa o assistente como apoio cognitivo.
- Clientes finais — usuários da Fase 2, interagem direto com o assistente via portal/widget/API do GLPI.
- Gestores de atendimento — consomem métricas de qualidade e produtividade.

### Stakeholders

- Gestores de atendimento — donos das metas de tempo de resposta e acurácia.
- Responsáveis por segurança e dados — validam guardrails, PII e auditoria (RNF4, RNF7).
- Mantenedores do projeto — governança de processo (branch `dev`, promoção para `main` autorizada), conforme [AGENTS.md](../AGENTS.md).
- Equipe de manutenção do GLPI — impactada apenas indiretamente (core do GLPI intocado).

### Core Personas

- **Agente de suporte (Fase 1)**: recebe tickets repetitivos sob pressão de SLA; quer um rascunho de resposta com nível de confiança e sugestão de categoria/urgência para aprovar ou editar; pain points: retrabalho de classificação e tempo perdido procurando artigos.
- **Cliente final (Fase 2)**: tem dúvida pontual e espera resposta imediata; quer auto-resolução quando a resposta é clara e conexão com humano quando há dúvida ou sensibilidade; pain point: fila para questões simples.
- **Gestor de atendimento**: precisa de consistência, auditoria e métricas; quer reduzir primeira resposta sem perder controle; pain point: ausência de rastreabilidade da qualidade das respostas.

## User Needs / Jobs To Be Done

- "Quando recebo um ticket repetitivo, quero uma sugestão de resposta com confiança e artigos da base, para responder mais rápido sem errar a classificação."
- "Quando a sugestão está boa, quero aprovar (ou editar e aprovar) e que o ticket seja criado no GLPI exatamente uma vez, com auditoria da ação."
- "Quando rejeito ou edito uma sugestão, quero registrar feedback fácil, para que o sistema melhore."
- "Como gestor, quero ver latência, confiança e aceitação, para medir o ganho real."
- "Como cliente (Fase 2), quero resposta imediata quando o sistema tem confiança e escalonamento para humano quando não tem."

## Product Principles or UX Principles

- **Aprovação humana primeiro**: na Fase 1, criação de ticket exige aprovação do agente (`requer_aprovacao` sempre true).
- **Núcleo único, interface por perfil**: a diferença entre fases é feita pela camada de interface e pelas políticas de guardrails, nunca por núcleos duplicados.
- **Guardrails como requisito central**: validação de conteúdo, PII e política de escalonamento fazem parte da arquitetura, não são camada opcional.
- **Soberania de dados**: LLM local obrigatório na Fase 1 (RNF5); credenciais só em variáveis de ambiente/secret manager (RNF7).
- **Rastreabilidade e idempotência**: 100% das interações auditadas (RNF4) e chave de idempotência obrigatória na criação de tickets (RNF8).

## Scope Summary

A fronteira decidida para esta entrega de validação é a Fase 1 (apoio ao agente) em piloto controlado, mais os preparatórios de Fase 2 já embutidos no núcleo (RF2.x). A Fase 2 completa (portal/widget no ar com auto-resolução) só é liberada após o gate objetivo da §10.2 da especificação. Fonte: [Especificação Técnica §2](../docs/legacy/spec/Especificação Técnica — Assistente de IA.md).

### In-Scope Capabilities

- Sugestão assistida ao agente (resposta, artigos, tickets similares, confiança) — Fase 1.
- Classificação de categoria, urgência e impacto — Fase 1.
- Aprovação humana e criação idempotente de ticket no GLPI — Fase 1.
- Feedback estruturado, auditoria e observabilidade — Fase 1.
- Contratos de API versionados, incluindo contratos de erro e validação.
- Guardrails por perfil (conteúdo, PII, aprovação, escalonamento).
- Preparatórios de autoatendimento no mesmo núcleo (RF2.x) — validados como contrato, sem operação em produção nesta entrega.

### Out-of-Scope Items

- Substituir agentes humanos — não-objetivo explícito (§1.3 da especificação).
- Treinar modelos próprios do zero — não-objetivo (§1.3); usa-se LLM pronto, preferencialmente local.
- Alterar o núcleo do GLPI ou seu banco de dados — não-objetivo (§1.3) e regra de implementação.
- Operação plena da Fase 2 (portal/widget em produção) — adiada até o gate de prontidão.
- UI própria para a Fase 2 — decisão registrada em ADR-0001 ([specs/sad.md](sad.md)): o autoatendimento é exposto como API (`/v2/atender`) consumida pelo portal GLPI já existente.
- Autenticação/autorização próprias do assistente além do OAuth2 do GLPI (RNF6) — fora desta entrega.

### Requisitos funcionais — Fase 1 (RF1.x)

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF1.1 | Receber pergunta do agente via API/painel | Must |
| RF1.2 | Identificar o solicitante do ticket a partir de e-mail/login | Must |
| RF1.3 | Sugerir resposta baseada em RAG na base de conhecimento | Must |
| RF1.4 | Sugerir categoria, urgência e impacto | Must |
| RF1.5 | Listar até 5 artigos relevantes da base | Should |
| RF1.6 | Criar ticket no GLPI somente após aprovação do agente | Must |
| RF1.7 | Registrar feedback (útil / não útil / editado) por sugestão | Must |
| RF1.8 | Sugerir tickets históricos similares | Should |
| RF1.9 | Adicionar acompanhamento em ticket existente | Should |
| RF1.10 | Exibir nível de confiança da resposta | Must |

### Requisitos funcionais — Fase 2 (RF2.x — preparatórios desde a Fase 1)

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF2.1 | Atender cliente diretamente via portal/widget | Must (F2) |
| RF2.2 | Auto-resolver quando confiança ≥ limiar e categoria permitida | Must (F2) |
| RF2.3 | Escalar automaticamente para ticket humano caso contrário | Must (F2) |
| RF2.4 | Aplicar guardrails de conteúdo e ação por perfil | Must (F2) |
| RF2.5 | Bloquear/anonimizar dados sensíveis na resposta | Must (F2) |
| RF2.6 | Reutilizar exatamente o mesmo núcleo da Fase 1 | Must (F2) |

### Requisitos não funcionais (RNF)

| ID | Requisito | Alvo |
|----|-----------|------|
| RNF1 | Latência p95 do endpoint de sugestão | ≤ 5s |
| RNF2 | Latência p95 do endpoint de criação de ticket | ≤ 2s |
| RNF3 | Disponibilidade | ≥ 99% em horário comercial |
| RNF4 | Auditoria completa de interações | 100% logado |
| RNF5 | Soberania — suporte a LLM local | Obrigatório na F1 |
| RNF6 | Autenticação OAuth2 (GLPI 11+) / token por perfil | GLPI 11+ |
| RNF7 | Isolamento de credenciais | Variáveis de ambiente / secret manager |
| RNF8 | Idempotência na criação de tickets | Chave de idempotência obrigatória |
| RNF9 | Testes automatizados no núcleo | ≥ 80% cobertura |

Numeração RF/RNF preservada de [Especificação Técnica §4–5](../docs/legacy/spec/Especificação Técnica — Assistente de IA.md); nenhum requisito novo foi criado nesta migração.

## Product Capability Map

Only decided in-scope capability clusters receive stable IDs.

| Capability ID | Capability | Priority | Outcome |
|---------------|------------|----------|---------|
| CAP-001 | Sugestão assistida ao agente | P1 | Resposta rascunhada com artigos, tickets similares e confiança em ≤5s |
| CAP-002 | Classificação de tickets | P1 | Categoria, urgência e impacto sugeridos com acurácia ≥85% |
| CAP-003 | Aprovação e criação de ticket | P1 | Ticket criado no GLPI só após aprovação, uma única vez (idempotente) |
| CAP-004 | Feedback, auditoria e observabilidade | P1 | Interações 100% auditadas, feedback estruturado e métricas básicas |
| CAP-005 | Contratos de API versionados | P1 | Contratos de entrada, saída e erro documentados e validados por testes |
| CAP-006 | Guardrails por perfil | P1 | Conteúdo validado, PII protegido, decisão rastreável antes da entrega |
| CAP-007 | Autoatendimento Fase 2 | P2 | Atendimento direto com auto-resolução ou escalonamento automático |
| CAP-008 | Núcleo compartilhado entre fases | P2 | Mesmo orquestrador/RAG/LLM/guardrails servindo as duas interfaces |
| CAP-009 | Gate de prontidão e métricas | P2 | Evidência objetiva para liberar a Fase 2 (§10.2) |

## Success Metrics / KPIs / Desired Outcomes

| Metric | Target | Why It Matters | Measurement Window |
|--------|--------|----------------|--------------------|
| Tempo médio de primeira resposta | −30% | Objetivo primário de negócio da Fase 1 | Piloto ≥ 4 semanas |
| Taxa de acerto de classificação (categoria/urgência) | ≥85% | Qualidade da sugestão e do triagem | Piloto ≥ 4 semanas |
| Sugestões aceitas (reaproveitamento da KB) | ≥70% | Prova valor do RAG para o agente | Piloto ≥ 4 semanas |
| Cobertura de categorias na KB | ≥80% | Prepara autoatendimento (Fase 2) | Antes do gate |
| Latência p95 do endpoint de sugestão | ≤5s (RNF1) | Experiência do agente no fluxo real | Contínua |
| Auditoria de interações | 100% logado (RNF4) | Conformidade e rastreabilidade | Contínua |
| Cobertura de testes do núcleo | ≥80% (RNF9) | Estabilidade das mudanças | Contínua |
| Taxa de auto-resolução Fase 2 | Medir pós-gate | Valor do autoatendimento | Pós-liberação F2 |
| CSAT do cliente no autoatendimento | Medir pós-gate | Qualidade percebida pelo cliente | Pós-liberação F2 |

## Assumptions

- A base de conhecimento do GLPI contém artigos suficientes e atualizados para alimentar o RAG nas categorias mais frequentes.
- LLM local (Ollama) atende a latência p95 ≤5s no hardware disponível — não validado em produção.
- Os alvos de negócio (−30%, ≥85%, ≥70%, ≥80%) partem de baseline não medida; serão calibrados no piloto.
- Agentes de suporte participarão do piloto e registrarão feedback com constância.
- A Fase 2 reutiliza o núcleo sem reescrita (RF2.6) — premissa arquitetural central.

## Constraints

- Não alterar o núcleo do GLPI ou seu banco de dados (§1.3; regra de implementação do projeto).
- LLM local obrigatório na Fase 1 (RNF5); provedor trocável por configuração, mas soberania de dados mantida.
- Credenciais nunca no repositório: variáveis de ambiente e secret manager (RNF7).
- Criação de ticket somente após aprovação humana (RF1.6) — não negociável.
- Núcleo compartilhado entre fases, sem duplicação de lógica (RF2.6).
- Idempotência obrigatória na criação de tickets (RNF8) e auditoria completa (RNF4).
- Guardrails são parte central da arquitetura, não camada opcional.
- Governança: desenvolvimento em `dev`; promoção para `main` com autorização prévia; versão `vx.x.x` incrementada na promoção ([AGENTS.md](../AGENTS.md), [Checklist §4](../docs/legacy/plan/Checklist de Entregáveis — Assistente de IA para GLPI.md)).

## Dependencies

- Instância GLPI 11+ com API REST e OAuth2 (RNF6) e base de conhecimento existente.
- Cliente `glpi-utils` (wrapper único de integração).
- Runtime LLM local — Ollama (Fase 1); provedores nuvem apenas via abstração configurável.
- Vector store (Qdrant ou pgvector — decisão pendente, ver PDQ-002).
- Stack: Python 3.11+, FastAPI, Pydantic, pytest + httpx.
- Acesso a ambiente de piloto com agentes reais para coleta de métricas.

## Risks

- **LLM alucina respostas** *(impacto: Alto)*: RAG obrigatório + exibição de confiança + revisão humana na Fase 1.
- **Vazamento de dados de clientes** *(impacto: Crítico)*: LLM local na Fase 1; guardrails de PII na Fase 2.
- **Base de conhecimento desatualizada** *(impacto: Alto)*: job de re-indexação periódica; feedback sinaliza gaps.
- **Rate limit na API do GLPI** *(impacto: Médio)*: cache + backoff + async.
- **Custo elevado de tokens** *(impacto: Médio)*: Ollama local; cache de respostas; prompts enxutos.
- **Baixa adesão dos agentes** *(impacto: Alto)*: piloto com early adopters + métricas de ganho visíveis.
- **Regressão na Fase 2** *(impacto: Alto)*: gate formal; rollback por feature flag.

Proveniência: [Especificação Técnica §11](../docs/legacy/spec/Especificação Técnica — Assistente de IA.md).

## Open Questions

- **PDQ-001**: a rota 6.4 da especificação (`/fase2/atender`) diverge do código (`/v2/atender`, prefixo de `interfaces/v2_client_api.py`) — decisão registrada para atualização da spec no âmbito do plano SP3.
- **PDQ-002**: Vector store — Qdrant ou pgvector (especificação §9 deixa em aberto).
- **PDQ-003**: orquestração RLM — LangChain ou LlamaIndex (especificação §9 deixa em aberto).
- **PDQ-004**: ~~ausência de `specs/sad.md`~~ — resolvido durante este bootstrap: o documento de contexto técnico foi criado em [specs/sad.md](sad.md) com ADR-0001 e ADR-0002 accepted.

## Release or Validation Approach

Valor e outcomes são validados por piloto controlado com agentes reais antes de qualquer expansão. A Fase 2 só é liberada quando a especificação §10.2 estiver atendida:

- taxa de aceitação de sugestões ≥70% por ≥4 semanas;
- taxa de acerto de classificação ≥85%;
- latência p95 ≤5s consistentemente;
- zero incidentes de segurança/dados em logs;
- cobertura da KB ≥80% das categorias mais frequentes;
- guardrails implementados e testados em modo permissivo;
- plano de escalonamento documentado e validado.

A Fase 1 só considera o MVP pronto com evidência objetiva (testes, auditoria, aprovação humana sempre exigida), conforme o critério de pronto do [Checklist §3](../docs/legacy/plan/Checklist de Entregáveis — Assistente de IA para GLPI.md).

## Domain Glossary / Terminology

- **GLPI**: sistema de gestão de tickets, ativos e base de conhecimento usado pela equipe de suporte; núcleo intocado pelo projeto.
- **RAG**: geração aumentada por recuperação — recupera artigos da base de conhecimento por similaridade e os injeta no contexto do LLM.
- **Guardrails**: regras de segurança e governança que validam conteúdo, dados sensíveis e ações antes da entrega da resposta.
- **Idempotência**: propriedade que garante que repetir a criação de ticket com a mesma chave não gera duplicata (RNF8).
- **Escalonamento**: encaminhamento automático do atendimento para humano quando a confiança é baixa, a categoria é sensível ou o limite de tentativas é atingido.
- **Confiança (limiar)**: score do modelo que decide entre auto-resolução e escalonamento na Fase 2 (`confiança ≥ 0.85`, §7.3).
- **SP**: etapa de especificação por precedência (SP1–SP11) que organiza a execução do projeto.

## Handoff Guidance

- **Product intent to preserve**: apoio ao agente humano com aprovação obrigatória antes de criar ticket; núcleo único compartilhado entre Fase 1 e Fase 2; auditoria e idempotência sempre presentes.
- **Scope boundaries to respect**: esta entrega valida a Fase 1 (+ preparatórios RF2.x); a Fase 2 em produção só após o gate §10.2; core do GLPI intocado.
- **Critical constraints**: LLM local obrigatório na Fase 1 (RNF5); guardrails como requisito central; segredos fora do repositório; governança `dev`/`main`.
- **Open decisions needing technical input**: rota `/fase2/atender` vs `/v2/atender` (PDQ-001); vector store (PDQ-002); orquestração RLM (PDQ-003). UI própria da Fase 2 é decisão fechada (ADR-0001, [specs/sad.md](sad.md)).

## Project Context Baseline Updates

- Rastreador de etapas em [Especificações por precedência — SP1 a SP11](../docs/legacy/spec/Especificações por precedência — SP1 a SP11.md): SP1, SP3 e SP4 em EM ANDAMENTO; SP2 DONE; SP5–SP11 declarados DONE — declaração sem evidência de validação correspondente, sujeita a reavaliação.
- Lacunas de implementação reconhecidas para o núcleo: contratos de erro/validação (SP3), integração GLPI real (SP4), LLM real (SP6), guardrails invocados em todos os fluxos (SP7), persistência de observabilidade (SP8).
- Divergência conhecida entre spec (§6.4 `/fase2/atender`) e código (`/v2/atender`), com decisão a registrar na atualização da especificação.
- Planos de execução existentes em [docs/plan](../docs/legacy/plan/README.md) para SP3, SP6, SP7, SP8 e SP11; SP2 e SP4 ainda sem plano correspondente (dívida de processo).
- Decisões arquiteturais registradas em [specs/sad.md](sad.md): ADR-0001 (Fase 2 via API para o portal GLPI, sem UI própria) e ADR-0002 (adoção do framework SDDP, com `docs/spec` e `docs/plan` como fonte migrada/histórica).
