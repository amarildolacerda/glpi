# Plano de execução — SP11 Evolução para Fase 2

## Status
DONE

## Objetivo
Preparar a evolução do mesmo núcleo para atendimento direto ao cliente, preservando a arquitetura compartilhada da Fase 1.

## Escopo
- reutilizar o mesmo núcleo de orquestração, RAG, LLM e guardrails;
- expor uma interface de cliente para atendimento automatizado;
- definir limiar de autoatendimento seguro;
- escalar automaticamente para atendimento humano quando o contexto não é suficiente;
- manter políticas. de segurança e rastreabilidade consistentes com a Fase 1.

## Riscos
- duplicação de lógica entre Fase 1 e Fase 2;
- automação excessiva sem revisão humana;
- perda de rastreabilidade e auditoria no fluxo direto ao cliente.

## Sequência de execução
1. confirmar que o núcleo compartilhado é reutilizável;
2. criar uma interface de cliente leve e segura para o fluxo de atendimento direto;
3. validar o uso do mesmo orquestrador e guardrails;
4. definir critérios de escalonamento para revisão humana;
5. validar o fluxo com testes automatizados.

## Critérios de aceite
- a Fase 2 reutiliza as camadas centrais sem duplicação estrutural;
- a interface muda, mas a inteligência e os guardrails continuam compartilhados;
- o fluxo mantém a segurança e a rastreabilidade;
- a evolução não compromete a Fase 1.

## Resultado esperado
Base funcional para a Fase 2, construída sobre o mesmo núcleo, com guardrails e rastreabilidade preservados.
