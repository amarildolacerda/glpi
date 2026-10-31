# TODO

Este arquivo registra pendências, ajustes e solicitações de implementação. Antes de iniciar qualquer alteração no código, consulte este documento — junto com [compact.md](compact.md) — para verificar se há itens novos ou pendentes. O trabalho estruturado vive em [specs/project-plan.md](specs/project-plan.md) (épicos E001–E008, ondas e dependências).

## Pendentes

### Sequência executiva recomendada (próxima onda de trabalho)
1. **Pesquisar e consolidar requisitos de suporte** — compreender dores, feedbacks e desejos de suporte, agentes e administradores; gerar uma base objetiva para priorizar a Fase 1 e a interface do atendente.
2. **Definir a visão de produto das fases** — fechar a arquitetura de entrega: infraestrutura + API, dashboard do atendente, interface do cliente final, e decisão entre solução separada versus plugin no GLPI.
3. **Fechar a feature E001 em SDDP** — criar `specs/00001-contratos-de-erro/` e rodar o pipeline lean `spec -> plan -> implement -> QC -> commit` para o epic E001.
4. **Implementar o núcleo da Fase 1** — seguir com E002–E005 (GLPI real, LLM real, guardrails e observabilidade), validando cada epic contra o plano e os testes relevantes.
5. **Preparar a transição para a Fase 2** — E006–E008 (contrato `/v2/atender`, escalonamento e gate de prontidão), com evidência e aprovação antes de avançar.
6. **Encaminhar operação e release** — concluir `specs/dod.md`, validar commit do pacote SDDP, reiniciar o OpenCode e, somente com autorização, fazer o `git push` para `origin`.

- fazer uma pesquisa sobre o tema "suporte de software" e registros de tickets para obter pontos relevantes, tipo de feedback e desejos de usuario de suporte e administradores de equipes de suporte;
- redefinir as fases: fase1: construção de infra-estrutura (ex: api) com acesso manual sem interface; fase1: construção de uma interface web de uso do atendente do suporte (dashboard, questões mais usadas; qtde de atendimentos do dia; login;) - (a pagina tem header, drawer a esquerda, pagina principal, footter de estatus; fase3 - interface para usuario final (o cliente); avaliar se é melhor uma solução separada ou um plugin para o GPLI;

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
