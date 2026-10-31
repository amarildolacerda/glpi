# Documentação — Assistente de IA para GLPI

Este diretório concentra toda a documentação do projeto: especificações de negócio e técnicas, arquitetura, planos de execução, backlog e checklists. As duas fontes de verdade são [docs/spec](spec/README.md) — o quê e o porquê: requisitos, contratos, arquitetura e guardrails — e [docs/plan](plan/README.md) — o como e o quando: sequência, riscos, critérios e acompanhamento. Nenhum requisito, decisão ou plano pode ser duplicado fora desses dois diretórios: este arquivo é apenas o índice da documentação.

## Modelo de desenvolvimento

Todo incremento do projeto segue a sequência obrigatória definida em [AGENTS.md](../AGENTS.md):

especificação → planejamento → implementação → validação → revisão de prontidão

Regras que governam essa sequência:

1. **Precedência SP1 → SP11.** A execução segue a ordem das especificações por precedência, sem pular etapas. A ordem e as dependências entre etapas estão definidas em [Especificações por precedência — SP1 a SP11](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md) e a regra de precedência também consta em [docs/plan/README.md](plan/README.md) e em [docs/spec/README.md](spec/README.md).
2. **Plano aprovado antes de escrever código.** Não se inicia implementação sem uma especificação válida em [docs/spec](spec/README.md) e um plano de execução aprovado em [docs/plan](plan/README.md) correspondente à etapa atual.
3. **Portões de qualidade.** Antes de considerar uma mudança pronta para a próxima etapa, ela deve atender aos portões de qualidade e aos critérios de pronto descritos em [AGENTS.md](../AGENTS.md#gates-de-qualidade): alinhamento com a especificação de negócio e arquitetura, validação pelos testes relevantes, compatibilidade da API com os contratos, ausência de segredos ou credenciais hardcoded, consideração de guardrails, auditoria e rastreabilidade, preservação do núcleo compartilhado entre Fase 1 e Fase 2 e atualização da documentação relevante.

Cada etapa em execução recebe registro de status (TODO, EM ANDAMENTO ou DONE) no documento da respectiva SP, conforme descrito em [docs/spec/README.md](spec/README.md) e [docs/plan/README.md](plan/README.md).

## Mapa das etapas (SP1–SP11)

A coluna "Especificação" aponta para a seção da etapa no documento de precedência, que define objetivo, conteúdo mínimo, critérios de aceite e entregável de cada SP. A coluna "Plano de execução" é preenchida somente quando existe um plano de execução dedicado; as etapas sem plano dedicado devem ter seu plano criado e aprovado antes do início da implementação. O status de cada etapa é rastreado exclusivamente em [Especificações por precedência — SP1 a SP11](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md) — este índice não copia nem reflete valores de status.

| SP | Tema | Especificação | Plano de execução | Status |
|----|------|---------------|-------------------|--------|
| SP1 | Base de alinhamento e governança | [Especificação](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp1--base-de-alinhamento-e-govern%C3%A7a) | — | [Rastreador](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp1--base-de-alinhamento-e-govern%C3%A7a) |
| SP2 | Arquitetura e desenho do sistema | [Especificação](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp2--arquitetura-e-desenho-do-sistema) | — | [Rastreador](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp2--arquitetura-e-desenho-do-sistema) |
| SP3 | Contratos de API | [Especificação](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp3--contratos-de-api) | — | [Rastreador](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp3--contratos-de-api) |
| SP4 | Integração com GLPI | [Especificação](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp4--integra%C3%A7%C3%A3o-com-glpi) | — | [Rastreador](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp4--integra%C3%A7%C3%A3o-com-glpi) |
| SP5 | Base de conhecimento e RAG | [Especificação](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp5--base-de-conhecimento-e-rag) | — | [Rastreador](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp5--base-de-conhecimento-e-rag) |
| SP6 | IA e resposta sugerida | [Especificação](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp6--ia-e-resposta-sugerida) | [Plano de execução — SP6 IA e resposta sugerida](plan/Plano%20de%20execu%C3%A7%C3%A3o%20%E2%80%94%20SP6%20IA%20e%20resposta%20sugerida.md) | [Rastreador](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp6--ia-e-resposta-sugerida) |
| SP7 | Guardrails e segurança | [Especificação](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp7--guardrails-e-seguran%C3%A7a) | [Plano de execução — SP7 Guardrails e segurança](plan/Plano%20de%20execu%C3%A7%C3%A3o%20%E2%80%94%20SP7%20Guardrails%20e%20seguran%C3%A7a.md) | [Rastreador](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp7--guardrails-e-seguran%C3%A7a) |
| SP8 | Observabilidade e feedback | [Especificação](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp8--observabilidade-e-feedback) | [Plano de execução — SP8 Observabilidade e feedback](plan/Plano%20de%20execu%C3%A7%C3%A3o%20%E2%80%94%20SP8%20Observabilidade%20e%20feedback.md) | [Rastreador](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp8--observabilidade-e-feedback) |
| SP9 | Testes e garantia de qualidade | [Especificação](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp9--testes-e-garantia-de-qualidade) | — | [Rastreador](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp9--testes-e-garantia-de-qualidade) |
| SP10 | MVP da Fase 1 | [Especificação](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp10--mvp-da-fase-1) | — | [Rastreador](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp10--mvp-da-fase-1) |
| SP11 | Evolução para Fase 2 | [Especificação](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp11--evolu%C3%A7%C3%A3o-para-fase-2) | [Plano de execução — SP11 Evolução para Fase 2](plan/Plano%20de%20execu%C3%A7%C3%A3o%20%E2%80%94%20SP11%20Evolu%C3%A7%C3%A3o%20para%20Fase%202.md) | [Rastreador](spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md#sp11--evolu%C3%A7%C3%A3o-para-fase-2) |

### Documentos transversais de especificação

Além do documento de precedência, a base de especificação inclui documentos que apoiam todas as etapas:

- [Especificação Técnica — Assistente de IA](spec/Especifica%C3%A7%C3%A3o%20T%C3%A9cnica%20%E2%80%94%20Assistente%20de%20IA.md)
- [Arquitetura do Sistema — Assistente de IA para GLPI](spec/Arquitetura%20do%20Sistema%20%E2%80%94%20Assistente%20de%20IA%20para%20GLPI.md)
- [Documento Técnico — Funcionamento da Solução](spec/Documento%20T%C3%A9cnico%20%E2%80%94%20Funcionamento%20da%20Solu%C3%A7%C3%A3o.md)

## Estrutura

```text
docs/
├── README.md
├── spec/
│   ├── README.md
│   ├── Especificação Técnica — Assistente de IA.md
│   ├── Arquitetura do Sistema — Assistente de IA para GLPI.md
│   ├── Documento Técnico — Funcionamento da Solução.md
│   └── Especificações por precedência — SP1 a SP11.md
└── plan/
    ├── README.md
    ├── Backlog Inicial — MVP Fase 1.md
    ├── Checklist de Entregáveis — Assistente de IA para GLPI.md
    ├── Plano de execução — SP6 IA e resposta sugerida.md
    ├── Plano de execução — SP7 Guardrails e segurança.md
    ├── Plano de execução — SP8 Observabilidade e feedback.md
    └── Plano de execução — SP11 Evolução para Fase 2.md
```

## Como contribuir

- Nunca duplicar documentos fora de `docs/spec` e `docs/plan`: requisitos, decisões, contratos e planos só existem nas cópias canônicas desses diretórios.
- Editar sempre a cópia canônica em `spec/` ou `plan/`; outros arquivos (como este índice) apenas referenciam as fontes de verdade por link.
- Manter links relativos, no mesmo estilo do README raiz do repositório: espaços codificados como `%20` e caracteres não ASCII percent-encoded (por exemplo, o travessão `—` como `%E2%80%94`).
- Atualizar este índice ao adicionar ou remover documentos em `docs/spec` ou `docs/plan`, mantendo a árvore da seção "Estrutura" e o mapa das etapas consistentes com os arquivos reais.
- Seguir as regras de desenvolvimento, fluxo de trabalho e portões de qualidade descritos em [AGENTS.md](../AGENTS.md), inclusive a exigência de plano aprovado antes de qualquer escrita de código.
