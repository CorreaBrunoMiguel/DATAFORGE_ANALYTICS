# REPOSITORY_OPERATIONS

## OBJETIVO

Este documento define as regras operacionais de repositório da DATAFORGE
ANALYTICS.

O objetivo é garantir:

- organização
- rastreabilidade
- clareza estrutural
- hygiene operacional
- padronização técnica
- escalabilidade sustentável

Projetos de dados degradam rapidamente sem governança adequada de repositório.

A organização do ambiente faz parte oficial da qualidade técnica da empresa.

---

## PRINCÍPIOS OPERACIONAIS

A operação de repositórios da DATAFORGE deve priorizar:

- simplicidade
- rastreabilidade
- clareza
- consistência
- modularidade
- manutenção sustentável

Nenhum repositório deve evoluir sem estrutura operacional mínima.

---

## FILOSOFIA DE REPOSITÓRIO

O repositório representa:

- ambiente operacional
- histórico institucional
- rastreabilidade analítica
- evolução técnica
- documentação viva
- contexto organizacional

O Git não deve ser tratado apenas como backup.

O histórico do repositório deve permitir entender:

- o que foi feito
- por que foi feito
- quando foi feito
- como evoluiu
- quais decisões foram tomadas

---

## ESTRATÉGIA ATUAL DA DATAFORGE

### MODELO OPERACIONAL

A DATAFORGE utiliza inicialmente estratégia de:

- monorepo controlado

Objetivo:

- reduzir overhead inicial
- centralizar governança
- facilitar evolução do framework
- acelerar experimentação
- manter consistência institucional

---

## ESTRUTURA PADRÃO DO REPOSITÓRIO

Estrutura esperada:

```tree
DATAFORGE_ANALYTICS/
│
├── CORE/
├── PROJECTS/
├── dataforge/
├── scripts/
├── SANDBOX/
├── README.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

---

## DIRETÓRIOS INSTITUCIONAIS

### CORE/

Contém documentação institucional da DATAFORGE.

Exemplos:

- workflows
- operating rules
- review criteria
- project lifecycle
- repository governance

O CORE representa a camada normativa da empresa.

---

### PROJECTS/

Contém projetos analíticos independentes.

Cada projeto representa:

- um contexto empresarial
- um dataset
- uma investigação operacional
- uma narrativa analítica própria

Estrutura esperada:

```text
PROJECTS/
└── PROJECT_NAME/
    ├── data/
    ├── notebooks/
    ├── docs/
    ├── reports/
    └── README.md
```

---

### dataforge/

Contém código reutilizável institucional.

Exemplos:

- utilitários
- dataset managers
- helpers
- pipelines
- validações
- abstrações internas

---

### SANDBOX/

Ambiente experimental.

Utilizado para:

- testes rápidos
- validações temporárias
- experimentação
- prototipagem

O conteúdo da SANDBOX não representa artefato oficial do projeto.

---

## POLÍTICA DE NOTEBOOKS

### NOTEBOOKS SÃO ARTEFATOS OFICIAIS

Notebooks fazem parte oficial das entregas operacionais.

Devem possuir:

- organização
- clareza
- rastreabilidade
- separação lógica
- interpretação analítica
- comunicação adequada

---

### NOTEBOOKS NÃO DEVEM

Notebooks NÃO devem:

- funcionar como dump de runtime
- armazenar outputs massivos
- persistir tracebacks desnecessários
- conter células desorganizadas
- possuir execução confusa
- misturar contextos distintos

---

### OUTPUTS

Preferência operacional:

- outputs limpos antes de commits relevantes

Especialmente:

- tabelas extensas
- tracebacks
- gráficos temporários
- outputs de debug

---

### EXECUTION COUNTS

Execution counts devem preferencialmente:

- permanecer limpos OU
- permanecer coerentes

Execution noise excessivo reduz legibilidade do diff.

---

### MARKDOWN ANALÍTICO

Markdowns analíticos devem ser preservados.

A documentação investigativa faz parte oficial da qualidade do notebook.

---

## POLÍTICA DE DATASETS

### DATASETS PEQUENOS

Datasets pequenos podem ser versionados quando:

- melhorarem reprodutibilidade
- não comprometerem performance do repositório
- fizerem parte do contexto oficial do projeto

---

### DATASETS GRANDES

Datasets grandes NÃO devem ser commitados diretamente.

Estratégias futuras podem incluir:

- armazenamento externo
- DVC
- cloud buckets
- pipelines de download
- versionamento especializado

---

### DADOS SENSÍVEIS

Dados sensíveis nunca devem ser commitados.

Incluindo:

- credenciais
- tokens
- dados privados
- informações protegidas
- arquivos internos não autorizados

---

## POLÍTICA DE .gitignore

O `.gitignore` deve proteger o repositório contra:

- lixo operacional
- caches
- arquivos temporários
- artefatos de runtime
- outputs locais

---

### ITENS NORMALMENTE IGNORADOS

Exemplos:

```text
.venv/
__pycache__/
.ipynb_checkpoints/
.pytest_cache/
.env
*.pyc
*.pyo
*.log
dist/
build/
*.egg-info/
```

---

## POLÍTICA DE COMMITS

### COMMITS DEVEM SER RASTREÁVEIS

Todo commit deve comunicar:

- intenção
- contexto
- natureza da alteração

---

### PADRÕES RECOMENDADOS

Exemplos:

```text
foundation: establish DATAFORGE lean core

