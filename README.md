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
    
## Exercícios
    
### 1. Retornar a área do poligono
#### DICA: quando precisar retornar valores em metros (cálculo de área ou distância, por exemplo), converter a geometria para UTM (SRID=31982) antes
    
### 2. Retornar o centroid de uma edificacao
#### DICA: Sempre que precisarmos retornar uma geometria é interessante utilizar ST_AsGeoJSON para converter a geometria

### 3. Retornar um buffer do poligono em geojson
    
### 4. Retornar um buffer do poligono em html representado no mapa
#### IMPORTANTE: O template para criação do mapa espera objetos do tipo Feature ou FeatureCollection, então deve-se adicionar a geometria a estrutura da Feature antes de retornar o HTML
#### Exemplos de GeoJSON: https://en.wikipedia.org/wiki/GeoJSON
    
### 5. Determinar a distância entre duas edificacoes
    
### 6. Retornar true ou false em resposta a operação crosses ou contains entre duas geometrias (passando o id da geometria A e da geometria B)
