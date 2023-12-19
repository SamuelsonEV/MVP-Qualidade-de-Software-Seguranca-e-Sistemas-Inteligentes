from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Arroz, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
arroz_tag = Tag(name="Arroz", description="Adição, visualização, remoção e predição de arrozs com Diabetes")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de arrozs
@app.get('/arrozs', tags=[arroz_tag],
         responses={"200": ArrozViewSchema, "404": ErrorSchema})
def get_arrozs():
    """Lista todos os arrozs cadastrados na base
    Retorna uma lista de arrozs cadastrados na base.
    
    Args:
        nome (str): nome do arroz
        
    Returns:
        list: lista de arrozs cadastrados na base
    """
    session = Session()
    
    # Buscando todos os arrozs
    arrozs = session.query(Arroz).all()
    
    if not arrozs:
        logger.warning("Não há arrozs cadastrados na base :/")
        return {"message": "Não há arrozs cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d arrozs econtrados" % len(arrozs))
        return apresenta_arrozs(arrozs), 200


# Rota de adição de arroz
@app.post('/arroz', tags=[arroz_tag],
          responses={"200": ArrozViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: ArrozSchema):
    """Adiciona um novo arroz à base de dados
    Retorna uma representação dos arrozs e diagnósticos associados.
    
    Args:
        name (str): nome do arroz
        preg (int): número de vezes que engravidou: Pregnancies
        plas (int): concentração de glicose no plasma: Glucose
        pres (int): pressão diastólica (mm Hg): BloodPressure
        skin (int): espessura da dobra cutânea do tríceps (mm): SkinThickness
        test (int): insulina sérica de 2 horas (mu U/ml): Insulin
        mass (float): índice de massa corporal (peso em kg/(altura em m)^2): BMI
        pedi (float): função pedigree de diabetes: DiabetesPedigreeFunction
        age (int): idade (anos): Age
        
    Returns:
        dict: representação do arroz e diagnóstico associado
    """
    
    # Carregando modelo
    ml_path = 'ml_model/rice_model.joblib'
    modelo = Model.carrega_modelo(ml_path)
    sc_path = 'ml_model/rice_scaler.pkl'
    scaler = Model.carrega_modelo(sc_path)
    
    arroz = Arroz(
        name=form.name.strip(),
        preg=form.preg,
        plas=form.plas,
        pres=form.pres,
        skin=form.skin,
        test=form.test,
        mass=form.mass,
        pedi=form.pedi,
        age=form.age,
        outcome=Model.preditor(modelo, scaler, form)
    )
    logger.debug(f"Adicionando produto de nome: '{arroz.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se arroz já existe na base
        if session.query(Arroz).filter(Arroz.name == form.name).first():
            error_msg = "Arroz já existente na base :/"
            logger.warning(f"Erro ao adicionar arroz '{arroz.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando arroz
        session.add(arroz)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado arroz de nome: '{arroz.name}'")
        return apresenta_arroz(arroz), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar arroz '{arroz.name}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de arroz por nome
@app.get('/arroz', tags=[arroz_tag],
         responses={"200": ArrozViewSchema, "404": ErrorSchema})
def get_arroz(query: ArrozBuscaSchema):    
    """Faz a busca por um arroz cadastrado na base a partir do nome

    Args:
        nome (str): nome do arroz
        
    Returns:
        dict: representação do arroz e diagnóstico associado
    """
    
    arroz_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{arroz_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    arroz = session.query(Arroz).filter(Arroz.name == arroz_nome).first()
    
    if not arroz:
        # se o arroz não foi encontrado
        error_msg = f"Arroz {arroz_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{arroz_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Arroz econtrado: '{arroz.name}'")
        # retorna a representação do arroz
        return apresenta_arroz(arroz), 200
   
    
# Rota de remoção de arroz por nome
@app.delete('/arroz', tags=[arroz_tag],
            responses={"200": ArrozViewSchema, "404": ErrorSchema})
def delete_arroz(query: ArrozBuscaSchema):
    """Remove um arroz cadastrado na base a partir do nome

    Args:
        nome (str): nome do arroz
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    arroz_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre arroz #{arroz_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando arroz
    arroz = session.query(Arroz).filter(Arroz.name == arroz_nome).first()
    
    if not arroz:
        error_msg = "Arroz não encontrado na base :/"
        logger.warning(f"Erro ao deletar arroz '{arroz_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(arroz)
        session.commit()
        logger.debug(f"Deletado arroz #{arroz_nome}")
        return {"message": f"Arroz {arroz_nome} removido com sucesso!"}, 200