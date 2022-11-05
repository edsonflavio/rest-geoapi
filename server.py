import json

from geoalchemy2.functions import ST_AsGeoJSON
from geoalchemy2.shape import to_shape
from sanic import Sanic, response
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Edificacao
from shapely.geometry import shape
import shapely.wkt
import geojson

app = Sanic(__name__)

# alembic init alembic
# alembic revision --autogenerate -m "criar tabelas"
# alembic upgrade head
# (alembic.ini) sqlalchemy.url = postgresql://postgres:12345@localhost/postgis_32_sample
# (alembic/env.py) target_metadata = [Edificacao.metadata]

engine = create_engine(f'postgresql://postgres:12345@localhost:5432/postgis_32_sample', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/", methods=["GET"])
async def retrieve_one_edificacoes(request):
    return response.json({"Resposta": "Geoserviço REST online"}, status=200)

@app.route("/edificacoes/<edificacao_id:int>", methods=["GET"])
async def retrieve_one_edificacoes(request, edificacao_id):
    edificacao = session.query(Edificacao).get(edificacao_id)
    wkt = to_shape(edificacao.geom)
    props = edificacao.to_dict()
    del props["geom"]
    feature_id = props["id"]
    del props["id"]
    feature = geojson.Feature(id=feature_id, geometry=shapely.wkt.loads(wkt.wkt), properties=props)
    return response.json(feature, status=200)

@app.route("/edificacoes/<edificacao_id:int>", methods=["PUT"])
async def update_one_edificacoes(request, edificacao_id):
    return response.json(body=None, status=204)

@app.route("/edificacoes/<edificacao_id:int>", methods=["DELETE"])
async def delete_one_edificacoes(request, edificacao_id):
    edificacao = session.query(Edificacao).get(edificacao_id)
    session.delete(edificacao)
    session.commit()
    return response.json(body=None, status=204)

@app.route("/edificacoes", methods=["GET"])
async def retrieve_edificacoes(request):
    feature_collection = {
        "type": "FeatureCollection",
        "features": []
    }

    for row in session.query(Edificacao).all():
        wkt = to_shape(row.geom)
        props = row.to_dict()
        del props["geom"]
        feature_id = props["id"]
        del props["id"]
        feature = geojson.Feature(id=feature_id, geometry=shapely.wkt.loads(wkt.wkt), properties=props)
        feature_collection["features"].append(feature)

    if 'text/html' in request.headers.get("accept").split(","):
        with open('map.html') as map_file:
            map_file_content = map_file.read()
            map_file_content = map_file_content.replace('const geojsonObject = {}', f'const geojsonObject = {json.dumps(feature_collection)}')
            return response.html(map_file_content)

    return response.json(feature_collection, status=200)

@app.route("/edificacoes", methods=["POST"])
async def create_edificacoes(request):
    edificacao = Edificacao(
        nome=request.json["properties"]["nome"],
        geom=f"SRID=4674;{shape(request.json['geometry']).wkt}"
    )
    session.add(edificacao)
    session.commit()
    return response.json({"Create": "Create Edificacao"}, status=201)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)