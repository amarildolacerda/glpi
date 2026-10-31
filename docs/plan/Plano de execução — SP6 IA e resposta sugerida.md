# Plano de execução — SP6 IA e resposta sugerida

Versão: 1.0
Status: DONE
Última atualização: 31/10/2026

---

## Objetivo

Implementar a camada de adaptação ao modelo de IA para geração da resposta sugerida, mantendo a separação entre orquestração, RAG, LLM e guardrails.

## Requisito da SP6

A SP6 corresponde à etapa de IA e resposta sugerida da sequência de precedência. A implementação deve respeitar:

- uso de um adapter configurável para provedor LLM;
- base de conhecimento já recuperada pelo RAG;
- geração de resposta sugerida com contexto do ticket e da pergunta;
- classificação de urgência, impacto e categoria;
- nível de confiança explícito;
- saída padronizada para o restante do sistema.

## Escopo do incremento

1. criar adapter de IA local e configurável;
2. gerar resposta por contexto e palavras-chave do suporte;
3. devolver dados estruturados para o orquestrador;
4. manter desacoplamento entre camada de IA e camada de API;
5. validar com teste automatizado.

## Critérios de aceite

- a camada LLM consegue gerar uma resposta estruturada;
- a resposta é contextualizada pelo conteúdo recuperado do RAG;
- a resposta inclui confiança e classificação mínima;
- o orquestrador usa o adapter sem acoplamento direto com a API externa;
- o teste relevante passa.

## Riscos

- acoplamento entre LLM e orquestrador;
- respostas pouco relevantes sem contexto do RAG;
- perda de padronização da resposta.

## Sequência de execução

1. definir o contrato do adapter de IA;
2. criar teste para comportamento esperado da resposta;
3. implementar o adapter com lógica local segura;
4. integrar o adapter no orquestrador;
5. validar com pytest e ajustar se necessário.

## Status atual

- SP5: DONE
- SP6: EM ANDAMENTO
- SP9: DONE
- SP10: DONE

A implementação só avança se o comportamento do adapter for validado no teste e a estrutura continuar consistente com a arquitetura.
