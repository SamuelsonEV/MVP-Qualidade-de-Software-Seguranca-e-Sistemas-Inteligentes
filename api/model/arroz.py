from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base

# colunas = Pregnancies,Glucose,BloodPressure,SkinThickness,test,BMI,DiabetesPedigreeFunction,Age,Outcome

class Arroz(Base):
    __tablename__ = 'arrozs'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    preg = Column("Pregnacies", Integer)
    plas = Column("Glucose", Float)
    pres = Column("BloodPressure", Float)
    skin = Column("SkinThickness", Float)
    test = Column("Insulin", Float)
    mass = Column("BMI", Integer)
    pedi = Column("DiabetesPedigreeFunction", Float)
    age = Column("Age", Integer)
    outcome = Column("Diagnostic", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, preg:int, plas:float, pres:float, name:float,
                 skin:float, test:float, mass:int,
                 pedi:float, age:int, outcome:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Arroz

        Arguments:
        name: nome do arroz
            preg: número de gestações
            plas: concentração de glicose
            pres: pressão sanguínea
            skin: espessura da pele
            test: insulina
            mass: índice de massa corporal
            pedi: função pedigree
            age: idade
            outcome: diagnóstico
            data_insercao: data de quando o arroz foi inserido à base
        """
        self.name=name
        self.preg = preg
        self.plas = plas
        self.pres = pres
        self.skin = skin
        self.test = test
        self.mass = mass
        self.pedi = pedi
        self.age = age
        self.outcome = outcome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao