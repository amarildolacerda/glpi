# AGENTS.md

## Visão geral

Este repositório tem como objetivo implantar um assistente de IA para suporte no GLPI. O desenvolvimento segue o framework SDDP (Spec-Driven Development Pipeline), transplantado de `../inhome` conforme [ADR-0002](specs/adrs/0002-adocao-framework-sddp.md), com artefatos canônicos em [specs/](specs/).

A prioridade inicial é a Fase 1: apoio ao agente humano. A Fase 2 (autoatendimento do cliente) deve ser pensada como evolução do mesmo núcleo, não como reescrita do projeto — conforme [ADR-0001](specs/adrs/0001-fase-2-via-portal-glpi.md), a Fase 2 será uma API-only para o portal do GLPI.

## Fonte de verdade

- [specs/prd.md](specs/prd.md) — requisitos do produto.
- [specs/sad.md](specs/sad.md) — arquitetura e decisões de design.
- [specs/project-plan.md](specs/project-plan.md) — plano de execução (epics, dependências e ondas).
- [specs/dod.md](specs/dod.md) — definição de pronto (pendente).
- [specs/NNNNN-slug/](specs) — artefatos de cada feature (spec.md, plan.md e derivados).
- Configuração do framework em [.github/sddp-config.md](.github/sddp-config.md).
- [docs/legacy/spec](docs/legacy/spec) e [docs/legacy/plan](docs/legacy/plan) são **legados migrados para `specs/`** (referência histórica apenas).
- Qualquer mudança de arquitetura, requisitos ou API deve ser alinhada com os artefatos SDDP antes de ser implementada.
- Antes de qualquer escrita de código, é obrigatório existir spec e plano aprovados da feature no formato SDDP, com os gates do pipeline atendidos.
- A implementação deve respeitar as metas de negócio e os guardrails de segurança listados nos artefatos canônicos.

## Objetivo do projeto

- Reduzir o tempo de primeira resposta do suporte.
- Aumentar a acurácia na classificação de categoria e urgência.
- Reaproveitar a base de conhecimento do GLPI por meio de RAG.
- Preparar a base para atendimento automatizado em uma segunda fase, sem substituir a supervisão humana.

## Regras de implementação

1. Não alterar o núcleo do GLPI ou seu banco de dados.
2. Manter o núcleo compartilhado entre Fase 1 e Fase 2.
3. Separar claramente as camadas de interface, orquestração, RAG, LLM, guardrails, integração com GLPI e schemas.
4. Priorizar a Fase 1 antes de expandir para a Fase 2.
5. Tratar a política de guardrails como parte central da arquitetura, não como camada opcional.
6. Nunca expor segredos no repositório: usar variáveis de ambiente e secret manager.
7. O arquivo `.env_default` deve funcionar como referência de configuração para novos ambientes e deve ser atualizado sempre que uma nova variável ou ajuste de configuração for necessário para dar suporte a um ambiente novo ou a uma mudança de infraestrutura.
8. O arquivo `.env` é local e não deve entrar no branch; qualquer segredo real deve permanecer fora do repositório.
9. Registrar interações e feedback para métricas e melhoria contínua.
10. Garantir idempotência na criação de tickets e auditoria completa das ações.
11. Todo desenvolvimento de código deve ocorrer no branch `dev`.
12. A promoção para `main` só deve ocorrer com autorização explícita e prévia.
13. Qualquer alteração em produção deve ser feita por merge ou release previamente aprovado, nunca diretamente em `main`.

## Fluxo SDDP

O fluxo de uma feature segue a sequência do pipeline SDDP, implementada nos workflows de [.github/sddp/workflows/](.github/sddp/workflows/) e executável de forma integrada pelo auto-piloto `sddp-autopilot-pipeline`:

1. **Specify** — criar/refinar a especificação da feature em `specs/NNNNN-slug/spec.md`.
2. **Clarify** — esclarecer ambiguidades e consolidar requisitos.
3. **Plan** — gerar `specs/NNNNN-slug/plan.md` com arquitetura, passos e riscos.
4. **Checklist** — gerar/verificar o checklist de qualidade da feature.
5. **Tasks** — decompor o plano em tarefas rastreáveis.
6. **Analyze** — validar consistência, riscos e compliance antes da implementação.
7. **Implement + QC** — implementar as tarefas com loop de quality control e evidência objetiva.

Regras do fluxo:

- Usar os agentes `sddp-*` (lista em [.opencode/agents/](.opencode/agents/)) por meio da ferramenta `task`, as skills em [.github/skills/](.github/skills/) e as instruções em [.github/instructions/](.github/instructions/).
- Nenhuma implementação sem spec + plano aprovados no formato SDDP (`spec.md` e `plan.md` da feature), com os gates do pipeline atendidos.
- Não avançar para a próxima etapa sem evidência de que a etapa anterior foi validada.
- As respostas sugeridas devem sempre incluir nível de confiança e exigir aprovação humana antes da criação de ticket.
- Implementar em pequenos incrementos, validando um requisito por vez; preferir testes antes da lógica de negócio sempre que possível.
- Manter APIs e modelos consistentes com os contratos descritos nos artefatos canônicos.
- Evoluções futuras devem reutilizar o mesmo núcleo e não duplicar lógica entre Fase 1 e Fase 2.
- O projeto deve seguir uma abordagem de segurança e observabilidade desde o início.

## Arquitetura esperada

- Núcleo compartilhado:
  - orchestrator
  - rag
  - llm adapter
  - guardrails
  - glpi client
  - schemas
