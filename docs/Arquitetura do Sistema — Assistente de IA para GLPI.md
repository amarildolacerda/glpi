# Arquitetura do Sistema — Assistente de IA para GLPI

Versão: 1.0
Status: Proposta
Última atualização: 31/10/2026

---

## 1. Objetivo da arquitetura

A arquitetura do projeto foi concebida para resolver o problema de suporte no GLPI com foco em três pilares:

- reduzir o tempo de resposta do atendimento;
- aumentar a qualidade da classificação e da resposta sugerida;
- manter a supervisão humana no fluxo crítico, sem abrir brechas de segurança ou automação indevida.

A solução se organiza em um núcleo compartilhado, reutilizável entre Fase 1 e Fase 2, com diferenciação principalmente na camada de interface e na política de guardrails.

---

## 2. Princípios arquiteturais

A arquitetura segue os seguintes princípios:

1. Núcleo compartilhado
   - o mesmo motor de orquestração, RAG, integração com LLM e regras de domínio deve servir tanto à Fase 1 quanto à Fase 2;
   - a diferença entre as fases é funcional e de política, não de duplicação estrutural.

2. Separação de responsabilidades
   - interface, orquestração, recuperação de conhecimento, LLM, guardrails e GLPI são módulos distintos;
   - a mudança em um componente não deve exigir reescrita dos demais.

3. Segurança por design
   - dados sensíveis devem ser tratados por políticas explícitas;
   - ações críticas, como criação de ticket, exigem validação e/ou aprovação humana;
   - credenciais ficam fora do código e no ambiente de execução.

4. Observabilidade e auditoria
   - cada interação deve ser registrada para análise, melhoria e conformidade.

5. Compatibilidade com GLPI
   - o sistema não altera o banco do GLPI nem o core do sistema;
   - toda interação ocorre por meio de um wrapper de integração bem definido.

---

## 3. Visão de alto nível

```text
┌──────────────────────────────────────────────────────────────┐
│                        Interfaces                            │
│  Fase 1: agente humano                                      │
│  Fase 2: cliente / portal / widget (futuro)                 │
└───────────────────────────┬──────────────────────────────────┘
                            │ HTTP / API
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                   Núcleo compartilhado                        │
│  ┌───────────────┐  ┌──────────────┐  ┌────────────────────┐ │
│  │ Orchestrator  │  │ RAG / KB     │  │ Guardrails         │ │
│  └──────┬────────┘  └──────┬───────┘  └─────────┬──────────┘ │
│         │                    │                       │      │
│         ▼                    ▼                       ▼      │
│  ┌───────────────┐  ┌──────────────┐  ┌────────────────────┐ │
│  │ LLM Adapter   │  │ Vector Index │  │ GLPI Client        │ │
│  └───────────────┘  └──────────────┘  └─────────┬──────────┘ │
└───────────────────────────────────────────────────────┼────┘
                                                        │
                                                        ▼
                                            ┌──────────────────┐
                                            │ GLPI / Base de  │
                                            │ conhecimento /  │
                                            │ tickets / APIs  │
                                            └──────────────────┘
```

---

## 4. Camadas da arquitetura

### 4.1 Camada de interfaces

A camada de interfaces expõe os pontos de entrada do sistema e representa a experiência de uso por perfil.

#### Fase 1: agente humano

Responsabilidades:

- receber a pergunta da solicitação;
- identificar usuário/solicitante e contexto do ticket;
- entregar sugestão ao agente;
- permitir aprovação ou rejeição da resposta;
- registrar feedback.

#### Fase 2: atendimento ao cliente

Responsabilidades:

- receber pergunta do cliente;
- validar perfil e nível de confiança;
- decidir entre resposta direta, escalonamento ou criação de ticket;
- aplicar guardrails mais rígidos por perfil e contexto.

A interface deve ser desacoplada do núcleo para permitir variação de canais e perfis sem interferir na lógica central.

---

### 4.2 Camada de orquestração

O orquestrador é o componente central do sistema. Ele coordena a sequência de operações e decide o fluxo esperado.

#### Responsabilidades principais

