# AGENTS.md

## Visão geral

Este repositório tem como objetivo implantar um assistente de IA para suporte no GLPI, seguindo a especificação técnica em [docs/Especificação Técnica — Assistente de IA](docs/Especificação%20T%C3%A9cnica%20%E2%80%94%20Assistente%20de%20IA).

A prioridade inicial é a Fase 1: apoio ao agente humano. A Fase 2 (autoatendimento do cliente) deve ser pensada como evolução do mesmo núcleo, não como reescrita do projeto.

## Fonte de verdade

- A especificação técnica no diretório [docs](docs) é a referência primária para escopo, requisitos e contratos.
- Qualquer mudança de arquitetura, requisitos ou API deve ser alinhada com essa documentação antes de ser implementada.
- A implementação deve respeitar as metas de negócio e os guardrails de segurança listados na especificação.

## Objetivo do projeto

- Reduzir o tempo de primeira resposta do suporte.
- Aumentar a acurácia na classificação de categoria e urgência.
- Reaproveitar a base de conhecimento do GLPI por meio de RAG.
- Preparar a base para atendimento automatizado em uma segunda fase, sem substituir a supervisão humana.

## Regras de implementação

1. Não alterar o núcleo do GLPI ou seu banco de dados.
2. Manter o núcleo compartilhado entre Fase 1 e Fase 2.
3. Separar claramente as camadas de interface, orquestração, RAG, LLM, guardrails e integração com GLPI.
4. Priorizar a Fase 1 antes de expandir para a Fase 2.
5. Tratar a política de guardrails como parte central da arquitetura, não como camada opcional.
6. Nunca expor segredos no repositório: usar variáveis de ambiente e secret manager.
7. Registrar interações e feedback para métricas e melhoria contínua.
8. Garantir idempotência na criação de tickets e auditoria completa das ações.
9. Todo desenvolvimento de código deve ocorrer no branch `dev`.
10. A promoção para `main` só deve ocorrer com autorização explícita e prévia.
11. Qualquer alteração em produção deve ser feita por merge ou release previamente aprovado, nunca diretamente em `main`.

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
  - fase 2: portal/cliente (futuro)
- Serviços de apoio:
  - feedback logger
  - métricas
  - configurações e prompts

## Stack e padrões recomendados

- Python 3.11+
- FastAPI para interfaces HTTP
- Pydantic para validação de payloads
- pytest para testes automatizados
- integração com GLPI via wrapper único (`glpi-utils` / cliente dedicado)
- suporte a LLM local como requisito da Fase 1, com provedor trocável por configuração

Se a tecnologia exata de cada componente ainda não estiver definida no momento, a decisão deve preservar os princípios da especificação: baixo acoplamento, modelagem orientada a contratos e compatibilidade com GLPI.

## Diretrizes para desenvolvimento

- Implementar em pequenas incrementos, validando um requisito por vez.
- Preferir testes antes da lógica de negócio sempre que possível.
- Manter APIs e modelos consistentes com os contratos descritos na especificação.
- As respostas sugeridas devem sempre incluir nível de confiança e devem exigir aprovação humana antes da criação de ticket.
- Evoluções futuras devem reutilizar o mesmo núcleo e não duplicar lógica entre Fase 1 e Fase 2.
- O projeto deve seguir uma abordagem de segurança e observabilidade desde o início.
- Todo incremento deve ser executado seguindo a sequência: especificação → planejamento → implementação → validação → revisão de prontidão.
- Não avançar para a próxima etapa sem evidência de que o requisito anterior foi validado.

## Fluxo de trabalho recomendado

1. Definir o objetivo e o escopo do incremento com base na especificação.
2. Validar se a mudança está alinhada ao modelo de arquitetura e aos guardrails do projeto.
3. Planejar a alteração em pequenos passos e manter a API/contratos consistentes.
4. Implementar a solução com testes focados no comportamento esperado.
5. Executar verificações relevantes antes de considerar a mudança pronta.
6. Só então realizar revisão final e promover para branch de integração.

## Gates de qualidade

Antes de considerar uma mudança pronta para seguir para a próxima etapa, ela deve atender aos critérios abaixo:

- a alteração está alinhada com a especificação de negócio e arquitetura;
- a implementação foi validada pelos testes relevantes;
- a API continua compatível com os contratos esperados;
- não houve exposição de segredos ou credenciais hardcoded;
- guardrails, auditoria e rastreabilidade foram considerados;
- a mudança não compromete o núcleo compartilhado entre Fase 1 e Fase 2;
- a documentação relevante foi atualizada quando necessário.

## Critérios de pronto

Um incremento só deve ser considerado concluído quando:

- o comportamento foi validado contra a especificação;
- os testes relevantes passam;
- a API segue o contrato estabelecido;
- não há credenciais hardcoded;
- os guardrails e auditoria foram considerados;
- a solução continua compatível com o modelo de suporte do GLPI;
- a mudança foi revisada em relação ao impacto de manutenção e evolução futura.

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

- `core/`
- `interfaces/`
- `feedback/`
- `config/`
- `tests/`
- `scripts/`
- `main.py`

## Instrução para agentes

Antes de propor ou aplicar mudanças, leia a especificação técnica em [docs/Especificação Técnica — Assistente de IA](docs/Especificação%20T%C3%A9cnica%20%E2%80%94%20Assistente%20de%20IA) e mantenha a implementação alinhada ao escopo do projeto.

A prioridade é entregar uma base sólida para a Fase 1, sem perder o desenho de arquitetura que permitirá a extensão futura para a Fase 2.

Além disso:

- todas as alterações de código devem ocorrer no branch `dev`;
- a promoção para `main` exige autorização explícita e prévia;
- qualquer alteração em produção deve ocorrer por merge ou release aprovado, nunca diretamente em `main`.

---

Este arquivo deve ser atualizado conforme o projeto evolui, especialmente quando houver decisões de stack, padrões de código, fluxos de deploy, integração com GLPI e evolução do processo de desenvolvimento.
