# compact.md — contexto compactado da sessão

> Atualizado em 30/10/2026 para restauração de contexto. Repo `/mnt/c/git/glpi`, branch `dev`.
> Timestamps de status: `[DD/MM HH:MM]`. **Consultar este arquivo antes de iniciar uma nova sessão.**
> Regra: após cada etapa/fase concluída, regerar este compacto (substituir o conteúdo, mantendo a estrutura).

## Objetivo

- Migração completa do projeto para o framework **SDDP** (transplantado de `../inhome`, ADR-0002), substituindo o modelo SP1–SP11 centrado em `docs/spec` + `docs/plan` — **CONCLUÍDA** (aguardando commit).
- Fontes de verdade: `specs/prd.md`, `specs/sad.md`, `specs/project-plan.md`, `specs/dod.md` (stub pendente), `specs/adrs/`, `specs/NNNNN-slug/` (nenhuma feature ainda).
- Fase 2 = **API-only para o portal GLPI** (ADR-0001, sem UI própria); execução via épicos E001–E008 em `specs/project-plan.md` (Wave 1 núcleo, Wave 2 Fase 2, Wave 3 gate).
- Nada em produção; tudo em `dev`; promoção a `main` exige autorização explícita.

## Estado do repositório [30/10]

- Commit atual em `dev`: `c71c23c` (redesenho docs antigos, status SP1–SP4, SP1 fechamento, versão centralizada, `.pyc` removidos).
- **Working tree pendente de commit (todo o pacote SDDP)**: `.github/sddp/` (31), `.github/skills/` (23), `.github/instructions/` (4), `.github/sddp-config.md`, `.opencode/agents/sddp-*.md` (38), `opencode.json` (allowlist de task), `specs/` (prd ~20KB, sad 350L, project-plan 8 épicos, adrs/0001+0002, dod stub), `AGENTS.MD` reescrita SDDP (161L, regra de compacto incluída), `requirements.txt` (+python-dotenv), `TODO.md` (vocabulário SDDP), `compact.md` (este arquivo), `docs/README.md` (ponteiro de legado), `README.md` (links → specs/), `docs/legacy/{spec,plan}` (movidos via git mv, renomeações rastreadas).
- Validação do pacote: link checker próprio — **76 links, 0 quebrados** (incl. proveniência do prd/project-plan atualizada para `../docs/legacy/`); pytest **12 passed**; Docker `:8000` `/health` 200, `/docs` 200, `/` 404 esperado.

## Convenções e decisões ativas

- **ADR-0001**: Fase 2 só via API (`/v2/atender`) consumida pelo portal GLPI; sem frontend neste projeto.
- **ADR-0002**: SDDP substitui SP1–SP11; docs antigos = `docs/legacy/` (histórico, não editar).
- Pipeline por feature: Specify → Clarify → Plan → Checklist → Tasks → Analyze → Implement+QC; auto-piloto `sddp-autopilot-pipeline`; agentes `sddp-*` via `task` (allowlist no `opencode.json`).
- Regras não negociáveis preservadas na `AGENTS.MD`: branch `dev`, promoção com autorização, `.env` fora/`.env_default` atualizado, `vx.x.x` centralizado, guardrails+aprovação humana, idempotência+auditoria, evidência objetiva por gate.
- **Compacto de sessão**: regerar `compact.md` após cada etapa; consultar antes de nova sessão (seção própria na AGENTS.MD).
- Identidade git local: Amarildo de Lacerda <amarildo_51@msn.com>. Commits em PT curto com prefixo `+`.

## Pendências conhecidas

1. **Commit do pacote SDDP em `dev`** (aguardando autorização do usuário) — depois `git push` (também com autorização).
2. **Restart do opencode** para carregar 38 agentes `sddp-*` + 14 skills (config é carregada na inicialização).
3. Primeira feature: `specs/00001-contratos-de-erro/` via pipeline (epic E001; insumo: plano legado `docs/legacy/plan/Plano de execução — SP3 Contratos de API.md`).
4. Épicos E002–E008 conforme `specs/project-plan.md`.
5. `specs/dod.md` — stub criado; conteúdo real pendente de definição de deploy.
6. Agente `explorer` com modelo quebrado (`opencode/nemotron-3-ultra-free`) — falha ao despachar; usar fixer/oracle ou bash direto; corrigir no config global.
7. SP5–SP11 ficaram com status "DONE" não validado no rastreador legado — histórico, sem ação (o status agora vive nos artefatos de feature).

## Sessões reutilizáveis e regras de lane

- `ora-1`/`ses_e705a1a52ffeYDxD1QTgnt3ukY` (oracle — prontidão + checagem SP1–SP4).
- `fix-1`/`ses_e705173deffedKetLzo5QIOq0v` (fixer — docs/SDDP, prd+project-plan).
- `fix-2`/`ses_e702ce8dbffebiW0Ea0NUkBUb7` (fixer — bootstrap sad, templates SDDP).
- `fix-3`/`ses_e70264e26ffeOErguSZIkt3QfA` (fixer — AGENTS.MD SDDP).
- `exp-1`, `exp-2` retained (sem resultado) — explorers não reutilizar até corrigir modelo.
- Regras: `task()` exige `subagent_type` + `task_id`; completed+unreconciled → `task_result` primeiro; spawn dentro de lane proibido (profundidade 1); escopos de escrita disjuntos entre lanes paralelas; bash do orquestrador para verificação (pytest, git, link checker).
- Venvs: `/tmp/opencode/glpi-venv` (trabalho) e `/tmp/opencode/glpi-clean` (validação de ambiente limpo); sistema tem pip bloqueado por PEP 668.
