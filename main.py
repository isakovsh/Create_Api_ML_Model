import pickle 
import sklearn
import numpy as np

with open("model.pkl","rb") as file:
    model = pickle.load(file)
data = np.asanyarray(6, 148, 72, 35, 0, 33.6, 0.627, 50, 1)
data= data.reshape(1,-1)
result = model.predict([])

print(result)

