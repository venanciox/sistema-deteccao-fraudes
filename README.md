# Sistema de Detecção de Fraudes

Projeto em desenvolvimento para estudo de **Python**, **APIs** e lógica de detecção de fraudes em transações financeiras.

O sistema analisa alguns fatores de uma transação e calcula uma pontuação de risco.

## Funcionalidades atuais

* Análise de risco de transações
* Classificação em baixo, médio ou alto risco
* Regras baseadas em:
    * valor da transação
    * horário
    * novo destinatário
    * quantidade de transações recentes
* API REST com FastAPI
* Validação de dados com Pydantic
* Histórico de análises salvo em JSON

## Tecnologias

* Python
* FastAPI
* Pydantic
* Uvicorn
* Git e GitHub

## Executando

Instale as dependências:
```bash
pip install -r requirements.txt
```

Para executar a API:
```bash
uvicorn api:app --reload
```

Documentação da API:
```text
http://127.0.0.1:8000/docs
```

Também é possível executar a versão pelo terminal:
```bash
python main.py
```

## Status

**Projeto em desenvolvimento.**

Novas funcionalidades e melhorias serão adicionadas conforme o projeto evoluir.

Desenvolvido para estudo e prática de desenvolvimento de software e detecção de fraudes.