feat(core): add dataset manager abstraction

feat(df001): initialize hotel booking investigation

fix(df001): correct invalid reservation parsing

docs(core): refine review workflow
```

---

### COMMITS INADEQUADOS

Evitar commits como:

```text
update
fix
changes
misc
final
ajustes
teste
```

Commits genéricos reduzem rastreabilidade institucional.

---

## POLÍTICA DE STAGING

O staging deve ser controlado.

Evitar:

```bash
git add .
```

sem inspeção prévia.

---

### ANTES DE TODO COMMIT

Verificações mínimas recomendadas:

```bash
git status
git diff --stat
git diff
```

---

## POLÍTICA DE PUSH

Pushes devem ocorrer apenas após:

- revisão do staging
- validação das alterações
- commit coerente
- working tree controlada

---

## WORKING TREE

A working tree deve permanecer saudável.

Evitar:

- dezenas de arquivos alterados simultaneamente
- mudanças sem contexto
- acúmulo prolongado de alterações não commitadas

---

## BRANCHES

### ESTRATÉGIA ATUAL

Inicialmente a DATAFORGE pode operar predominantemente em:

- main

Objetivo:

- reduzir complexidade inicial
- priorizar disciplina operacional

---

### EVOLUÇÃO FUTURA

Conforme maturidade aumentar:

- feature branches
- PR workflows
- release branches
- CI/CD

podem ser incorporados.

---

## REVISÃO OPERACIONAL

Toda alteração relevante deve ser revisada considerando:

- impacto estrutural
- rastreabilidade
- organização
- risco operacional
- coerência metodológica

---

## HIGIENE OPERACIONAL

Problemas considerados críticos:

- notebooks gigantes com outputs
- datasets massivos commitados
- caches versionados
- commits genéricos
- working tree descontrolada
- mistura excessiva de contextos
- ausência de organização estrutural

---

## CRESCIMENTO DO REPOSITÓRIO

A arquitetura da DATAFORGE deve evoluir organicamente.

Novas ferramentas ou estruturas só devem surgir quando:

- necessidade real aparecer
- reutilização justificar
- limitação operacional existir

---

## CRITÉRIOS PARA SPLIT FUTURO

Projetos poderão futuramente sair do monorepo quando:

- crescerem excessivamente
- exigirem autonomia operacional
- possuírem lifecycle independente
- necessitarem deploy específico
- exigirem governança própria

---

## AUTOMAÇÕES FUTURAS

Possíveis evoluções:

- hooks Git
- notebook cleaning automático
- linting
- CI pipelines
- validações automatizadas
- testes institucionais
- pre-commit hooks

A introdução dessas ferramentas deve ocorrer apenas quando houver necessidade
operacional real.

---

## PRINCÍPIO CENTRAL

A organização do repositório faz parte oficial da maturidade técnica.

Ambientes caóticos comprometem:

- investigação
- manutenção
- colaboração
- revisão
- escalabilidade
- qualidade analítica

A DATAFORGE trata governança operacional como parte fundamental da engenharia de
dados e analytics.
