# API Shopping

![Badge de versão](https://img.shields.io/github/v/tag/jose-alison/python-api-shopping) ![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN)

# Sobre o projeto

API desenvolvida com Python e FastApi, com o objetivo de fornecer endpoints para cadastro de vendas e controle de estoques. Projeto desenvolvido usando o Python 3.12.

# Clonando o projeto

```
git clone git@github.com:jose-alison/python-api-shopping.git
```

# Instalando as dependencias do projeto

```
pip install -r requirements.txt
```

# Executando o projeto em homologação

```
uvicorn app.main:app --reload --port 3001 --app-dir src
```

# Consultando documentação

A FastApi já implementa a documentação em Swagger e ReDoc.

No projeto, a documentação usando Swagger pode ser acessada no projeto através da url:

    [http://localhost:3001/docs]()

A documentação usando ReDoc, foi desabilitada, mas caso deseje implementá-la, é necessário remover o parametro redoc_url, em `src/app/main.py`:

```
app=FastAPI(
	...

	redoc_url=None
)
```

No projeto, definir o argumento redoc_url como None, desabilita o recurso do projeto. Ao habilitar, será possível consultar o ReDoc através do link:

[http://localhost:3001/redoc]()

# Validando a saúde da API

[
    http://localhost:3001/check](http://localhost:3001/check)

Ao chamar a rota de checagem, é possível receber um retorno com status 200 e a mensagem:

```
{
  "status": "API em funcionamento normal",
  "version": "1.0.0"
}
```