- Interfaces:
  - fase 1: apoio ao agente
  - fase 2: portal/cliente (API-only, futuro — ADR-0001)
- Serviços de apoio:
  - feedback logger
  - métricas
  - configurações e prompts
- Stack e padrões recomendados: Python 3.11+, FastAPI para interfaces HTTP, Pydantic para validação de payloads, pytest para testes automatizados, integração com GLPI via wrapper único (`glpi-utils` / cliente dedicado), suporte a LLM local como requisito da Fase 1 com provedor trocável por configuração. Se a tecnologia exata de um componente ainda não estiver definida, a decisão deve preservar baixo acoplamento, modelagem orientada a contratos e compatibilidade com GLPI.

## Gates de qualidade

Antes de considerar uma mudança pronta para seguir para a próxima etapa, ela deve atender aos critérios abaixo:

- a alteração está alinhada com o prd, a arquitetura (sad) e o plano da feature;
- a implementação foi validada pelos testes relevantes, com evidência objetiva (comando executado + resultado);
- a API continua compatível com os contratos esperados;
- não houve exposição de segredos ou credenciais hardcoded;
- guardrails, auditoria e rastreabilidade foram considerados;
- a mudança não compromete o núcleo compartilhado entre Fase 1 e Fase 2;
- a documentação relevante (specs/, .env_default, docs afetados) foi atualizada quando necessário.

## Critérios de pronto

Um incremento só deve ser considerado concluído quando:

- o comportamento foi validado contra a spec da feature (spec.md) e contra os requisitos (prd.md);
- os testes relevantes passam, com evidência objetiva registrada (comando executado + resultado observado);
- a API segue o contrato estabelecido;
- não há credenciais hardcoded;
- os guardrails e auditoria foram considerados;
- a solução continua compatível com o modelo de suporte do GLPI;
- a mudança foi revisada em relação ao impacto de manutenção e evolução futura;
- a documentação relevante foi atualizada.

## Evidência de validação

Toda alteração deve ser acompanhada de evidência objetiva, como:

- comando de teste executado;
- resultado observado;
- análise do impacto em API, arquitetura ou segurança;
- registro de qualquer restrição ou dependência não resolvida.

Não se deve assumir que o comportamento está correto apenas porque a mudança foi implementada.

## Versionamento da implementação

- A versão da implementação deve ser centralizada e rastreável em um único ponto do projeto.
- O padrão de versionamento deve seguir o formato `vx.x.x`.
- A versão deve ser incrementada sempre que houver promoção para produção.
- A promoção para produção deve ser acompanhada da atualização explícita da versão correspondente.
- Mudanças em desenvolvimento podem ocorrer sem promoção, mas a mudança de versão só deve acontecer no momento da liberação para produção.

## Estrutura de diretórios esperada

- `specs/` (prd.md, sad.md, project-plan.md, dod.md, adrs/, NNNNN-slug/)
- `.github/` (sddp/workflows/, skills/, instructions/, sddp-config.md)
- `.opencode/agents/` (agentes `sddp-*`)
- `core/`
- `interfaces/`
- `feedback/`
- `config/`
- `tests/`
- `scripts/`
- `main.py`

## Compacto de sessão

- Após **cada etapa/fase concluída** (pipeline, fatia, commit ou milestone), regerar o arquivo [compact.md](compact.md) na raiz: substituir seu conteúdo mantendo a estrutura (Objetivo, Estado do repositório com timestamp, Bateria/evidência, Convenções e decisões ativas, Pendências conhecidas, Sessões reutilizáveis e regras de lane).
- **Antes de iniciar uma nova sessão de trabalho**, consultar `compact.md` para restaurar contexto (estado atual, pendências, decisões ativas, lanes reutilizáveis) — não depender de memória da sessão anterior.
- O `compact.md` é o handoff canônico entre sessões; não arquivá-lo nem removê-lo.

## Instrução para agentes

Antes de propor ou aplicar mudanças, leia os artefatos canônicos em [specs/](specs/) (prd.md, sad.md, project-plan.md e, quando existir, a spec e o plano da feature em `specs/NNNNN-slug/`) e mantenha a implementação alinhada ao escopo do projeto. [docs/legacy/spec](docs/legacy/spec) e [docs/legacy/plan](docs/legacy/plan) são referência histórica apenas.

Antes de iniciar qualquer alteração, consulte [TODO.md](TODO.md) para verificar se há novas solicitações de implementação, ajustes ou pendências relevantes; registre novas pendências nesse arquivo.
A prioridade é entregar uma base sólida para a Fase 1, sem perder o desenho de arquitetura que permitirá a extensão futura para a Fase 2.

Além disso:

- todas as alterações de código devem ocorrer no branch `dev`;
- o arquivo `.env` não entra no branch e deve conter apenas valores locais/secretos;
- o arquivo `.env_default` deve ser mantido atualizado sempre que uma nova variável ou ajuste de configuração exigir replicação em outro ambiente;
- a promoção para `main` exige autorização explícita e prévia;
- qualquer alteração em produção deve ocorrer por merge ou release aprovado, nunca diretamente em `main`;
- o framework SDDP foi transplantado de `../inhome` (ADR-0002); qualquer evolução do processo de desenvolvimento deve considerar esse provenance.

---

Este arquivo deve ser atualizado conforme o projeto evolui, especialmente quando houver decisões de stack, padrões de código, fluxos de deploy, integração com GLPI e evolução do processo de desenvolvimento (SDDP).
