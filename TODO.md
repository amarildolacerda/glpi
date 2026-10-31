# TODO

Este arquivo registra pendências, ajustes e solicitações de implementação. Antes de iniciar qualquer alteração no código, consulte este documento — junto com [compact.md](compact.md) — para verificar se há itens novos ou pendentes. O trabalho estruturado vive em [specs/project-plan.md](specs/project-plan.md) (épicos E001–E008, ondas e dependências).

## Pendentes

- [ ] **Commit do pacote SDDP** em `dev`: framework transplantado, specs/ (prd, sad, project-plan, adrs), AGENTS.MD reescrita, arquivamento de docs/, requirements.txt, compact.md. (Aguarda autorização de commit.)
- [ ] **Reiniciar o opencode** para carregar os 38 agentes `sddp-*` e 14 skills transplantados (config carregada na inicialização).
- [ ] `specs/dod.md` (deployment & operations) — criar quando a operação de deploy estiver definida.
- [ ] **Primeira feature SDDP**: criar `specs/00001-contratos-de-erro/` e rodar o pipeline (Fatia A / epic E001 — contratos de erro; insumo: plano legado em `docs/legacy/plan/Plano de execução — SP3 Contratos de API.md`).
- [ ] Epics E002–E008 conforme [specs/project-plan.md](specs/project-plan.md) (núcleo → Fase 2 API-only → gate).
- [ ] `git push` do branch `dev` para `origin` (requer autorização).
- [ ] Agente `explorer` está com modelo de config quebrado (`opencode/nemotron-3-ultra-free` inexistente) — corrigir no config global antes de usar lanes explorer.

## Concluídos

- [x] Redesenho de docs/spec+plan (duplicatas removidas, índice, links) e status SP1–SP4 — commit `c71c23c`.
- [x] Fechamento SP1: aprovação dos docs base, versão centralizada, `.pyc` removidos, `python-dotenv` no requirements.
- [x] Adoção do SDDP (ADR-0002): framework transplantado de `../inhome`, bootstrap de `specs/prd.md`, `specs/sad.md`, `specs/project-plan.md`, ADR-0001/0002, reescrita da AGENTS.MD, `opencode.json`, legado arquivado em `docs/legacy/`.
- [x] Fase 2 definida como API-only para o portal GLPI (ADR-0001).
- [x] Skill global `sdd` atualizada para o modelo SDDP.
- [x] Rotina de `compact.md` instituída (regerar a cada etapa; consultar antes de nova sessão).
- [x] Definir regra de consulta ao TODO antes das alterações de código.
- [x] Criar script de instalação rápido em `install.sh` para ambiente local ou Docker e incluir referência no README.
