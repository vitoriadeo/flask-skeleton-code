# Flask Skeleton Code

> Uma estrutura base organizada para iniciar projetos Flask rapidamente, seguindo boas práticas de desenvolvimento.

Este repositório serve como um ponto de partida para projetos Flask. Ele já vem configurado com o padrão Application Factory, suporte a Blueprints, tratamento de erros e ferramentas de padronização de código.

Embora seja um projeto inicial, ele foi desenhado para ser escalável e fácil de manter.

## 🚀 Tecnologias e Ferramentas

Tem algumas coisas já instaladas, como o Gunicorn, Commitizen, Flask, Python Dotenv e alguns arquivos já configurados com os módulos de Blueprint, loggings, páginas para tratamento de erros, arquivos templates para issues e configurações para ambientes de desenvolvimento e produção.

---

## Estrutura do Projeto

```text
flask-skeleton-code/
├── app/
│   ├── controllers/     # Rotas e lógica (Blueprints)
│   ├── static/          # Arquivos CSS, JS e imagens
│   ├── templates/       # Arquivos HTML
│   │   └── error/       # Páginas de erro (404, 500)
│   ├── __init__.py      # Fábrica do Aplicativo (create_app)
│   └── config.py        # Configurações de Ambiente (Dev/Prod)
├── tests/               # (Em construção) Testes automatizados
├── .cz.toml             # Configuração do Commitizen
├── .env.example         # Exemplo das variáveis de ambiente
├── .gitignore           # Arquivos ignorados pelo Git
├── requirements.txt     # Dependências do projeto
├── run.py               # Ponto de entrada para desenvolvimento
└── README.md            # Documentação
```

---

## Como rodar o projeto

> Você vai precisar do python 3.14 ou superior
Clone o repositório:

```bash
git clone [https://github.com/vitoriadeo/flask-skeleton-code.git](https://github.com/vitoriadeo/flask-skeleton-code.git)
cd flask-skeleton-code
```

Crie e ative o ambiente virtual:
No Windows:

```bash
python -m venv env
.\env\Scripts\activate
```

No Linux/Mac:

```bash
python3 -m venv env
source env/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure as variáveis de ambiente: Crie um arquivo .env na raiz do projeto (baseado no .env.example) e defina sua chave secreta:

```plaintext
FLASK_APP=run.py
FLASK_DEBUG=1
SECRET_KEY="sua-chave-super-secreta"
```

Execute o servidor de desenvolvimento:

```bash
python run.py
```

O projeto estará rodando em: <http://127.0.0.1:5000>

### Padrões de Commit

Este projeto utiliza o Commitizen para garantir que o histórico do Git fique organizado.

Para fazer um commit, em vez de usar `git commit -m "..."`, utilize:

```bash
cz commit
```

E siga o passo a passo interativo no terminal.

Para gerar novas versões (tags) automaticamente:

```bash
cz bump
```

## Próximos Passos (To-Do)

Como este é um projeto de aprendizado contínuo, as próximas melhorias planejadas são:

[ ] Implementar testes automatizados (Pytest).
[ ] Adicionar configuração para Banco de Dados (SQLAlchemy/Migrate).
[ ] Criar um Dockerfile para containerização.
