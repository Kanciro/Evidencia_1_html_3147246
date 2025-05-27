from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

#crear clase

class Categoria(Base):
    __tablename__="categorias"
    66
    id = Column(Integer, primary_key=True,)
    nombre = Column(String(20))


class Productos(Base):
    __tablename__="Productos"
    id = Column(Integer, primary_key=True,)
    nombre = Column(String(20))
    precio = Column(Integer)
    categoria_id = Column(Integer , ForeignKey("categorias.id"))

