# 🚀 Projeto ETL Automático com Python e SQL Server

Este projeto implementa um pipeline **ETL (Extract, Transform, Load)** totalmente automatizado utilizando Python, com:

- Geração automática de dados simulados
- Transformação dos dados usando pandas
- Carga para banco de dados SQL Server via SQLAlchemy com ODBC Driver 18
- Logging detalhado para monitoramento
- Pipeline executável via script único `auto-etl.py`
- Suporte para agendamento de execução automática (Windows Task Scheduler, cron, etc)

---

## ✨ Funcionalidades

- **Geração automática de dados:** simula registros para carregar no banco
- **Transformação:** limpeza e preparação dos dados com pandas
- **Carga:** inserção dos dados no SQL Server com segurança e eficiência
- **Logs:** gravação das etapas para facilitar debug e acompanhamento
- **Automação:** todo o fluxo executado com um único comando Python

---

## 🚀 Como executar

### 1. Configurar ambiente virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar a string de conexão

Edite o arquivo `etl/load.py` e ajuste a variável `string_conexao` com suas credenciais e detalhes do servidor SQL Server:

```python
string_conexao = (
    "mssql+pyodbc://USUARIO:SENHA@HOST/NOME_BANCO"
    "?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
)
```

> **Importante:** substitua `USUARIO`, `SENHA`, `HOST` e `NOME_BANCO` conforme seu ambiente.

### 4. Executar o pipeline completo

```bash
python auto-etl.py
```

### 5. Verificar logs

O arquivo `etl.log` será criado e atualizado automaticamente, contendo informações sobre cada etapa do processo.

---

## ⏰ Agendamento (Opcional)

Para rodar o pipeline automaticamente em intervalos regulares, configure:

- **Windows Task Scheduler** (Agendador de Tarefas do Windows)
- **cron** no Linux/macOS

Basta apontar o agendador para executar o script `auto-etl.py` usando o interpretador Python do seu ambiente virtual.

---

## 📋 Requisitos

- Python 3.8 ou superior
- SQL Server (local ou remoto)
- ODBC Driver 18 para SQL Server instalado no sistema
- Bibliotecas Python instaladas via `pip install -r requirements.txt`

---


