# Especificação

Esta pasta concentra a base de especificação do sistema: requisitos de negócio, arquitetura, contratos, guardrails e documentação técnica.

## Regra de trabalho

Antes de qualquer implementação de código, é obrigatório:

1. definir a especificação do incremento em uma visão clara de escopo e requisitos;
2. validar o alinhamento com a arquitetura e os guardrails do projeto;
3. confirmar o que será entregue e como será validado;
4. verificar a precedência da etapa atual e o plano de execução correspondente em [docs/plan/README.md](../plan/README.md);
5. registrar o status da SP em TODO, EM ANDAMENTO ou DONE durante a execução.

## Conteúdo principal

- Especificação técnica do assistente de IA para GLPI
- Arquitetura do sistema
- Documento técnico de funcionamento da solução
- Especificações por precedência SP1 a SP11

## Fonte de verdade

A documentação nesta pasta deve ser a referência primária para requisitos, APIs, arquitetura e decisões de produto/tecnologia.

## Sequência prioritária

A execução segue a ordem das SPs em precedência:

SP1 → SP2 → SP3 → SP4 → SP5 → SP6 → SP7 → SP8 → SP9 → SP10 → SP11

Cada SP deve ser acompanhada por status de execução:

- TODO
- EM ANDAMENTO
- DONE

## Plano de execução

O plano de trabalho e o acompanhamento do progresso devem ser registrados em [docs/plan/README.md](../plan/README.md).

A implementação do projeto deve seguir as especificações organizadas por precedência, em ordem:

1. SP1 — Base de alinhamento e governança
2. SP2 — Arquitetura e desenho do sistema
3. SP3 — Contratos de API
4. SP4 — Integração com GLPI
5. SP5 — Base de conhecimento e RAG
6. SP6 — IA e resposta sugerida
7. SP7 — Guardrails e segurança
8. SP8 — Observabilidade e feedback
9. SP9 — Testes e garantia de qualidade
10. SP10 — MVP da Fase 1
11. SP11 — Evolução para Fase 2

A documentação detalhada da sequência está em [Especificações por precedência — SP1 a SP11.md](Especificações%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md).
