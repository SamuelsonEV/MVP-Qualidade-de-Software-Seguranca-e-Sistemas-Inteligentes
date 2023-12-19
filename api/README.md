# API 

Este é um projeto de MVP (Minimum Viable Product) de uma API Flask que utiliza machine learning para diferenciar tipos de grãos de arroz.
Ela permite adicionar, visualizar, remover e modificar tarefas da base de dados. 

O objetivo principal deste gerenciador é fornecer uma ferramenta útil.

## Requisitos

* Python 3.* ou docker instalado (opcionalmente docker-compose) 

* Git instalado para clonar o repositório, e após clonar ir ao diretório raiz, pelo terminal.

## Como Utilizar

Para utilizar esta API, siga os passos abaixo:
### 1. Executando:
#### Executando com docker  
Abrir um terminal no diretório raiz do projeto e executar:
```shell
docker run -it -v $PWD:/app -w /app --name api-task-manager --network host --rm python:3.8-slim-buster /app/entrypoint.sh 
```  
#### Executando com docker-compose
Abrir um terminal diretório raiz do projeto e executar:
```shell
docker-compose up
```
#### Executando diretamente no interpretador Python local.
Abrir um terminal no diretório raiz do projeto e executar:
```shell
pip install -r requirements.txt
```
```shell
flask run --host 0.0.0.0 --port 5000
```

### 2. Inserindo dados iniciais
#### Usando Docker (Caso tenha utilizado Docker no passo 1.)
Abrir um terminal no diretório raiz do projeto e executar:
```shell
docker exec api-task-manager bash -c 'python /app/sample_data.py'
```
#### Usando docker-compose (Caso tenha utilizado Docker Compose no passo 1.)
Abrir um terminal no diretório raiz do projeto e executar:
```shell
docker-compose exec api-task-manager bash -c 'python /app/sample_data.py'
```
#### Diretamente no interpretador Python local.
Abrir um terminal no diretório raiz do projeto e executar:
```shell
python ./sample_data.py
```


## Documentação Swagger

Para obter a documentação completa desta API no estilo Swagger, acesse: 
[http://localhost:5000/](http://localhost:5000)

## Autor

Este projeto foi desenvolvido por Samuelson E. V.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](https://www.mit.edu/~amini/LICENSE.md) para obter detalhes.