# Plano de execução — SP7 Guardrails e segurança

Versão: 1.0
Status: DONE
Última atualização: 31/10/2026

---

## Objetivo

Implementar a camada de guardrails para validar a ação do assistente, reduzir risco operacional e garantir que respostas sensíveis ou fora de escopo não avancem sem revisão humana.

## Requisito da SP7

A SP7 corresponde à etapa de guardrails e segurança da sequência de precedência. A implementação deve respeitar:

- validação de conteúdo e risco antes da resposta;
- exigência de aprovação humana para ações críticas;
- tratamento de dados sensíveis e informações de acesso;
- regras de perfil e escalonamento para atendimento humano;
- rastreabilidade das decisões de segurança.

## Escopo do incremento

1. definir regras básicas de validação para respostas e ações;
2. bloquear ou sinalizar conteúdo sensível quando necessário;
3. garantir que a Fase 1 exija aprovação humana antes de criar ticket;
4. adicionar camada de decisão no orquestrador;
5. validar com teste automatizado.

## Critérios de aceite

- a resposta do sistema é validada antes de seguir para o agente ou para a criação de ticket;
- dados sensíveis são detectados e tratados de forma segura;
- ações críticas exigem confirmação humana;
- a regra de guardrails fica integrada ao núcleo sem acoplamento com a interface;
- o teste relevante passa.

## Riscos

- excesso de permissividade na resposta;
- uso indevido de dados sensíveis;
- criação de ticket sem supervisão humana;
- regras de segurança inconsistentes entre módulos.

## Sequência de execução

1. definir o contrato de validação do guardrail;
2. criar teste para risco e regra de aprovação;
3. implementar a camada de guardrails;
4. integrar a validação ao orquestrador;
5. validar com pytest e ajustar se necessário.

## Status atual

- SP5: DONE
- SP6: DONE
- SP7: EM ANDAMENTO
- SP9: DONE
- SP10: DONE

A implementação só avança se a validação de segurança estiver documentada, testada e integrada ao núcleo.
