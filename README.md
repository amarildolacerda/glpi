# GLPI AI Support

Assistente de IA para apoiar o atendimento em GLPI com foco em produtividade, qualidade da resposta e reutilização da base de conhecimento.

## Visão geral

Este projeto tem como objetivo reduzir o esforço manual de agentes de suporte, acelerar o atendimento e melhorar a consistência das respostas entregues aos usuários. A solução é pensada para operar em duas fases evolutivas:

- Fase 1: apoio ao agente humano durante o atendimento.
- Fase 2: autoatendimento do cliente, com escalonamento para atendimento humano quando necessário.

A proposta central é usar a mesma base arquitetural em ambas as fases, preservando o núcleo de orquestração, RAG, integrações e guardrails, enquanto a interface e as políticas variam conforme o perfil de usuário.

## Objetivos do projeto

- reduzir o tempo de primeira resposta;
- aumentar a acurácia na classificação de categoria e urgência;
- reutilizar artigos e conhecimento da base do GLPI;
- apoiar a criação de tickets com supervisão humana;
- preparar a base para um atendimento automatizado do cliente no futuro.

## Problema que resolve

O suporte no GLPI frequentemente lida com tickets repetitivos e com necessidade de resposta rápida, mas a equipe também precisa manter qualidade, segurança e rastreabilidade. O assistente proposto atua como apoio cognitivo: sugere respostas, identifica articulações relevantes da base de conhecimento, classifica o ticket e reduz a carga operacional sem substituir a decisão humana.

## Público-alvo

- agentes de suporte do GLPI;
- gestores de atendimento;
- equipes que desejam ampliar a automação com controle e segurança.

## Fase 1: assistência ao agente

Na primeira etapa, o assistente auxilia o agente no fluxo de atendimento com:

- sugestão de resposta;
- recomendação de categoria, urgência e impacto;
- indicação de artigos da base de conhecimento;
- identificação de tickets históricos similares;
- registro de feedback para melhoria contínua;
- criação de ticket somente após aprovação humana.

## Fase 2: autoatendimento do cliente

A segunda fase amplia o uso do mesmo núcleo para interação direta com o cliente, com regras mais rígidas de segurança e escalonamento automático. Em casos de baixa confiança ou risco, o sistema deve encaminhar o atendimento para um humano.

## Princípios de arquitetura

O projeto foi pensado para manter a separação clara entre:

- interfaces por perfil de usuário;
- orquestração da experiência;
- recuperação de conhecimento via RAG;
- adaptação ao modelo LLM;
- validações e guardrails;
- integração com GLPI.

Esse desenho facilita evolução, manutenção e testes sem misturar regras de negócio com detalhes operacionais de infraestrutura.

## Status do projeto

- Status: em estruturação inicial com base documental e arquitetural consolidadas
- Fase prioritária: Fase 1
- Base documental: especificação, arquitetura, documento técnico, checklist e backlog definidos
- Regra de governança: desenvolvimento em `dev`; promoção para `main` apenas com autorização prévia

## Instalação rápida

Para preparar o ambiente em modo local ou Docker, use o script de instalação:

```bash
bash install.sh --mode local
# ou
bash install.sh --mode docker
```

O script detecta o ambiente, prepara o venv/local ou inicia o compose, e pode ser usado em modo de validação com `--dry-run` para verificar o que seria executado.

## Documentação disponível

Para informações detalhadas sobre requisitos, arquitetura, implementação e processo, consulte:

### Especificação e arquitetura
- [specs/prd.md](specs/prd.md) — requisitos do produto
- [specs/sad.md](specs/sad.md) — arquitetura e decisões (ADRs em [specs/adrs/](specs/adrs/))
- Documentação legada migrada em [docs/legacy/spec](docs/legacy/spec) e [docs/legacy/plan](docs/legacy/plan) (referência histórica)

### Plano de execução
- [specs/project-plan.md](specs/project-plan.md) — ondas, épicos e dependências
- Planos legados do modelo SP1–SP11 em [docs/legacy/plan/](docs/legacy/plan)
- [AGENTS.MD](AGENTS.MD)

### Regra de processo

Antes de qualquer implementação de código, é obrigatório garantir que exista uma especificação válida ([specs/prd.md](specs/prd.md), [specs/sad.md](specs/sad.md)) e um plano de execução ([specs/project-plan.md](specs/project-plan.md) e a spec/plano da feature em `specs/NNNNN-slug/`). A execução só começa após essa revisão (fluxo SDDP — ver [AGENTS.md](AGENTS.md)).

## Observações importantes

- Este projeto não tem como objetivo substituir agentes humanos.
- Não deve haver alteração do core do GLPI ou do banco de dados do sistema.
- A implementação deve preservar segurança, auditoria e rastreabilidade das interações.
- A fase 2 deve reutilizar o mesmo núcleo da fase 1, sem duplicação estrutural.

## Objetivo de longo prazo

Construir um assistente de suporte inteligente, seguro e extensível, capaz de acelerar o atendimento em GLPI e preparar a organização para um modelo de suporte mais escalável e automatizado no futuro.
