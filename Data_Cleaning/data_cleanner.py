import pandas as pd
import inspect
import os
import sys
from scipy.io import arff
from sklearn.utils import shuffle

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, PARENT_DIR)

# Carrega arquivo csv usando Pandas usando o path

# Informa o path de importação do dataset
path = CURRENT_DIR + "/Original_Dataset/Rice_Cammeo_Osmancik.arff"


# Load arff file
data = arff.loadarff(path)
dataset = pd.DataFrame(data[0])

# Shuffle dataset
dataset = shuffle(dataset)

# Subistituindo o tipo do arroz para Cammeo ou Osmancik por 1 ou 0
dataset['Class'] = dataset['Class'].map({b'Cammeo': 1, b'Osmancik': 0})

number_of_golden = 200

golden = dataset.iloc[:number_of_golden,:]
trainig = dataset.iloc[number_of_golden:,:]

# Salva golden Dateset
golden.to_csv(PARENT_DIR + "/api/database/rice_golden.csv", index=False)


# Salva Dateset usado para treino
trainig.to_csv(PARENT_DIR + "/Treinando_Modelo/rice_training_dataset.csv", index=False)


