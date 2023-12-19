from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.preprocessing import StandardScaler

class Avaliador:

    def avaliar(self, modelo, X_test, Y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler().fit(X_test)  # ajuste do scaler com o conjunto de treino
        rescaledX = scaler.transform(X_test)
        predicoes = modelo.predict(rescaledX)
        # print(predicoes.item())
        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return (accuracy_score(Y_test, predicoes),
                recall_score(Y_test, predicoes, average='binary'),
                precision_score(Y_test, predicoes, average='binary'),
                f1_score(Y_test, predicoes, average='binary'))
