# Checklist de Entregáveis — Assistente de IA para GLPI

Versão: 1.0
Status: Proposta
Última atualização: 31/10/2026

---

## 1. Objetivo

Este checklist organiza os entregáveis do projeto e serve como referência de pronto para cada etapa de desenvolvimento. A estrutura foi pensada para manter o foco na Fase 1, sem perder a visão de evolução para a Fase 2.

---

## 2. Entregáveis por etapa

### 2.1 Documentação e base de alinhamento

- [ ] Definição clara do problema de negócio e do objetivo do projeto
- [ ] Documento de especificação técnica aprovado
- [ ] README com visão geral de produto e objetivos
- [ ] AGENTS.md com regras do processo e fluxo de desenvolvimento
- [ ] Arquitetura geral documentada
- [ ] Documento técnico de funcionamento da solução revisado

### 2.2 Arquitetura e desenho do sistema

- [ ] Definição do núcleo compartilhado
- [ ] Separação entre interface, orchestrator, RAG, LLM, guardrails e GLPI Client
- [ ] Definição clara de responsabilidades por camada
- [ ] Fluxo principal da Fase 1 documentado
- [ ] Fluxo principal da Fase 2 documentado como evolução
- [ ] Objetivos de segurança e observabilidade definidos

### 2.3 Contratos de API

- [ ] Definição do payload de entrada da sugestão da Fase 1
- [ ] Definição do payload de resposta da sugestão
- [ ] Definição do endpoint de aprovação do ticket
- [ ] Definição do endpoint de feedback
- [ ] Definição de contratos de erro e validação
- [ ] Validação de compatibilidade com os requisitos da especificação

### 2.4 Integração com GLPI

- [ ] Cliente único para interação com GLPI
- [ ] Mapeamento de campos de ticket e solicitante
- [ ] Política de busca de base de conhecimento
- [ ] Política de consulta de histórico e tickets similares
- [ ] Criação de ticket com aprovação humana
- [ ] Idempotência na criação de tickets
- [ ] Auditoria da ação executada no GLPI

### 2.5 Mecanismo de RAG

- [ ] Estrutura de dados para artigos da base de conhecimento
- [ ] Índice ou mecanismo de busca semântica
- [ ] Relevância e ranking dos resultados
- [ ] Recuperação contextualizada por ticket/solicitante
- [ ] Tratamento de ausência de resultados relevantes

### 2.6 Mecanismo de IA

- [ ] Adapter para provedor LLM configurável
- [ ] Prompt base e regras de contexto
- [ ] Geração de resposta sugerida
- [ ] Geração de categoria, urgência e impacto
- [ ] Inclusão de nível de confiança na resposta
- [ ] Estrutura padronizada de saída para o sistema

### 2.7 Guardrails e segurança

- [ ] Definição das regras de validação do conteúdo
- [ ] Tratamento de dados sensíveis
- [ ] Política para solicitação de aprovação humana
- [ ] Política de escalonamento para atendimento humano
- [ ] Regras de perfil de usuário e permissão de ação
- [ ] Registro de risco e decisão de guardrails

### 2.8 Observabilidade e feedback

- [ ] Registro de interações e contexto
- [ ] Persistência de feedback útil / não útil / editado
- [ ] Logs de decisão e ações do orquestrador
- [ ] Métricas de latência, confiança e aceitação
- [ ] Coleta de indicadores de qualidade do suporte

### 2.9 Testes

- [ ] Testes unitários para módulos core
- [ ] Testes de integração com GLPI
- [ ] Testes de API e contratos
- [ ] Testes de guardrails
- [ ] Testes de fluxo de aprovação e rejeição
- [ ] Cobertura mínima baseada no objetivo do núcleo

### 2.10 MVP da Fase 1

- [ ] API de sugestão funcional
- [ ] Identificação do solicitante a partir de e-mail/login
- [ ] Busca de artigos relevantes da base de conhecimento
- [ ] Resposta sugerida com nível de confiança
- [ ] Sugestão de categoria, urgência e impacto
- [ ] Criação de ticket somente após aprovação humana
- [ ] Registro de feedback da interação
- [ ] Auditoria da operação

### 2.11 Evolução para Fase 2

- [ ] Reuso do mesmo núcleo compartilhado
- [ ] Interface para atendimento direto ao cliente
- [ ] Política de autoatendimento com limiar definido
- [ ] Escalonamento automático para atendimento humano
- [ ] Guardrails específicos por perfil
- [ ] Tratamento de conteúdo sensível e anonimização quando necessário

---

## 3. Critério de pronto por entregável

Cada entregável só deve ser considerado concluído quando:

- atende ao escopo da especificação;
- segue o desenho de arquitetura definido;
- foi validado por testes relevantes;
- está compatível com o GLPI e com o modelo de suporte previsto;
- não expõe credenciais ou dados sensíveis no código;
- possui documentação e regras de manutenção adequadas.

---

## 4. Regra de promoção

- desenvolvimento em `dev`;
- promoção para `main` somente com autorização prévia;
- versão da implementação em `vx.x.x` atualizada no momento da promoção para produção;
- qualquer alteração de ambiente produtivo deve passar por processo de merge ou release aprovado.

---

## 5. Checklist resumido do MVP

- [ ] especificação alinhada com o escopo
- [ ] arquitetura do módulo principal definida
- [ ] API de sugestão implementada
- [ ] RAG funcionando sobre a base de conhecimento
- [ ] LLM adapter configurado
- [ ] guardrails básicos implementados
- [ ] integração com GLPI funcional
- [ ] aprovação humana antes de criar ticket
- [ ] feedback registrado
- [ ] testes básicos executados
- [ ] documentação atualizada

---

## 6. Próximo passo recomendado

A implementação deve seguir este checklist em ordem, priorizando a Fase 1 e deixando a Fase 2 como evolução do mesmo núcleo. Isso reduz riscos, aumenta rastreabilidade e mantém a arquitetura coerente com a especificação.
