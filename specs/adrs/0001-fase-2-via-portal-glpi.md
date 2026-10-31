# ADR-0001: Fase 2 via portal GLPI consumindo API própria (sem UI própria)

Status: accepted

Data: 2026-10-30

## Contexto

A Fase 2 do projeto prevê atendimento automatizado direto ao cliente (autoatendimento). O checklist de entregáveis lista uma "interface para atendimento direto ao cliente", mas o projeto não possui frontend próprio e o cliente já usa o portal GLPI como canal oficial de suporte. Criar uma UI nova duplicaria canais, fragmentaria o atendimento e ampliaria o superfície de segurança.

## Decisão

A Fase 2 será exposta exclusivamente como API (`/v2/atender` e derivados), consumida pelo portal GLPI existente. O projeto não desenvolverá interface gráfica própria para o cliente final.

## Consequências

- O portal GLPI passa a ser o único canal da Fase 2; o assistente opera como serviço interno de API.
- Contratos de API da v2 precisam ser estáveis e versionados (consumidor externo).
- Redução de escopo: sem work de frontend/design no projeto.
- UX do autoatendimento fica a cargo do portal GLPI, fora deste repositório.
