from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import  declarative_base

#variable cadena de conexion
MARIADB_URL='mysql+pymysql://root:admin@127.0.0.1:3315/pyshop_3147246'
#creer objeto
engine= create_engine(MARIADB_URL)

#PLANTILLA BASE
Base=declarative_base()