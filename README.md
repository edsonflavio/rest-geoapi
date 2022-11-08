# Geoserviço REST

## Para a correta execução do serviço é necessário que os passos a seguir seja executados:

### Instalação do python versão 3.8.10
https://www.python.org/downloads/release/python-3810/

### Instalação do postman
Para o consumo da API será usado o cliente web postman, que permite realizar requisições HTTP completas (manipulando cabeçalho, corpo e método da requisição)

https://www.postman.com/downloads/?utm_source=postman-home

### Instalação das bibliotecas python necessárias
Depois de fazer o download deste projeto, através do prompt de comando do windows, acesse a pasta do projeto usando o comando 'cd <nome-da-pasta>' e depois execute o seguinte comando

    pip install -r requirements.txt

### Executar serviço
Para que o geoserviço começe a receber requisições, execute o comando abaixo

    python server.py

Depois disso será possível acessá-lo através do endereço http://localhost:8000 usando qualquer cliente web como o postman ou qualquer navegador

### Editar código
Para editar o código recomenda-se o uso do pychar community 
    
https://www.jetbrains.com/pt-br/pycharm/download/#section=windows
