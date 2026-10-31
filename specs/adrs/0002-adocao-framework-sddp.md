# ADR-0002: Adoção do framework SDDP, substituindo o modelo SP1–SP11

Status: accepted

Data: 2026-10-30

## Contexto

O projeto operava com um modelo próprio de desenvolvimento guiado por especificação: etapas SP1–SP11 rastreadas em `docs/spec/Especificações por precedência — SP1 a SP11.md`, planos em `docs/plan/` e regras em `AGENTS.MD`. O modelo funcionou como base, mas os statuses divergiam da realidade do código, faltavam planos para várias etapas e o processo dependia de disciplina manual. O projeto vizinho `../inhome` opera o framework SDDP (Spec-Driven Development Pipeline) com auto-piloto, que formaliza o mesmo princípio com artefatos canônicos, gates por fase e QC automatizado.

## Decisão

Adotar o framework SDDP transplantado de `../inhome` (workflows em `.github/sddp/`, skills em `.github/skills/`, agentes `sddp-*` em `.opencode/agents/`, config em `.github/sddp-config.md`), substituindo o modelo SP1–SP11. Fontes de verdade passam a ser `specs/prd.md`, `specs/sad.md`, `specs/project-plan.md`, `specs/dod.md` (pendente) e pastas de feature `specs/NNNNN-slug/`. Os documentos de `docs/spec/` e `docs/plan/` são migrados para os artefatos canônicos e mantidos como referência histórica.

## Consequências

- Toda implementação nova segue o pipeline Specify → Clarify → Plan → Checklist → Tasks → Analyze → Implement+QC, com gates e evidência por fase.
- A `AGENTS.MD` é reescrita para o fluxo SDDP, preservando as regras não negociáveis (segurança, branch `dev`, versionamento, guardrails, auditoria).
- O rastreador manual de SP deixa de ser fonte de status; o status vive nos artefatos de feature.
- Requer restart do opencode para carregar os 38 agentes e 14 skills transplantados.
