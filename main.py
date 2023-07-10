import pickle 
import sklearn
import numpy as np

with open("model.pkl","rb") as file:
    model = pickle.load(file)


def predict_func(data: list):
    """
    A pre-trained model
    https://github.com/isakovsh/MachineLearning-Classification/blob/main/Diabet%20Classfication/diabet.ipynb
    """
    data = np.asanyarray(data)
    data = data.reshape(1,-1)
    result = model.predict(data)
    return result
