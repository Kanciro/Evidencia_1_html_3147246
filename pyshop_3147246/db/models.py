from .database import Base
from sqlalchemy import Column, Integer, String

#crear clase

class Categoria(Base):
    __tablename__="categorias"
    id = Column(Integer,
                PrimaryKey=True,
                )
    nombre = Column(String(20))