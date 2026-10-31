# Briefing de produto: Assistente de IA para suporte no GLPI

## Resumo executivo

O projeto deve entregar primeiro um assistente de apoio ao agente de suporte no GLPI, com foco em reduzir o tempo de primeira resposta, padronizar a classificação de categoria e urgência, e reaproveitar a base de conhecimento da organização.

A partir desse núcleo compartilhado, a segunda fase evolui para atendimento automatizado via API para o portal GLPI, sem duplicar lógica de negócio e sem criar uma interface própria de cliente no escopo atual do projeto.

## Problema de negócio

Os agentes de suporte lidam com volume alto de tickets repetitivos e com maior pressão por rapidez e qualidade. Sem apoio inteligente, o processo fica mais lento por:

- retrabalho na triagem e classificação;
- baixa reutilização da base de conhecimento;
- respostas inconsistentes ou demoradas;
- dificuldade de rastrear e medir qualidade e tempo de resposta;
- sobrecarga de tarefas operacionais simples no fluxo de atendimento.

## Valor para o cliente e para a operação

### Para os agentes de suporte
- resposta sugerida com contexto do ticket;
- artigos relevantes da base de conhecimento;
- classificação mais consistente de categoria, urgência e impacto;
- aprovação humana antes de qualquer ação crítica;
- menos tempo gasto em trabalho repetitivo.

### Para gestores e operação
- métricas de tempo de resposta, qualidade e aceitação;
- rastreabilidade de decisões e feedback;
- processo mais previsível e escalável;
- melhoria contínua com base em dados de interação.

### Para o cliente final
- resposta mais rápida quando houver confiança do sistema;
- escalonamento para humano quando necessário;
- melhor experiência em uma etapa posterior, sem quebrar a governança de segurança.

## Visão da arquitetura

A decisão de arquitetura do projeto é manter um núcleo compartilhado entre as fases:

- orquestração;
- busca e RAG;
- integração com GLPI;
- adapter de LLM;
- guardrails;
- schemas e contratos;
- observabilidade e feedback.

A diferenciação entre fases está na interface e nas políticas de uso, não na duplicação do núcleo.

## Definição das fases

### Fase 1 — apoio ao agente humano

Objetivo: acelerar o atendimento sem substituir a supervisão humana.

Funcionalidades esperadas:
- painel interno do suporte;
- contexto do ticket e histórico relevante;
- busca por artigos e tickets similares;
- classificação sugerida de categoria e urgência;
- resposta sugerida com nível de confiança;
- aprovação do agente antes de criar ou escalar ações críticas;
- persistência de feedback e observabilidade.

### Fase 2 — portal do cliente via API-only

Objetivo: preparar o mesmo núcleo para autoatendimento controlado.

Direção de arquitetura:
- a Fase 2 não terá interface própria neste projeto;
- o portal GLPI consome a API do mesmo núcleo;
- regras mais rígidas para identidade, escalonamento e segurança;
- cliente final acessa apenas fluxos apropriados para seu perfil.

### Fase futura (opcional)

Uma interface externa, widget ou app complementar pode ser adicionada depois, como cliente da API, mas isso não é prioridade de negócio neste momento nem requisito de Fase 2.

## Roadmap orientado por valor

### Ordem de prioridade
1. Apoio ao agente de suporte
2. Resposta sugerida com contexto e KB
3. Classificação confiável de categoria/urgência
4. Observabilidade e feedback
5. Autoatendimento via API para portal GLPI

### Roadmap sugerido

#### Wave 1 — Núcleo do suporte
- contratos de erro e validação da API;
- integração com GLPI real;
- LLM real com adapter configurável;
- guardrails e aprovação humana;
- observabilidade e feedback.

#### Wave 2 — Fase 2 API-only
- contrato estável de atendimento para portal GLPI;
- escalonamento com ticket real;
- gate de prontidão para liberação.

#### Wave 3 — Reavaliação e maturidade
- medir evidências reais de ganho;
- ajustar guardrails, UX e métricas;
- decidir expansão ou consolidação do produto.

## Critérios de sucesso

- reduzir o tempo de primeira resposta;
- aumentar consistência na classificação;
- reduzir retrabalho dos agentes;
- aumentar a reutilização da base de conhecimento;
- manter aprovação humana em ações críticas;
- preservar rastreabilidade e auditoria;
- preparar a transição para o portal do cliente sem reescrever o núcleo.

## Decisões-chave

- Fase 1 é a prioridade principal.
- Fase 2 será API-only, conforme definição do projeto.
- O núcleo compartilhado é obrigatório.
- A interface do cliente não deve ser criada antes do gate de maturidade.
- O valor mais relevante para o cliente é rapidez, qualidade e governança, não automação irrestrita.

## Próximos passos

- fechar o epic E001 em SDDP;
- implementar o núcleo da Fase 1 em ondas;
- validar a arquitetura com testes e evidências reais;
- preparar a transição para a API do portal GLPI apenas após o gate apropriado.
