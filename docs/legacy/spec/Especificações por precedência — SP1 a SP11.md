# Especificações por precedência — SP1 a SP11

Versão: 1.0
Status: Aprovada
Última atualização: 31/10/2026

---

## Objetivo

Este documento traduz o checklist de entregáveis em uma sequência de especificações priorizadas para o desenvolvimento do assistente de IA para GLPI. A ordem define a precedência de implementação e garante que cada incremento seja construído sobre uma base válida de escopo, arquitetura e validação.

A ordem de execução deve seguir a precedência abaixo, sem pular etapas:

### Regra de processo

- antes de começar a implementação, deve existir um plano de execução aprovado em [docs/plan](../plan);
- a etapa atual deve ser validada contra a SP correspondente antes de escrever código;
- durante a implementação, cada SP deve receber registro de status: TODO, EM ANDAMENTO ou DONE;
- a codificação só avança quando a etapa anterior estiver concluída e validada.

- SP1 Base de alinhamento e governança
- SP2 Arquitetura e desenho do sistema
- SP3 Contratos de API
- SP4 Integração com GLPI
- SP5 Base de conhecimento e RAG
- SP6 IA e resposta sugerida
- SP7 Guardrails e segurança
- SP8 Observabilidade e feedback
- SP9 Testes e garantia de qualidade
- SP10 MVP da Fase 1
- SP11 Evolução para Fase 2

---

## SP1 — Base de alinhamento e governança

Status: EM ANDAMENTO

### Objetivo
Estabelecer o escopo, os objetivos, as regras de processo e a base documental do projeto.

### Conteúdo mínimo
- definição clara do problema de negócio;
- objetivo do assistente de IA para GLPI;
- visão geral da Fase 1 e Fase 2;
- README do projeto com objetivos e público-alvo;
- AGENTS.md com regras de processo, branch e política de promoção;
- documentação técnica e de arquitetura aprovadas;
- alinhamento com a política de segurança e dados sensíveis.

### Critérios de aceite
- o problema e o objetivo estão explícitos;
- a governança do projeto e o fluxo de desenvolvimento estão documentados;
- a documentação é consistente com a arquitetura esperada;
- o projeto não permite execução sem a base documental mínima.

### Entregável
Documento base do projeto com visão, objetivos, regras e alinhamento do escopo.

---

## SP2 — Arquitetura e desenho do sistema

Status: DONE

### Objetivo
Definir o desenho estrutural do sistema e a separação entre as camadas de negócio, interface, integração e apoio.

### Conteúdo mínimo
- núcleo compartilhado entre Fase 1 e Fase 2;
- separação entre interface, orchestrator, RAG, LLM adapter, guardrails e GLPI client;
- definição de responsabilidades por camada;
- fluxo funcional da Fase 1;
- evolução da Fase 2 como reaproveitamento do mesmo núcleo;
- objetivos de segurança, rastreabilidade e observabilidade.

### Critérios de aceite
- as responsabilidades de cada camada estão claras;
- o núcleo compartilhado é independente da interface de usuário;
- a arquitetura preserva compatibilidade com o GLPI e a política de guardrails;
- a estrutura é suficiente para sustentar a Fase 1 e futuras extensões.

### Entregável
Arquitetura do sistema validada e compatível com a especificação do projeto.

---

## SP3 — Contratos de API

Status: EM ANDAMENTO

### Objetivo
Definir os contratos de entrada e saída das interfaces públicas do assistente.

### Conteúdo mínimo
- payload para sugestão da Fase 1;
- payload de resposta com resposta sugerida, artigos, confiança e ticket sugerido;
- endpoint de aprovação do ticket;
- endpoint de feedback;
- endpoint de auto-piloto, quando aplicável;
- contratos de erro e validação.

### Critérios de aceite
- os payloads seguem o modelo esperado pela arquitetura;
- o contrato está documentado antes da implementação;
- a API permite validação por Pydantic e testes automatizados;
- a compatibilidade com a especificação foi verificada antes da execução.

### Entregável
API versionada e contratos formalizados para os principais fluxos do assistente.

---

## SP4 — Integração com GLPI

Status: EM ANDAMENTO

### Objetivo
Definir a estratégia de integração com o GLPI para consulta, contexto e criação de tickets com aprovação humana.

### Conteúdo mínimo
- cliente único para interação com o GLPI;
- mapeamento de campos de ticket e solicitante;
- consulta de histórico e tickets similares;
- política de criação de ticket;
- idempotência para ações de criação;
- auditoria da ação executada no GLPI.

### Critérios de aceite
- a integração não altera o core do GLPI nem o banco de dados;
- a criação de ticket depende de aprovação humana na Fase 1;
- a ação é rastreável e idempotente;
- a integração é isolada em um componente único e reutilizável.

### Entregável
Cliente de integração com GLPI encapsulado e pronto para uso pelo orquestrador.

---

## SP5 — Base de conhecimento e RAG

Status: DONE

### Objetivo
Implementar a recuperação contextual da base de conhecimento do GLPI para apoiar a resposta sugerida e a classificação.

### Conteúdo mínimo
- estrutura de dados para artigos e conteúdos;
- mecanismo de busca ou rankeamento relevante;
- consulta contextual por ticket, pergunta e solicitante;
- tratamento para ausência de resultados relevantes;
- reforço do contexto do atendimento na resposta.

### Critérios de aceite
- os resultados relevantes são recuperados para consultas típicas do suporte;
- a busca considera o contexto do problema e não apenas palavras isoladas;
- os resultados têm relevância suficiente para alimentar o LLM;
- em caso de baixa relevância, o sistema registra e trata essa condição.

### Entregável
Mecanismo de RAG funcional e integrado ao orquestrador.

