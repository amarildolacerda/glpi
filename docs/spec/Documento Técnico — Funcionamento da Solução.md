# Documento Técnico — Funcionamento da Solução

Versão: 1.0
Status: Aprovada
Última atualização: 31/10/2026

---

## 1. Visão técnica da solução

A solução é um assistente de suporte construído sobre um núcleo compartilhado, que conecta três elementos principais:

- a base de conhecimento do GLPI;
- um mecanismo de orquestração de IA;
- a integração com o sistema de gestão de tickets.

A ideia central é manter um único motor de decisão que possa ser usado tanto pela Fase 1 (apoio ao agente humano) quanto pela Fase 2 (atendimento direto ao cliente), alterando apenas a camada de interface e os critérios de segurança/escala.

Em termos práticos, o sistema recebe uma pergunta, consulta a base de conhecimento, interpreta o contexto do ticket ou do cliente, classifica a solicitação, sugere uma resposta e, quando necessário, cria ou atualiza registros no GLPI após aprovação humana ou conforme regras predefinidas.

---

## 2. Arquitetura geral

A arquitetura é organizada em camadas com responsabilidades distintas:

### 2.1 Camada de interface

Responsável por receber os dados de entrada e expor endpoints HTTP para cada fase do projeto.

- Fase 1: suporte ao agente humano;
- Fase 2: atendimento direto ao cliente (futura expansão).

A camada de interface valida o payload, autentica o usuário ou o perfil, e entrega o contexto ao orquestrador.

### 2.2 Camada de orquestração

O orquestrador é o componente central da solução. Ele coordena toda a execução do fluxo, definindo a ordem das etapas:

1. receber contexto;
2. consultar a base de conhecimento;
3. solicitar geração de resposta e classificação;
4. aplicar guardrails;
5. montar retorno ao cliente/agente;
6. registrar feedback e métricas;
7. disparar ação no GLPI, quando aprovada.

Essa camada atua como ponto de integração entre interface, IA, RAG e GLPI.

### 2.3 Camada de recuperação de conhecimento (RAG)

A recuperação é feita por meio de busca semântica sobre a base de conhecimento do GLPI.

A lógica pode ser resumida assim:

- extrai-se o texto relevante do conteúdo documental;
- normaliza-se a pergunta e o contexto;
- busca-se similaridade por embedding ou indexação vetorial;
- selecionam-se os artigos mais relevantes;
- entregam-se esses resultados ao LLM para contextualização da resposta.

Esse mecanismo reduz a dependência de memória do modelo e melhora a qualidade da resposta ao basear a resposta em material interno e validado pela organização.

### 2.4 Camada de adaptação ao modelo LLM

O componente de adaptação ao LLM abstrai o provedor usado, permitindo trocar entre:

- Ollama;
- OpenAI;
- Anthropic;
- Gemini;
- outros provedores configuráveis.

Essa camada define:

- o modelo selecionado;
- o prompt base;
- o formato da resposta;
- as regras de contexto e limitações de tokens;
- o controle de temperatura e estratégia do modelo.

Assim, o restante da aplicação não depende de um provedor específico.

### 2.5 Camada de guardrails

Os guardrails funcionam como mecanismo de segurança e governança da solução. Eles verificam se a resposta:

- está dentro do escopo do suporte;
- respeita a sensibilidade do assunto;
- não divulga dados pessoais ou críticos;
- não propõe ação inválida ou perigosa;
- está adequada ao perfil do usuário (agente ou cliente).

Ainda, essa camada define se a resposta deve ser:

- apenas sugerida;
- aprovada automaticamente;
- escalada para atendimento humano;
- registrada para análise de risco.

### 2.6 Camada de integração com GLPI

O cliente do GLPI encapsula todas as chamadas ao sistema, de forma centralizada.

Ele é responsável por:

- buscar dados do ticket;
- localizar o solicitante;
- consultar artigos e históricos;
- criar ticket;
- adicionar acompanhamento;
- registrar interação e feedback.

A integração é feita por meio de um wrapper único, reduzindo acoplamento e permitindo troca de implementação sem alterar o restante do sistema.

### 2.7 Camada de feedback e métricas

Cada interação é registrada para permitir:

- análise de qualidade;
- rastreabilidade operativa;
- medição de respostas úteis ou editadas;
- monitoramento de acurácia e tempo de resposta;
- melhoria contínua do sistema.

Esse componente é essencial para que a solução evolua de forma orientada por dados e não apenas por intuição.

---

## 3. Fluxo técnico da Fase 1

A Fase 1 é a prioridade inicial do projeto e representa o suporte ao agente humano.

### 3.1 Entrada da requisição

O agente envia uma requisição contendo:

- o texto da pergunta;
- o canal de origem (painel, e-mail, Teams etc.);
- o identificador do agente;
- o e-mail ou login do solicitante;
- o identificador do ticket, quando houver.

A API valida o payload e encaminha o contexto para o orquestrador.

### 3.2 Contextualização do ticket

O orquestrador realiza o enriquecimento do contexto com informações do GLPI, como:

- dados do solicitante;
- histórico de tickets relacionados;
- categoria atual do atendimento;
- conteúdo do ticket em aberto;
- artigos relevantes já existentes.

Esse passo é importante porque a resposta precisa ser contextualizada e não apenas baseada na frase isolada do usuário.

### 3.3 Busca na base de conhecimento

A solução consulta o RAG para localizar conteúdos relevantes. O resultado pode incluir:

- artigos da base de conhecimento;
- conteúdos similares;
- histórico de casos parecidos;
- referências sugeridas para resposta.

