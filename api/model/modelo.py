import numpy as np
import pickle
import joblib
import pandas as pd

class Model:
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model,scaler, form):
        """Realiza a predição de um arroz com base no modelo treinado
        """
        # [form.preg, form.plas, form.pres, form.skin, form.test, form.mass, form.pedi]
        data = {"Area": [form.preg],
                "Perimeter": [form.plas],
                "Major_Axis_Length": [form.pres],
                "Minor_Axis_Length": [form.skin],
                "Eccentricity": [form.test],
                "Convex_Area": [form.mass],
                "Extent": [form.pedi]
                }

        # atributos = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age']
        atributos = ["Area", "Perimeter", "Major_Axis_Length", "Minor_Axis_Length", "Eccentricity", "Convex_Area",
                     "Extent"]
        entrada = pd.DataFrame(data, columns=atributos)
        array_entrada = entrada.values
        X_entrada = array_entrada[:, 0:7].astype(float)
        rescaledEntradaX = scaler.transform(X_entrada)
        print(rescaledEntradaX)
        # Predição de classes dos dados de entrada
        saidas = model.predict(rescaledEntradaX)
        print("first:")
        print(saidas.item())
        return int(saidas.item())