# Conversor de TXT/CSV para RSS

## Como rodar localmente
1. Clone o repositório e entre na pasta do projeto:
    ```bash
    git clone https://github.com/seu-repo/conversor-rss.git
    cd conversor-rss
    ```
2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```
3. Configure as variáveis de ambiente:
    ```bash
    cp .env.example .env
    ```
4. Execute a aplicação:
    ```bash
    python run.py
    ```
5. Acesse `http://127.0.0.1:5000/` e envie um arquivo TXT ou CSV para conversão.

## Implantação no Render.com
1. Crie um novo serviço web no Render.com.
2. Escolha o repositório do GitHub.
3. Configure as variáveis de ambiente conforme o `.env`.
4. Use `gunicorn wsgi:app` como comando de inicialização.