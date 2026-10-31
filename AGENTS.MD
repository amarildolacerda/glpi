# AGENTS.md

## Visão geral

Este repositório tem como objetivo implantar um assistente de IA para suporte no GLPI, seguindo a especificação técnica em [docs/Especificação Técnica — Assistente de IA](docs/Especificação%20T%C3%A9cnica%20%E2%80%94%20Assistente%20de%20IA).

A prioridade inicial é a Fase 1: apoio ao agente humano. A Fase 2 (autoatendimento do cliente) deve ser pensada como evolução do mesmo núcleo, não como reescrita do projeto.

## Fonte de verdade

- A especificação técnica no diretório [docs](docs) é a referência primária para escopo, requisitos e contratos.
- Qualquer mudança de arquitetura, requisitos ou API deve ser alinhada com essa documentação antes de ser implementada.
- A implementação deve respeitar as metas de negócio e os guardrails de segurança listados na especificação.

## Objetivo do projeto

- Reduzir o tempo de primeira resposta do suporte.
- Aumentar a acurácia na classificação de categoria e urgência.
- Reaproveitar a base de conhecimento do GLPI por meio de RAG.
- Preparar a base para atendimento automatizado em uma segunda fase, sem substituir a supervisão humana.

## Regras de implementação

1. Não alterar o núcleo do GLPI ou seu banco de dados.
2. Manter o núcleo compartilhado entre Fase 1 e Fase 2.
3. Separar claramente as camadas de interface, orquestração, RAG, LLM, guardrails e integração com GLPI.
4. Priorizar a Fase 1 antes de expandir para a Fase 2.
5. Tratar a política de guardrails como parte central da arquitetura, não como camada opcional.
6. Nunca expor segredos no repositório: usar variáveis de ambiente e secret manager.
7. Registrar interações e feedback para métricas e melhoria contínua.
8. Garantir idempotência na criação de tickets e auditoria completa das ações.

## Arquitetura esperada

- Núcleo compartilhado:
  - orchestrator
  - rag
  - llm adapter
  - guardrails
  - glpi client
  - schemas
- Interfaces:
  - fase 1: apoio ao agente
  - fase 2: portal/cliente (futuro)
- Serviços de apoio:
  - feedback logger
  - métricas
  - configurações e prompts

## Stack e padrões recomendados

- Python 3.11+
- FastAPI para interfaces HTTP
- Pydantic para validação de payloads
- pytest para testes automatizados
- integração com GLPI via wrapper único (`glpi-utils` / cliente dedicado)
- suporte a LLM local como requisito da Fase 1, com provedor trocável por configuração

Se a tecnologia exata de cada componente ainda não estiver definida no momento, a decisão deve preservar os princípios da especificação: baixo acoplamento, modelagem orientada a contratos e compatibilidade com GLPI.

## Diretrizes para desenvolvimento

- Implementar em pequenas incrementos, validando um requisito por vez.
- Preferir testes antes da lógica de negócio sempre que possível.
- Manter APIs e modelos consistentes com os contratos descritos na especificação.
- As respostas sugeridas devem sempre incluir nível de confiança e devem exigir aprovação humana antes da criação de ticket.
- Evoluções futuras devem reutilizar o mesmo núcleo e não duplicar lógica entre Fase 1 e Fase 2.
- O projeto deve seguir uma abordagem de segurança e observabilidade desde o início.

## Estrutura de diretórios esperada

- `core/`
- `interfaces/`
- `feedback/`
- `config/`
- `tests/`
- `scripts/`
- `main.py`

## Critérios de pronto

Um incremento só deve ser considerado concluído quando:

- o comportamento foi validado contra a especificação;
- os testes relevantes passam;
- a API segue o contrato estabelecido;
- não há credenciais hardcoded;
- os guardrails e auditoria foram considerados;
- a solução continua compatível com o modelo de suporte do GLPI.

## Instrução para agentes

Antes de propor ou aplicar mudanças, leia a especificação técnica em [docs/Especificação Técnica — Assistente de IA](docs/Especificação%20T%C3%A9cnica%20%E2%80%94%20Assistente%20de%20IA) e mantenha a implementação alinhada ao escopo do projeto.

A prioridade é entregar um base sólida para a Fase 1, sem perder o desenho de arquitetura que permitira a extensão futura para a Fase 2.

---

Este arquivo deve ser atualizado conforme o projeto evolui, especialmente quando houver decisões de stack, padrões de código, fluxos de deploy e integração com GLPI.
