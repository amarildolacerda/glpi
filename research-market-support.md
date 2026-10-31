# Pesquisa de mercado e contexto de suporte: registro do levantamento

## Objetivo

Registrar, de forma objetiva e rastreável, o que foi levantado sobre suporte de software, tickets e necessidades operacionais de agentes e administradores de equipes de suporte, com foco em orientar a arquitetura e o roadmap do projeto.

## Método do levantamento

A pesquisa foi conduzida com foco em fontes públicas e no contexto documental já existente no repositório. O objetivo foi validar se os problemas identificados no projeto refletem padrões reais de operação de suporte e não apenas premissas internas.

## Fontes consultadas

### 1. Repositório do projeto
- [README.md](README.md)
- [specs/prd.md](specs/prd.md)
- [specs/project-plan.md](specs/project-plan.md)
- [docs/legacy/spec](docs/legacy/spec)
- [docs/legacy/plan](docs/legacy/plan)

Esses documentos já descrevem explicitamente que o suporte no GLPI lida com tickets repetitivos, baixa reutilização da base de conhecimento, pressão por respostas rápidas e necessidade de supervisão humana.

### 2. Referências públicas e padrões observados em suporte de software

A busca teve como objetivo consolidar direção de produto e não apenas confirmar premissas internas. A literatura e a prática de suporte de software frequentemente reforçam os mesmos pontos:

- ticketing e triagem exigem priorização por urgência e impacto;
- suporte eficiente depende de histórico e base de conhecimento;
- resposta rápida sem qualidade compromete reputação e SLA;
- ações críticas dependem de aprovação humana e auditoria;
- observabilidade e feedback são essenciais para melhoria contínua.

### 3. Fontes externas públicas pesquisadas

- Google Search: consulta pública em "customer support best practices" — resultados públicos reforçaram a recorrência de temas como resposta rápida, conhecimento do produto, suporte empático e resolução da causa raiz.
- YouTube Search: consulta pública em "customer support ticketing best practices" — resultados públicos também destacaram a importância de contexto do cliente, automação leve, triagem e resposta rápida em tickets.
- Help Scout — "10 ways to deliver great customer service": artigo público que reforça que “valuing customers' time” e velocidade de resposta são fundamentais, além da necessidade de conhecimento do produto e continuidade de contexto.
- Pesquisa acadêmica — "Machine Learning for Automated IT Support Ticket Routing": artigo público acadêmico que identifica automação e classificação de tickets como requisitos centrais em ambientes de suporte de TI e serviços, especialmente em volume alto e classificação complexa.

### 4. Citações e conclusões a partir das fontes internas

- [README.md](README.md): descreve o objetivo de apoiar o atendimento em GLPI com foco em produtividade, qualidade da resposta e reutilização da base de conhecimento.
- [specs/prd.md](specs/prd.md): indica que o problema central é reduzir o tempo de primeira resposta, melhorar a acurácia na classificação e reaproveitar a base de conhecimento.
- [specs/project-plan.md](specs/project-plan.md): organiza a execução em ondas e prioriza a Fase 1 como suporte ao agente humano, com Fase 2 API-only como evolução do mesmo núcleo.
- [docs/legacy/spec](docs/legacy/spec): consolida a visão técnica do assistente e reforça a necessidade de suporte humano, guardrails e rastreabilidade.
- [docs/legacy/plan](docs/legacy/plan): documenta a linha de implementação e validação das etapas anteriores, corroborando o padrão de operação e a continuidade da arquitetura.

### 5. Registro de citações formais

#### Fontes externas
- Help Scout: “valuing customers' time is the most important thing in any online customer experience” — [Help Scout / good customer service](https://www.helpscout.com/blog/good-customer-service/)
- Help Scout: artigo reforça que conhecimento do produto, atitude positiva e resolução rápida são elementos centrais do suporte de qualidade — [Help Scout / good customer service](https://www.helpscout.com/blog/good-customer-service/)
- Academic paper: “In a typical IT service desk, the volume of incoming service tickets can exceed several thousands per week...” — [ESA Research / Machine Learning for Automated IT Support Ticket Routing](https://esa-research.org/index.php/EDSJ/article/view/154)
- Google Search / YouTube Search: consultas públicas revisadas para validar temas recorrentes de suporte: velocidade, contexto, classificação e resolução eficiente — [Google Search](https://www.google.com/search?q=customer+support+best+practices) e [YouTube Search](https://www.youtube.com/results?search_query=customer+support+ticketing+best+practices)

#### Fontes internas
- “Aumentar a acurácia na classificação de categoria e urgência” — [specs/prd.md](specs/prd.md)
- “Reduzir o tempo de primeira resposta do suporte” — [specs/prd.md](specs/prd.md)
- “Reaproveitar a base de conhecimento do GLPI por meio de RAG” — [specs/prd.md](specs/prd.md)
- “A Fase 2 será uma API-only para o portal do GLPI” — [specs/adrs/0001-fase-2-via-portal-glpi.md](specs/adrs/0001-fase-2-via-portal-glpi.md)
- “Pipeline lean do projeto: spec → plan → implement → QC → commit” — [AGENTS.MD](AGENTS.MD)
- “A prioridade inicial é a Fase 1: apoio ao agente humano” — [AGENTS.MD](AGENTS.MD)

## O que foi levantado

### Padrões de operação reais de suporte
- Tickets repetitivos consomem tempo do time.
- Suporte precisa classificar tickets rapidamente para priorizar atendimento.
- Agentes precisam consultar KB e históricos para responder sem retrabalho.
- O ganho real vem da redução do tempo de primeira resposta junto com qualidade da resposta.
- Ações sensíveis ou críticas exigem aprovação humana e registro de decisão.

### Need do usuário e do operador
- Agentes de suporte querem reduzir esforço repetitivo.
- Gestores querem métricas de tempo, qualidade e acurácia.
- Usuários do suporte esperam respostas rápidas e consistentes.
- A base de conhecimento precisa ser melhor reutilizada no momento do atendimento.

### Observações relevantes para o produto
- O valor mais relevante para o cliente interno é a produtividade do atendente.
- O valor mais relevante para a operação é a consistência e o controle do processo.
- O maior ganho em produto está em combinar triagem, KB e resposta sugerida em um fluxo único.
- A evolução para atendimento automatizado deve acontecer sobre o mesmo núcleo e sem duplicação de lógica.

## Conclusões coletadas

### 1. O problema do projeto é real e alinhado ao mercado
A repetitividade dos tickets e a necessidade de resposta rápida são padrões comuns em suporte de software. O problema central do projeto não é hipotético: ele reflete uma dor real de operação.

### 2. A Fase 1 deve ser focada no agente humano
A maior oportunidade de valor está em dar velocidade ao atendente, em vez de automatizar a interação sem supervisão. Isso é consistente com a prioridade do projeto e com a necessidade de manter controle, qualidade e segurança.

### 3. A base de conhecimento e a triagem são diferenciais estratégicos
A capacidade de sugerir artigos, tickets similares e classificação adequada é um ganho de eficiência direto e facilmente percebido pela operação.

### 4. A Fase 2 deve ser evolutiva e não reescrita
A arquitetura central deve continuar compartilhada entre as fases. O mecanismo de autoatendimento deve ser uma extensão do núcleo, não uma solução paralela ou dedicada.

### 5. O controle humano e a observabilidade são requisitos de produto, não opcionais
Qualquer avanço em automação precisa manter aprovação humana em ações críticas, auditoria e rastreabilidade de decisões.

## Registro de evidência

### Evidências internas do projeto
- [README.md](README.md) descreve o objetivo de apoiar o atendimento em GLPI com foco em produtividade e qualidade da resposta.
- [specs/prd.md](specs/prd.md) reforça que a redução do tempo de primeira resposta e a acurácia da classificação são objetivos centrais.
- [specs/project-plan.md](specs/project-plan.md) estrutura a entrega em ondas, com foco em núcleo, Fase 1 e Fase 2 API-only.
- [docs/legacy/spec](docs/legacy/spec) e [docs/legacy/plan](docs/legacy/plan) corroboram o histórico do projeto e a evolução do desenho de suporte.

### Evidências de padrão de mercado
- suporte de software normalmente exige triagem rápida, priorização e uso de KB;
- time de suporte precisa de resposta mais rápida sem perder qualidade;
- sistemas de ticketing eficazes priorizam rastreabilidade, classificação e observabilidade.

## Conclusão final

A pesquisa confirmou que o projeto está alinhado com padrões reais de operação de suporte e que a estratégia mais valiosa é priorizar o suporte ao agente humano na Fase 1, com base de conhecimento, triagem inteligente, aprovação humana e métricas de qualidade, e evoluir para atendimento automatizado via API na Fase 2 com o mesmo núcleo técnico.

## Status

Registro consolidado como evidência do levantamento realizado.
