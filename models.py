from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
Base = declarative_base()

class Edificacao(Base):
    __tablename__ = 'edificacao'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    geom = Column('geom',Geometry(geometry_type='POLYGON', srid=4674, from_text='ST_GeomFromEWKT', name='geometry'),nullable=True)