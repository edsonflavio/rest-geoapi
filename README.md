# Geoserviço REST

## Para a correta execução do serviço é necessário que os passos a seguir seja executados:

### Instalação do python versão 3.11.2
https://www.python.org/downloads/release/python-3112/

### Instalação do postgresql 15.2.1 com postgis 3.3.2
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

### Instalação do postman
Para o consumo da API será usado o cliente web postman, que permite realizar requisições HTTP completas (manipulando cabeçalho, corpo e método da requisição)

https://www.postman.com/downloads/?utm_source=postman-home

### Criação do ambiente virtual python
Para isolar o ambiente de desenvolvimento deste projeto da instalação original do python execute os seguintes passos usando o prompt de comando do windows

    python -m venv <nome-do-ambiente>

    <nome-do-ambiente>\Scripts\activate

### Instalação das bibliotecas python necessárias
Depois de fazer o download deste projeto, através do prompt de comando do windows, acesse a pasta do projeto usando o comando 'cd <nome-da-pasta>' e depois execute o seguinte comando

    pip install -r requirements.txt

### Editar código
Para editar o código recomenda-se o uso do pycharm community 
    
https://www.jetbrains.com/pt-br/pycharm/download/#section=windows
