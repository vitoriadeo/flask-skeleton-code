# Flask Skeleton Code

Este repositório serve como um ponto de partida para projetos Flask. Ele já vem configurado com o padrão Application Factory, suporte a Blueprints, tratamento de erros e ferramentas de padronização de código.

Embora seja um projeto inicial, ele foi desenhado para ser escalável e fácil de manter.

### Sobre este projeto

> Este repositório foi desenvolvido como um laboratório de estudo para dissecar e compreender a arquitetura do Flask em profundidade. O objetivo principal não é apenas ter uma estrutura para clonar, mas dominar o fluxo de dados, o ciclo de vida da aplicação e a interdependência entre módulos.



## Tecnologias e ferramentas

Tem algumas coisas já instaladas, como o gunicorn, commitizen, flask, python dotenv e alguns arquivos já configurados com os módulos de blueprint, loggings, páginas para tratamento de erros, arquivos templates para issues e configurações para ambientes de desenvolvimento e produção.

---

## Como rodar o projeto

> Você vai precisar: Python 3.14 ou superior

Clone o repositório

```bash
git clone https://github.com/vitoriadeo/flask-skeleton-code.git
cd flask-skeleton-code
```

Crie e ative o ambiente virtual
```bash
# No Windows:
python -m venv env
.\env\Scripts\activate

# No Linux/Mac:
python3 -m venv env
source env/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Configure as variáveis de ambiente: crie um arquivo .env na raiz do projeto e defina sua chave secreta:
```plaintext
FLASK_APP=run.py
FLASK_DEBUG=1
SECRET_KEY="sua-chave-super-secreta"
```

Execute o servidor de desenvolvimento:
```bash
python run.py
```

O projeto estará rodando em <http://127.0.0.1:5000> (ou outro endereço indicado no terminal)

---

### Padrões de Commit
Este projeto utiliza o Commitizen para garantir que o histórico do Git fique organizado. Há uma configuração pronta no projeto nomeado como `.cz.toml` mas caso queira fazer suas regras, depois de baixar os requirements, apague o .cz.toml existente e configure outro para o seu ambiente, rode `cz init` no terminal.

Para fazer um commit, em vez de usar `git commit -m "..."`, utilize:
```bash
cz commit
```

E siga o passo a passo interativo no terminal.

Para gerar novas versões (tags) automaticamente:
```bash
cz bump
```
