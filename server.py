import json
import os
from sanic import Sanic, response

app = Sanic(__name__)

@app.route("/", methods=["GET"])
async def api_entry_point(request):
    return response.json({"Resposta": "Geoserviço REST online"}, status=200)

@app.route("/edificacoes/<edificacao_id:int>", methods=["GET"])
async def recuperar_edificacao(request, edificacao_id):
    with open('edificacoes.json', 'r') as edificacoes_file:
        file_content = json.loads(edificacoes_file.read())
        edificacoes = [feature for feature in file_content['features'] if feature["id"] == edificacao_id]

        if (len(edificacoes) == 0):
            return response.json({'Resultado': 'Recurso não encontrado'}, status=404)

    return response.json(edificacoes[0], status=200)

@app.route("/edificacoes/<edificacao_id:int>", methods=["PUT"])
async def atualizar_edificacao(request, edificacao_id):
    feature_collection = {
        "type": "FeatureCollection",
        "features": []
    }
    with open('edificacoes.json', 'r') as edificacoes_file:
        file_content = json.loads(edificacoes_file.read())
        for feature in file_content['features']:
            if feature["id"] == edificacao_id:
                feature.update(request.json)
                feature_collection["features"].append(feature)
            else:
                feature_collection["features"].append(feature)

    with open('edificacoes.json', 'w') as edificacoes_file:
        edificacoes_file.writelines(json.dumps(feature_collection))

    return response.json(body=None, status=204)

@app.route("/edificacoes/<edificacao_id:int>", methods=["DELETE"])
async def deletar_edificacao(request, edificacao_id):
    feature_collection = {
        "type": "FeatureCollection",
        "features": []
    }
    with open('edificacoes.json', 'r') as edificacoes_file:
        file_content = json.loads(edificacoes_file.read())
        edificacoes = [feature for feature in file_content['features'] if feature["id"] != edificacao_id]
        feature_collection["features"] = edificacoes

    with open('edificacoes.json', 'w') as edificacoes_file:
        edificacoes_file.writelines(json.dumps(feature_collection))

    return response.json(body=None, status=204)

@app.route("/edificacoes", methods=["GET"])
def recuperar_edificacoes(request):

    # if 'text/html' in request.headers.get("accept").split(","):
    #     with open('map.html') as map_file:
    #         map_file_content = map_file.read()
    #         map_file_content = map_file_content.replace('const geojsonObject = {}', f'const geojsonObject = {json.dumps(feature_collection)}')
    #         return response.html(map_file_content)

    return response.file('edificacoes.json', status=200, mime_type="application/geo+json")

@app.route("/edificacoes", methods=["POST"])
async def criar_edificacao(request):
    with open('edificacoes.json', 'r') as edificacoes_file:
        file_content = json.loads(edificacoes_file.read())
        feature = {'id': len(file_content['features'])+1}
        feature.update(request.json)

        file_content['features'].append(feature)

    with open('edificacoes.json', 'w') as edificacoes_file:
        edificacoes_file.writelines(json.dumps(file_content))

    return response.json({"Create": "Create Edificacao"}, status=201)

if __name__ == '__main__':
    if not os.path.isfile('edificacoes.json'):
        with open('edificacoes.json', 'w') as edificacoes_file:
            feature_collection = {
                "type": "FeatureCollection",
                "features": []
            }
            edificacoes_file.writelines(json.dumps(feature_collection))
    app.run(host="0.0.0.0", port=8000)