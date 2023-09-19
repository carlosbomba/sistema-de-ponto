from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Boolean, LargeBinary
import datetime

Base = declarative_base()

class PointTable(Base):
    #descrevendo o que temos no banco de dados
    __tablename__ = "ponto"

    codigo = Column(Integer, primary_key=True)
    cnpj_empresa = Column(Integer, nullable=True)
    matricula = Column(Integer, nullable=True)
    data_entrada = Column(DateTime(timezone=True), nullable=True)
    hora_entrada = Column(DateTime(timezone=True), nullable=False)
    data_saida = Column(DateTime(timezone=True), nullable=True)
    hora_saida = Column(DateTime(timezone=True), nullable=True)