- receber o contexto da solicitação;
- complementar dados do ticket, do solicitante e do canal;
- consultar a base de conhecimento via RAG;
- preparar o prompt e o payload para o LLM;
- receber sugestões de resposta e classificação;
- aplicar regras de guardrails;
- decidir se a operação deve seguir para criação de ticket ou retorno apenas sugerido;
- persistir metadados e feedback.

O orquestrador funciona como “motor de decisão” da aplicação.

---

### 4.3 Camada de recuperação de conhecimento (RAG)

A recuperação de conhecimento é responsável por conectar a inteligência ao material interno do GLPI.

#### Funções

- pesquisar artigos e conteúdos relevantes;
- procurar tickets históricos similares;
- retornar contexto útil ao modelo;
- reduzir erros por ausência de base documental;
- contextualizar respostas com dados confiáveis da organização.

#### Fluxo técnico

1. a pergunta entra no sistema;
2. o contexto do ticket/cliente é incorporado;
3. a busca semântica consulta a base de conhecimento;
4. os resultados mais relevantes são priorizados por similaridade;
5. esse conjunto de documentos é passado ao modelo LLM para síntese e resposta.

---

### 4.4 Camada de adaptação ao LLM

A camada de adaptação ao LLM abstrai o provedor de inteligência artificial para permitir trocas sem impacto em outras partes do sistema.

#### Responsabilidades

- selecionar o provedor configurado;
- montar o prompt com contexto e instruções;
- controlar parâmetros relevantes do modelo;
- padronizar a resposta em schema de saída;
- encapsular variações entre provedores.

#### Provedores esperados

- Ollama (preferencial para soberania/local);
- OpenAI;
- Anthropic;
- Gemini;
- outros compatíveis via configuração.

Essa camada reduz acoplamento entre aplicação e fornecedor de IA.

---

### 4.5 Camada de guardrails

Os guardrails são uma camada estratégica de segurança e governança, e não um componente opcional.

#### Funções

- validar a resposta do modelo;
- impedir ações indevidas ou inseguras;
- filtrar dados sensíveis;
- decidir quando a resposta deve apenas ser sugerida;
- decidir quando escalonar para atendimento humano;
- bloquear autoatendimento em casos de risco ou baixa confiança.

#### Exemplos de validações

- categoria fora do escopo;
- tentativa de expor dados pessoais;
- resposta sem nível de confiança adequado;
- geração de ação que exige aprovação do agente;
- autoatendimento em caso de categoria sensível.

---

### 4.6 Camada de integração com GLPI

A camada de integração encapsula todas as interações com o GLPI através de um cliente único e centralizado.

#### Responsabilidades

- consultar dados do ticket;
- identificar solicitante;
- buscar artigos e histórico;
- criar ticket;
- adicionar acompanhamento;
- registrar feedback interno;
- garantir idempotência em ações de criação.

#### Requisito técnico

Todo o acesso ao GLPI deve passar por uma abstração única, de modo que a troca de estratégia de integração ou adaptações do GLPI não afetem o restante da solução.

---

### 4.7 Camada de feedback, métricas e auditoria

A solução deve registrar qualquer interação relevante para acompanhamento, qualidade e melhoria contínua.

#### Dados que devem ser persistidos

- pergunta recebida;
- contexto de entrada;
- artigos consultados;
- resposta sugerida;
- categoria, urgência e impacto sugeridos;
- confiança atribuída;
- feedback do agente ou do cliente;
- ticket criado e o identificador da interação.

Essa camada fornece base para:

- análise de eficiência;
- melhoria dos prompts;
- ajuste do ranking da busca;
- avaliação do impacto real da IA no suporte.

---

### 4.8 Camada de configuração e prompts

A configuração deve centralizar parâmetros de execução, evitando codificação rígida.

#### Inclui

- configuração do provedor LLM;
- regras de guardrails;
- prompts de sistema;
- parâmetros do modelo;
- endpoints e credenciais de ambiente;
- regras de autenticação e autorização.

A separação de configuração facilita implantação, manutenção e testes.

---

## 5. Fluxo funcional da Fase 1

