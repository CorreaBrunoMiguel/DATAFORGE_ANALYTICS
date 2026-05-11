# DATA SCIENCE PLAYBOOK

Versão: 1.0  
Status: Ativo

---

## 1. OBJETIVO

Este documento define os padrões operacionais da DATAFORGE ANALYTICS.

Toda atividade executada dentro da organização deverá seguir as diretrizes
descritas neste playbook.

---

## 2. PRINCÍPIOS OPERACIONAIS

### 2.1 DECISÕES BASEADAS EM EVIDÊNCIA

Nenhuma conclusão poderá ser realizada sem:

- análise
- evidência
- validação
- justificativa técnica

---

### 2.2 DADOS SÃO IMPERFEITOS

Todo dataset deve ser considerado potencialmente:

- inconsistente
- incompleto
- enviesado
- despadronizado
- ruidoso

Nenhuma coluna deve ser considerada confiável sem validação.

---

### 2.3 ORGANIZAÇÃO É OBRIGATÓRIA

Todo projeto deverá possuir:

- estrutura clara
- notebooks organizados
- nomenclatura consistente
- outputs interpretáveis
- narrativa analítica

---

### 2.4 O NEGÓCIO TEM PRIORIDADE

O melhor modelo nem sempre representa a melhor solução.

Toda solução deverá considerar:

- interpretabilidade
- custo
- impacto
- manutenção
- aplicabilidade

---

## 3. PIPELINE OPERACIONAL

Todo projeto seguirá, total ou parcialmente, as etapas abaixo.

### ETAPA 1 — BUSINESS UNDERSTANDING

Objetivos:

- entender problema
- definir métricas
- identificar stakeholders
- entender impacto

---

### ETAPA 2 — DATA UNDERSTANDING

Objetivos:

- investigar estrutura
- identificar padrões
- validar qualidade
- encontrar inconsistências

Checklist mínimo:

- shape
- dtypes
- missing values
- duplicados
- cardinalidade
- distribuição
- correlação

---

### ETAPA 3 — DATA CLEANING

Objetivos:

- padronizar
- corrigir inconsistências
- tratar valores inválidos
- normalizar formatos

---

### ETAPA 4 — EXPLORATORY DATA ANALYSIS

Objetivos:

- gerar hipóteses
- encontrar padrões
- identificar comportamento
- produzir insights

Regra: todo gráfico deve possuir interpretação textual.

---

### ETAPA 5 — FEATURE ENGINEERING

Objetivos:

- melhorar representação dos dados
- reduzir ruído
- aumentar capacidade preditiva

---

### ETAPA 6 — MODELING

Objetivos:

- criar baseline
- comparar modelos
- validar performance
- justificar escolhas

---

### ETAPA 7 — EVALUATION

Objetivos:

- validar generalização
- investigar erros
- analisar métricas
- medir impacto

---

### ETAPA 8 — COMMUNICATION

Objetivos:

- comunicar descobertas
- apresentar recomendações
- traduzir impacto técnico

---

## 4. REGRAS GERAIS

### REGRA 1

Nenhuma limpeza sem justificativa.

---

### REGRA 2

Nenhum gráfico sem interpretação.

---

### REGRA 3

Nenhum modelo sem baseline.

---

### REGRA 4

Nenhuma métrica isolada.

---

### REGRA 5

Sempre investigar risco de data leakage.

---

### REGRA 6

Sempre questionar a qualidade dos dados.

---

### REGRA 7

Toda decisão relevante deve ser documentada.

---

## 5. OBJETIVO FINAL

O objetivo da DATAFORGE ANALYTICS não é apenas produzir código.

O objetivo é desenvolver:

- pensamento analítico
- maturidade técnica
- capacidade investigativa
- rigor metodológico
- visão de negócio
- capacidade de resolver problemas reais
