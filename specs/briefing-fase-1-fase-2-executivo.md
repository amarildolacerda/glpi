# Briefing executivo: Assistente de IA para suporte no GLPI

## Objetivo

Acelerar o atendimento de suporte no GLPI, reduzir o tempo de primeira resposta, melhorar a consistência da triagem e preparar a organização para um modelo de autoatendimento controlado no futuro.

## Problema

A operação de suporte hoje sofre com volume alto de tickets repetitivos, triagem inconsistente, baixa reutilização da base de conhecimento e pressão por resposta rápida sem perder qualidade.

## Estratégia

### Fase 1 — apoio ao agente humano
- painel interno do suporte;
- contexto do ticket e histórico relevante;
- artigos e tickets similares sugeridos;
- classificação de categoria, urgência e impacto;
- resposta sugerida com nível de confiança;
- aprovação humana obrigatória antes de ações críticas;
- observabilidade e feedback para melhoria contínua.

### Fase 2 — portal do cliente via API-only
- manter o mesmo núcleo compartilhado;
- usar API para o portal do GLPI;
- sem interface própria do cliente neste projeto;
- regras de segurança, identidade e escalonamento mais rígidas;
- expansão gradual e controlada.

## Valor para o negócio

- redução do tempo de primeira resposta;
- aumento da consistência operacional;
- menos retrabalho na rotina de suporte;
- melhor uso da base de conhecimento;
- maior rastreabilidade e auditoria;
- preparação para atendimento automatizado sem perder supervisão humana.

## Arquitetura

O projeto preserva um núcleo compartilhado entre as fases:
- orquestração;
- RAG e busca;
- integração com GLPI;
- adapter de LLM;
- guardrails;
- schemas e contratos;
- observabilidade e feedback.

A diferença entre as fases fica na interface e nas políticas de uso, não na duplicação da lógica funcional.

## Roadmap priorizado

1. Apoio ao agente de suporte
2. Resposta sugerida com contexto e KB
3. Classificação confiável de categoria/urgência
4. Observabilidade e feedback
5. Autoatendimento via API para portal GLPI

## Critérios de sucesso

- tickets atendidos mais rapidamente;
- melhor consistência na classificação;
- uso efetivo da base de conhecimento;
- aprovação humana em ações críticas;
- qualidade e rastreabilidade monitoradas;
- transição para Fase 2 sem reescrever o núcleo.

## Decisão principal

A prioridade estratégica é entregar valor real na Fase 1 e usar a mesma base técnica para a Fase 2, em vez de criar uma solução paralela ou duplicada.

## Próximo passo

Executar a primeira feature em SDDP (E001) e, em seguida, avançar nas ondas do núcleo da Fase 1 antes da expansão para o portal do cliente.
