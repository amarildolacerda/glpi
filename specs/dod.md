---
document_type: deployment-operations
status: pending
created: 2026-10-30
updated: 2026-10-30
---

# Deployment & Operations — Assistente de IA para Suporte GLPI

> **Pendente.** Este documento será criado pelo workflow `deployment-operations` quando a operação de deploy estiver definida.

Conteúdo mínimo planejado (conforme `.github/sddp/workflows/deployment-operations/`):

- topologia de deployment atual: Docker / docker-compose (porta 8000, uvicorn, `--reload` em dev) — ver `specs/sad.md` (Deployment and Trust Topology);
- gestão de configuração e segredos (`.env_default` como referência; `.env` local);
- procedimentos de release (branch `dev` → `main` com autorização; versionamento `vx.x.x`);
- observabilidade operacional e rollback.