### 5.1 Cenário principal

1. O agente envia uma pergunta por uma interface de suporte.
2. A API valida o payload e identifica o contexto do ticket.
3. O orquestrador busca o solicitante e dados relevantes no GLPI.
4. O RAG consulta a base de conhecimento e artigos semelhantes.
5. O LLM gera resposta sugerida, categoria, urgência e impacto.
6. Os guardrails validam a resposta e a classificação.
7. A resposta é devolvida ao agente com nível de confiança.
8. O agente revisa e aprova ou rejeita a proposta.
9. Em caso de aprovação, o GLPI Client cria o ticket com idempotência.
10. O feedback e a interação são registrados.

### 5.2 Regra crítica

A criação de ticket não deve ocorrer de forma automática sem aprovação humana na Fase 1, mesmo quando a resposta do modelo for considerada confiável.

---

## 6. Fluxo funcional da Fase 2

A Fase 2 reutiliza o mesmo núcleo da Fase 1, mas com uma política mais rígida de segurança e autoatendimento.

### Fluxo típico

1. Cliente envia pergunta ao atendimento automatizado.
2. O orquestrador monta contexto relevante.
3. O RAG busca conhecimento e histórico.
4. O LLM gera resposta proposta.
5. Os guardrails validam se a resposta é segura e adequada ao cliente.
6. Se a confiança for alta e a categoria permitir, o sistema responde diretamente.
7. Se a confiança ou o contexto não forem adequados, o sistema escala para atendimento humano.

### Diferença principal

A diferença entre Fase 1 e Fase 2 não está no núcleo, e sim na interface e nos critérios de decisão.

---

## 7. Estrutura de módulos proposta

A estrutura de módulos esperada é a seguinte:

```text
glpi-ai-support/
├── core/
│   ├── orchestrator.py
│   ├── rag.py
│   ├── llm.py
│   ├── guardrails.py
│   ├── glpi_client.py
│   └── schemas.py
├── interfaces/
│   ├── phase1_agent_api.py
│   └── phase2_client_api.py
├── feedback/
│   ├── logger.py
│   └── metrics.py
├── config/
│   ├── prompts/
│   ├── guardrails.yaml
│   └── settings.py
├── tests/
├── scripts/
│   └── ingest_kb.py
├── main.py
└── README.md
```

---

## 8. Dependências e integração

### Dependências principais

- GLPI para base de conhecimento e tickets;
- RAG para recuperação semântica;
- LLM para geração e classificação;
- FastAPI para interfaces HTTP;
- Pydantic para validação de modelos;
- pytest para testes automatizados.

### Critério de acoplamento

O sistema deve manter baixa dependência entre módulos. Em especial:

- a API não deve conhecer detalhes internos do modelo;
- o LLM não deve conhecer implementação do GLPI;
- o GLPI Client não deve implementar regras de negócio da IA;
- o guardrails não deve misturar lógica de acesso ao banco ou apresentação.

---

## 9. Requisitos de qualidade que a arquitetura deve satisfazer

A arquitetura deve garantir:

- latência aceitável para resposta orientada a agente;
- isolamento de credenciais e ambiente;
- rastreabilidade completa das interações;
- idempotência na criação de tickets;
- suporte a LLM local como requisito inicial da Fase 1;
- compatibilidade com os contratos da API definidos pela especificação;
- capacidade de extensão para a Fase 2 sem reescrever o núcleo.

---

## 10. Conclusão

A arquitetura proposta organiza a solução em módulos com funções bem definidas, preservando a separação entre as fases do projeto e o núcleo compartilhado. Ela atende ao objetivo principal do sistema: apoiar o atendimento no GLPI com segurança, qualidade e rastreabilidade, ao mesmo tempo em que prepara a evolução para um atendimento mais automatizado no futuro.

A solução ganha robustez porque o núcleo de IA e integração é compartilhado, enquanto a interface e as políticas de segurança adaptam a experiência conforme o perfil do usuário. Esse desenho reduz risco de duplicação, facilita manutenção e alinha a implementação com a proposta de negócio do projeto.