---

## SP6 — IA e resposta sugerida

Status: DONE

### Objetivo
Definir a camada de adaptação ao modelo LLM e a geração de respostas e classificações relevantes para o suporte.

### Conteúdo mínimo
- adapter configurável para provedor LLM;
- prompt base e contexto do ticket;
- geração de resposta sugerida;
- geração de categoria, urgência e impacto;
- inclusão do nível de confiança na resposta;
- saída padronizada em contrato do sistema.

### Critérios de aceite
- a resposta do modelo é contextualizada com a base de conhecimento;
- a resposta traz nível de confiança e classificação explicita;
- a saída usa schema consistente e validado;
- a camada LLM é desacoplada do restante da solução.

### Entregável
Motor de geração de resposta sugerida, com contexto e classificação por domínio.

---

## SP7 — Guardrails e segurança

Status: DONE

### Objetivo
Aplicar regras de segurança, governança e validação para impedir respostas inadequadas, acidentalmente sensíveis ou fora do escopo.

### Conteúdo mínimo
- regras de validação do conteúdo;
- tratamento de dados sensíveis e PII;
- política de aprovação humana antes de criar ticket;
- política de escalonamento para atendimento humano;
- regras de perfil de usuário e permissão de ação;
- registro de risco e decisão de guardrails.

### Critérios de aceite
- a resposta é validada antes de ser entregue ao agente;
- ações críticas exigem supervisão humana;
- dados sensíveis são minimizados e protegidos;
- as decisões do guardrail ficam rastreáveis para auditoria.

### Entregável
Camada de guardrails funcional, segura e documentada.

---

## SP8 — Observabilidade e feedback

Status: DONE

### Objetivo
Registrar a interação, capturar feedback e coletar métricas para melhoria contínua.

### Conteúdo mínimo
- log da interação e do contexto;
- persistência de feedback útil, não útil ou editado;
- registro de decisão e ações do orquestrador;
- métricas de latência, confiança e aceitação;
- indicadores para melhoria da qualidade do atendimento.

### Critérios de aceite
- cada interação tem rastreabilidade;
- o feedback gerencia aprendizado contínuo;
- métricas básicas e permanentes existem para operação e melhoria;
- os dados coletados não comprometem a segurança ou privacidade.

### Entregável
Sistema de observabilidade e feedback funcional.

---

## SP9 — Testes e garantia de qualidade

Status: DONE

### Objetivo
Validar a qualidade do desenvolvimento em cada camada e garantir a estabilidade do MVP.

### Conteúdo mínimo
- testes unitários para módulos core;
- testes de integração com GLPI;
- testes de API e contratos;
- testes de guardrails;
- testes de fluxo de aprovação e rejeição;
- cobertura mínima orientada ao objetivo do núcleo.

### Critérios de aceite
- os testes refletem comportamento real do sistema;
- as mudanças são validadas antes de avançar para a próxima etapa;
- falhas de negócio e de segurança são detectadas cedo;
- a evidência de validação acompanha cada incremento.

### Entregável
Base de testes automatizados e validação contínua do MVP.

---

## SP10 — MVP da Fase 1

Status: DONE

### Objetivo
Entregar a primeira versão operacional do assistente para apoio ao agente humano.

### Conteúdo mínimo
- API de sugestão funcional;
- identificação do solicitante a partir de e-mail ou login;
- busca por artigos relevantes na base de conhecimento;
- resposta sugerida com nível de confiança;
- classificação de categoria, urgência e impacto;
- criação de ticket somente após aprovação humana;
- registro de feedback da interação;
- auditoria da operação.

### Critérios de aceite
- a Fase 1 funciona para o principal fluxo de atendimento;
- a criação de ticket sem aprovação não é permitida;
- o agente pode revisar e aprovar ou rejeitar a sugestão;
- o MVP está validado com evidência objetiva.

### Entregável
MVP funcional da Fase 1, pronto para uso controlado e validação operacional.

---

## SP11 — Evolução para Fase 2

Status: DONE

### Objetivo
Preparar a evolução do mesmo núcleo para atendimento direto ao cliente com políticas de segurança mais rígidas.

### Conteúdo mínimo
- reaproveitamento do núcleo compartilhado;
- interface para atendimento direto ao cliente;
- política de autoatendimento com limiar definido;
- escalonamento automático para atendimento humano;
- guardrails específicos por perfil;
- tratamento de conteúdo sensível e anonimização quando necessário.

### Critérios de aceite
- a Fase 2 reutiliza exatamente o mesmo núcleo sem duplicação estrutural;
- a interface muda, mas a inteligência e o guardrail continuam compartilhados;
- a política de segurança e escalonamento foi definida antes da aplicação;
- a evolução não compromete a Fase 1.

### Entregável
Plano de extensão para a Fase 2 preservando a arquitetura compartilhada.

---

## Dependências de precedência

- SP1 deve preceder SP2 e demais etapas.
- SP2 deve preceder SP3, SP4 e SP5.
- SP3 e SP4 são pré-condições para a implementação do fluxo funcional.
- SP5, SP6 e SP7 devem se desenvolver de forma integrada antes do MVP.
- SP8 e SP9 reforçam qualidade, observabilidade e maturidade do sistema.
- SP10 define a entrega da Fase 1.
- SP11 é evolução posterior e não substitui o núcleo da Fase 1.

---

## Regra de execução

Antes de qualquer implementação de código, a equipe deve confirmar:

1. a especificação da etapa atual;
2. o plano de execução correspondente;
3. os critérios de aceite e validação da etapa;
4. a precedência com as etapas anteriores.

A execução sem essa base é considerada incompleta e fora do processo do projeto.
