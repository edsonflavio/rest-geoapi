import json
from datetime import datetime
from uuid import UUID

from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Sequence
from sqlalchemy.orm import declarative_base, DeclarativeMeta

Base = declarative_base()

class Edificacao(Base):
   __tablename__ = 'edificacao'
   __table_args__ = {'schema': 'public'}

   id = Column('id', Integer(), primary_key=True, nullable=False)
   nome = Column('nome', String(length=100), nullable=True)
   geom = Column('geom',Geometry(geometry_type='GEOMETRY', srid=4674, from_text='ST_GeomFromEWKT', name='geometry'),nullable=True)

   # https://mmas.github.io/sqlalchemy-serialize-json
   RELATIONSHIPS_TO_DICT = False

   def __iter__(self):
      return self.to_dict().iteritems()

   def to_dict(self, rel=None, backref=None):
      if rel is None:
         rel = self.RELATIONSHIPS_TO_DICT
      res = {column.key: getattr(self, attr) for attr, column in self.__mapper__.c.items()}
      if rel:
         for attr, relation in self.__mapper__.relationships.items():
            # Avoid recursive loop between to tables.
            if backref == relation.table:
               continue
            value = getattr(self, attr)
            if value is None:
               res[relation.key] = None
            elif isinstance(value.__class__, DeclarativeMeta):
               res[relation.key] = value.to_dict(backref=self.__table__)
            else:
               res[relation.key] = [i.to_dict(backref=self.__table__) for i in value]
      return res

   def to_json(self, rel=None):
      def extended_encoder(x):
         if isinstance(x, datetime):
            return x.isoformat()
         if isinstance(x, UUID):
            return str(x)

      if rel is None:
         rel = self.RELATIONSHIPS_TO_DICT
      return json.dumps(self.to_dict(rel), default=extended_encoder)