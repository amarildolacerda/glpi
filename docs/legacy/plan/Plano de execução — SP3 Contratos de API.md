# Plano de execução — SP3 Contratos de API

Versão: 1.0
Status: EM ANDAMENTO
Última atualização: 30/10/2026

---

## Status

SP3: EM ANDAMENTO (conforme rastreador em [Especificações por precedência — SP1 a SP11](../spec/Especifica%C3%A7%C3%B5es%20por%20preced%C3%AAncia%20%E2%80%94%20SP1%20a%20SP11.md)).

Os payloads e as rotas da Fase 1 já existem (`core/schemas.py`, `interfaces/v1_agent_api.py`, `interfaces/v2_client_api.py`). Faltam os contratos de erro e validação (SP3, conteúdo mínimo), os testes negativos e o alinhamento da spec 6.4.

## Objetivo

Formalizar os contratos da API da Fase 1, incluindo contratos de erro e validação, e alinhar a documentação à implementação.

## Escopo

- modelo `ErrorResponse` padronizado em `core/schemas.py` (código, mensagem, detalhes);
- handlers globais FastAPI para 422 (validação Pydantic), 400 e 500, sem vazar stacktrace;
- testes de contrato negativos;
- atualização da spec 6.4 para `/v2/atender`, registrando a decisão;
- não inclui autenticação/autorização: fora do escopo desta SP e registrado como risco.

## Riscos

- quebrar consumidores existentes (mitigação: formato de erro aditivo; endpoints 200 permanecem inalterados);
- autenticação e autorização continuam indefinidas nesta SP, o que limita a proteção dos endpoints até uma etapa futura.

## Sequência de execução

1. documentar o contrato de erro na spec;
2. implementar `ErrorResponse` e exception handlers;
3. criar testes negativos (payload inválido → 422 com corpo padronizado; erro inesperado → 500 padronizado);
4. validar que os 12 testes existentes continuam passando;
5. atualizar o status no rastreador.

## Critérios de aceite

- payload inválido retorna 422 com corpo `ErrorResponse`;
- erros 500 não expõem detalhes internos;
- testes novos e antigos passam;
- spec 6.4 bate com o código;
- contrato documentado antes da validação.

## Resultado esperado

Contratos de entrada, saída e erro da API da Fase 1 formalizados, documentados e validados por testes, com a especificação consistente com a implementação.
