import json

from sanic import Sanic, response
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from shapely.geometry import shape
from models import Edificacao
from geoalchemy2.functions import ST_AsGeoJSON

engine = create_engine("postgresql://postgres:postgres@localhost/postgis_33_sample", echo=True)
app = Sanic(__name__)

@app.route("/edificacoes", methods=["GET"])
async def list_edificacoes(request):
    features = []

    stmt = select(Edificacao.id, Edificacao.name, ST_AsGeoJSON(Edificacao.geom)).order_by(Edificacao.id)
    with engine.connect() as conn:
        rows = conn.execute(stmt)
        for id, name, geometry in rows:
            feature = {
                "id": f"{id}",
                "type": "Feature",
                "properties": {
                    "nome": f"{name}"
                },
                "geometry": json.loads(geometry)
            }
            features.append(feature)

    feature_collection = {
        "type": "FeatureCollection",
        "features": features
    }

    if 'text/html' in request.headers.get("accept").split(","):
        with open('map.html') as map_file:
            map_file_content = map_file.read()
            map_file_content = map_file_content.replace('const geojsonObject = {}', f'const geojsonObject = {json.dumps(feature_collection)}')
        return response.html(map_file_content)
    return response.json(feature_collection)

@app.route("/edificacoes", methods=["POST"])
async def create_edificacoes(request):

    geom = shape(request.json['geometry'])
    edificacao = Edificacao(name=request.json['properties']['nome'], geom=f"SRID=4674;{geom}")

    with Session(engine) as session:
        session.add(edificacao)
        session.commit()

    return response.json({"Message": "Created!"}, status=201)

@app.route("/edificacoes/<id:int>", methods=["GET"])
async def get_edificacao(request, id):
    stmt = select(Edificacao.id, Edificacao.name, ST_AsGeoJSON(Edificacao.geom)).where(Edificacao.id == id)
    with engine.connect() as conn:
        resp = conn.execute(stmt).first()
        if resp is None:
            return response.json({'Resultado': 'Recurso não encontrado'}, status=404)

        id, name, geometry = resp

        feature = {
            "id": f"{id}",
            "type": "Feature",
            "properties": {
                "nome": f"{name}"
            },
            "geometry": json.loads(geometry)
        }

    return response.json(feature, status=200)

@app.route("/edificacoes/<id:int>", methods=["PUT"])
async def update_edificacao(request, id):

    with Session(engine) as session:
        edificacao = session.get(Edificacao, id)
        edificacao.name = request.json["properties"]["nome"]
        session.add(edificacao)
        session.commit()
    return response.json(body=None, status=204)


@app.route("/edificacoes/<id:int>", methods=["DELETE"])
async def delete_edificacao(request, id):
    with Session(engine) as session:
        edicicacao = session.get(Edificacao, id)
        session.delete(edicicacao)
        session.commit()
    return response.json(body=None, status=204)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8500)