# Plano de execução — SP8 Observabilidade e feedback

## Status
DONE

## Objetivo
Registrar a interação, capturar feedback e coletar métricas básicas para melhoria contínua do assistente.

## Escopo
- registro da interação com identificador e contexto;
- persistência de feedback útil, não útil e editado;
- coleta de métricas simples de confiança, latência e aprovação;
- integração do logger na API de feedback;
- documentação do comportamento e validação por testes.

## Riscos
- feedback não ser persistido em um formato reutilizável;
- métricas limitadas prejudicarem rastreabilidade;
- integração sem contrato claro gerar inconsistência entre endpoints e logs.

## Sequência de execução
1. definir o contrato de observabilidade para interação e feedback;
2. criar testes que validem o registro de feedback e métricas;
3. implementar `feedback/logger.py` e `feedback/metrics.py`;
4. integrar a resposta da API `/v1/feedback` com o logger;
5. validar com pytest e confirmar que a etapa está estável.

## Critérios de aceite
- cada interação possui identificador rastreável;
- feedback útil, não útil e editado é registrado em estrutura consistente;
- métricas básicas existem e podem ser consumidas por operação;
- a API expõe o registro sem expor dados sensíveis.

## Resultado esperado
Sistema de observabilidade e feedback funcional, operável e rastreável no núcleo do projeto.
