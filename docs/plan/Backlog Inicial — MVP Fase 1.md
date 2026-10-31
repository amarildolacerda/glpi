# Backlog Inicial — MVP Fase 1

Versão: 1.0
Status: Aprovada
Última atualização: 31/10/2026

---

## 1. Objetivo do backlog

Este backlog define a sequência inicial de desenvolvimento para a Fase 1 do assistente de IA para GLPI, priorizando um MVP funcional e seguro antes de expandir para a Fase 2.

A ordem de execução foi pensada para reduzir risco, manter a arquitetura coerente e garantir que cada componente entregue tenha valor real para o agente humano.

---

## 2. Sequência sugerida de desenvolvimento

### Fase 1 — Infraestrutura e base do projeto

- [ ] Criar estrutura inicial do projeto
- [ ] Configurar ambiente Python 3.11+
- [ ] Definir dependências principais (`fastapi`, `pydantic`, `pytest`, etc.)
- [ ] Configurar variáveis de ambiente e secrets
- [ ] Definir estrutura de diretórios esperada
- [ ] Criar configuração base do app
- [ ] Definir versionamento centralizado da implementação (`vX.X.X`)

### Fase 2 — APIs e contratos

- [ ] Definir contrato de entrada e saída da API de sugestão
- [ ] Definir contrato da API de aprovação de ticket
- [ ] Definir contrato da API de feedback
- [ ] Implementar endpoints básicos da Fase 1
- [ ] Validar payloads com Pydantic
- [ ] Implementar tratamento de erros e status HTTP

### Fase 3 — Integração com GLPI

- [ ] Criar cliente único para integração com GLPI
- [ ] Implementar consulta ao solicitante e ao ticket
- [ ] Implementar busca de histórico de tickets
- [ ] Implementar criação de ticket após aprovação
- [ ] Implementar idempotência para criação de ticket
- [ ] Registrar auditoria da ação no GLPI

### Fase 4 — Base de conhecimento e RAG

- [ ] Definir estratégia de ingestão da base de conhecimento
- [ ] Criar script de ingestão inicial
- [ ] Indexar artigos relevantes
- [ ] Implementar busca semântica por similaridade
- [ ] Montar contexto da resposta com artigos recuperados
- [ ] Validar relevância dos resultados retornados

### Fase 5 — LLM e resposta sugerida

- [ ] Implementar adapter do provedor LLM
- [ ] Definir prompt base do agente
- [ ] Receber contexto do ticket e pergunta do usuário
- [ ] Gerar resposta sugerida
- [ ] Gerar categoria, urgência e impacto
- [ ] Incluir nível de confiança na resposta
- [ ] Padronizar resposta do sistema em schema

### Fase 6 — Guardrails e segurança

- [ ] Definir regras de validação para resposta do modelo
- [ ] Bloquear respostas inseguras ou fora de escopo
- [ ] Tratar dados sensíveis e informações críticas
- [ ] Definir regra de aprovação humana antes de criar ticket
- [ ] Definir critério de escalonamento para atendimento humano
- [ ] Registrar decisões do guardrail para auditoria

### Fase 7 — Feedback, métricas e observabilidade

- [ ] Registrar interações e contexto
- [ ] Persistir feedback do agente
- [ ] Medir utilidade da resposta e edição por parte do agente
- [ ] Registrar criação de ticket e rejeição
- [ ] Criar métricas básicas de latência e uso
- [ ] Preparar base para melhoria contínua

### Fase 8 — Testes e validação

- [ ] Implementar testes unitários do núcleo
- [ ] Implementar testes de API
- [ ] Implementar testes de integração parcial com GLPI
- [ ] Validar comportamento do guardrail
- [ ] Validar criação de ticket com e sem aprovação
- [ ] Executar validação final do MVP da Fase 1

---

## 3. Entregável mínimo do MVP

O MVP da Fase 1 deve conter, ao menos:

- API REST para sugestão de resposta
- identificação do solicitante a partir do e-mail/login
- busca na base de conhecimento
- resposta sugerida com confiança
- classificação de categoria, urgência e impacto
- aprovação humana antes da criação do ticket
- feedback do agente
- criação do ticket no GLPI por ação humana
- auditoria e logs de interação

---

## 4. Critério de pronto por fase

Cada fase do backlog só pode ser considerada concluída quando:

- o requisito correspondente foi validado;
- os testes relevantes foram executados;
- a integração com o restante do sistema foi confirmada;
- o impacto em segurança e observabilidade foi revisado;
- a documentação foi atualizada, quando necessário.

---

## 5. Recomendação de execução

A execução deve partir da base do projeto para o valor de negócio mais crítico, respeitando esta ordem:

1. infraestrutura
2. contratos e API
3. GLPI
4. RAG
5. LLM
6. guardrails
7. feedback e métricas
8. testes e validação

Assim, o time consegue entregar um MVP funcional e com menor risco antes de evoluir para a Fase 2.
