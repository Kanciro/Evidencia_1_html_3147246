from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

#crear clase

class Criptomonedas(Base):
    __tablename__="Criptomonedas"
    id_Cripto = Column(Integer, primary_key=True,)
    simbolo = Column(String(20))
    nombre = Column(String(20))
    id_api = Column(Integer)
    fecha_creacion= Column(Integer)



class Valor_historico(Base):
    __tablename__="valor_historico"
    id_valor_historico = Column(Integer, primary_key=True,)
    valor = Column(String(20))
    fecha = Column(Integer)
    id_cripto=Column(Integer, ForeignKey("Criptomonedas.id_Cripto"))


class valor_fiat (Base):
    __tablename__="valor_fiat"
    id_valor_fiat = Column(Integer, primary_key=True,)
    valor = Column(String(20))
    fecha = Column(Integer)
    id_moneda=Column(Integer, ForeignKey("moneda_fiat.id_moneda"))
    id_valor_historico=Column(Integer, ForeignKey("valor_historico.id_valor_historico"))
    hora=Column(Integer)

class moneda_fiat (Base):
    __tablename__="moneda_fiat"
    id_moneda = Column(Integer, primary_key=True,)
    COI = Column(String(20))
    nombre = Column(String(20))


class Calculadora_de_divisas(Base):
    __tablename__="calculadora_de_divisas"
    id_calculadora = Column (Integer, 
                        primary_key=True
                )
    api_valor_fiat = Column(String(50))
    id_cripto = Column(Integer, ForeignKey("Criptomonedas.id_Cripto"))
    cambio = Column(String(100))
    tiempo = Column(String(100))



class Noticias(Base):
    __tablename__ = "noticias"
    id_noticias = Column(Integer, primary_key=True,)
    id_cripto = Column(Integer, ForeignKey("Criptomonedas.id_Cripto"))
    api_id = Column(Integer)
    titulo = Column(String(255))
    url = Column(String(500))
    contenido = Column(String(2000))
    fuente_nombre = Column(String(100))
    categoria_nombre = Column(String(100)) 
    tiempo = Column(Integer) 
    id_fuente =Column (Integer, ForeignKey("fuente.id_fuentes"))
    id_categoria =Column (Integer, ForeignKey("categoria_noticias.id_categoria"))



class Categoria_noticias(Base):
    __tablename__="categoria_noticias"
    id_categoria = Column(Integer, primary_key=True,)
    categoria = Column(String(100))


class Fuentes_noticias(Base):
    __tablename__="fuente"
    id_fuentes = Column(Integer, primary_key=True,)
    fuente = Column(String(100))




class Usuarios(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True)
    email = Column(String(100)) 
    contrasena= Column(String(255)) 
    fecha_nacimiento=Column(Integer)
    

