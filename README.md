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

## Documentação disponível

Para informações detalhadas sobre requisitos, arquitetura, implementação e processo, consulte:

- [Especificação Técnica — Assistente de IA](docs/Especificação%20T%C3%A9cnica%20%E2%80%94%20Assistente%20de%20IA)
- [Arquitetura do Sistema — Assistente de IA para GLPI](docs/Arquitetura%20do%20Sistema%20%E2%80%94%20Assistente%20de%20IA%20para%20GLPI.md)
- [Documento Técnico — Funcionamento da Solução](docs/Documento%20T%C3%A9cnico%20%E2%80%94%20Funcionamento%20da%20Solu%C3%A7%C3%A3o.md)
- [Checklist de Entregáveis — Assistente de IA para GLPI](docs/Checklist%20de%20Entreg%C3%A1veis%20%E2%80%94%20Assistente%20de%20IA%20para%20GLPI.md)
- [Backlog Inicial — MVP Fase 1](docs/Backlog%20Inicial%20%E2%80%94%20MVP%20Fase%201.md)
- [AGENTS.md](AGENTS.md)

## Observações importantes

- Este projeto não tem como objetivo substituir agentes humanos.
- Não deve haver alteração do core do GLPI ou do banco de dados do sistema.
- A implementação deve preservar segurança, auditoria e rastreabilidade das interações.
- A fase 2 deve reutilizar o mesmo núcleo da fase 1, sem duplicação estrutural.

## Objetivo de longo prazo

Construir um assistente de suporte inteligente, seguro e extensível, capaz de acelerar o atendimento em GLPI e preparar a organização para um modelo de suporte mais escalável e automatizado no futuro.
