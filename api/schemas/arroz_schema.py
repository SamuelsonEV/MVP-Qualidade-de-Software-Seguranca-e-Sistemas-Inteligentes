from pydantic import BaseModel
from typing import Optional, List
from model.arroz import Arroz
import json
import numpy as np

class ArrozSchema(BaseModel):
    """ Define como um novo arroz a ser inserido deve ser representado
    """
    name: str = "Maria"
    preg: int = 6
    plas: float = 148
    pres: float = 72
    skin: float = 35
    test: float = 2
    mass: int = 33.6
    pedi: float = 0.627
    age: int = 50
    
class ArrozViewSchema(BaseModel):
    """Define como um arroz será retornado
    """
    id: int = 1
    name: str = "Maria"
    preg: int = 6
    plas: float = 148
    pres: float = 72
    skin: float = 35
    test: float = 0
    mass: int = 33.6
    pedi: float = 0.627
    age: int = 50
    outcome: int = None
    
class ArrozBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do arroz.
    """
    name: str = "Maria"

class ListaArrozsSchema(BaseModel):
    """Define como uma lista de arrozs será representada
    """
    arrozs: List[ArrozSchema]

    
class ArrozDelSchema(BaseModel):
    """Define como um arroz para deleção será representado
    """
    name: str = "Maria"
    
# Apresenta apenas os dados de um arroz    
def apresenta_arroz(arroz: Arroz):
    """ Retorna uma representação do arroz seguindo o schema definido em
        ArrozViewSchema.
    """
    return {
        "id": arroz.id,
        "name": arroz.name,
        "preg": arroz.preg,
        "plas": arroz.plas,
        "pres": arroz.pres,
        "skin": arroz.skin,
        "test": arroz.test,
        "mass": arroz.mass,
        "pedi": arroz.pedi,
        "age": arroz.age,
        "outcome": arroz.outcome
    }
    
# Apresenta uma lista de arrozs
def apresenta_arrozs(arrozs: List[Arroz]):
    """ Retorna uma representação do arroz seguindo o schema definido em
        ArrozViewSchema.
    """
    result = []
    for arroz in arrozs:
        result.append({
            "id": arroz.id,
            "name": arroz.name,
            "preg": arroz.preg,
            "plas": arroz.plas,
            "pres": arroz.pres,    
            "skin": arroz.skin,
            "test": arroz.test,
            "mass": arroz.mass,
            "pedi": arroz.pedi,
            "age": arroz.age,
            "outcome": arroz.outcome
        })

    return {"arrozs": result}