A busca é indexada para reduzir latência e aumentar precisão.

### 3.4 Geração da resposta

O LLM recebe:

- a pergunta do usuário;
- o contexto do ticket;
- os documentos recuperados;
- instruções do prompt;
- regras de negócio e de segurança.

A resposta gerada contém, em geral:

- texto sugerido ao agente;
- categoria sugerida;
- urgência e impacto;
- confiança da resposta;
- artigos recomendados;
- tickets similares.

A ideia não é responder por conta própria, mas apoiar a decisão humana.

### 3.5 Validação por guardrails

Antes de entregar a resposta ao agente, a camada de guardrails valida:

- se a resposta é coerente e segura;
- se a classificação está de acordo com as regras definidas;
- se ela deve ser tratada como resposta simples ou como alerta de risco;
- se há necessidade de escalonamento.

A validação pode bloquear ou reformular determinados trechos antes da resposta final.

### 3.6 Aprovação humana e criação de ticket

A resposta sugerida é entregue ao agente com nível de confiança. Se o agente editar e aprovar, o sistema gera o payload final do ticket e envia a criação ao GLPI.

Nesse ponto, entram dois requisitos técnicos fundamentais:

- idempotência: evitar duplicação de tickets em reenvios coincidentes;
- auditoria: registrar a interação e o que foi aprovado.

Se a aprovação não ocorrer, a interação pode ser apenas registrada para feedback e melhoria do sistema.

### 3.7 Feedback e aprendizagem

Ao final, o sistema registra:

- se a resposta foi útil;
- se ela foi editada;
- se houve rejeição;
- comentário do agente.

Esse histórico alimenta as métricas e permite ajustar tanto os prompts quanto os algoritmos de busca e classificação.

---

## 4. Fluxo técnico da Fase 2

A Fase 2 reaproveita o mesmo núcleo da Fase 1, mas altera a interface e os critérios de atuação.

O cliente envia uma pergunta diretamente ao sistema. O mesmo orquestrador:

- busca conhecimento;
- classifica a necessidade;
- valida nível de confiança;
- aplica guardrails específicos para cliente;
- decide entre:
  - responder diretamente;
  - escalar para atendimento humano;
  - criar ticket automaticamente em cenário permitido.

O diferencial da fase 2 é que a política de segurança e autoatendimento é mais rígida, com bloqueio de dados sensíveis e estímulo à ação humana quando a confiança é baixa ou a categoria é crítica.

---

## 5. Interação entre componentes

A execução típica da solução pode ser entendida como uma sequência linear, mas com dependências de retorno em vários pontos:

1. Interface recebe e valida a requisição.
2. Orquestrador reúne o contexto do ticket ou cliente.
3. RAG retorna documentos relevantes.
4. LLM gera resposta e classificações.
5. Guardrails validam a resposta e a ação.
6. Feedback Logger registra a interação.
7. GLPI Client executa operação final, quando necessário.

Esse fluxo torna a solução modular: cada componente tem uma função definida e a troca de uma parte não exige reescrever o restante do sistema.

---

## 6. Requisitos técnicos que orientam o funcionamento

A solução é desenhada para atender requisitos fundamentais de qualidade e operação:

- latência aceitável para consultas em suporte em tempo real;
- disponibilidade em horário comercial;
- suporte a LLM local para soberania e redução de dependência de provedores externos;
- autenticação e autorização por perfil;
- isolamento de credenciais por variáveis de ambiente;
- uso obrigatório de arquivo `.env` local para valores reais e sensíveis, sem commit no repositório;
- uso de `.env_default` como referência versionada para novos ambientes e para qualquer mudança de configuração que precise ser replicada;
- rastreabilidade completa de operações;
- cobertura de testes no núcleo da aplicação.

Esses requisitos influenciam diretamente decisões como:

- separação entre API e lógica de negócio;
- uso de modelos e prompts configuráveis;
- centralização do cliente GLPI;
- uso de sistema de logs e auditoria;
- criação e manutenção do arquivo `.env_default` como espelho de referência para novos ambientes, sempre que uma nova variável ou parâmetro de configuração for adicionado.

> Observação: o arquivo `.env` deve permanecer local e fora do controle de versão. O `.env_default` existe para documentar os valores esperados e facilitar a replicação em outro ambiente sem expor segredos.

---

## 7. Ponto de vista técnico do que a solução faz

Do ponto de vista técnico, a solução não é apenas um chat de IA. Ela funciona como um motor de suporte operacional conectado ao GLPI, com capacidade de:

- contextualizar a pergunta em relação ao ticket e ao usuário;
- consultar conhecimento interno e histórico;
- gerar resposta e classificação com base em dados reais;
- validar a ação antes de executá-la;
- registrar a interação para observabilidade e melhoria;
- fazer a operação final no GLPI com segurança e controle.

Em outras palavras, a solução transforma a base de conhecimento e o histórico do GLPI em um sistema inteligente de apoio à decisão, com supervisão humana no nível crítico e base para automação futura.

---

## 8. Conclusão

A arquitetura proposta é organizada para tratar o problema de suporte de forma escalável e segura. O núcleo compartilhado permite que a inteligência seja reutilizada entre diferentes interfaces e perfis, enquanto as regras de guardrails e integração mantêm o sistema alinhado ao contexto operacional do GLPI.

A evolução do projeto depende de manter essa separação clara: interface, orquestração, recuperação de conhecimento, adaptação ao LLM e integração com GLPI são componentes distintos, mas articulados em um único fluxo técnico coerente.
