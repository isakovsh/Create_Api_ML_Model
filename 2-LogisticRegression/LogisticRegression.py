import numpy as np 


def sigmoid(x):
    return 1/(1+np.exp(-x))

class LogisticRegressionGD:
    def __init__(self,lr=0.01,n_iter=1000):
        self.lr = lr 
        self.n_iter = n_iter 
        self.theta0 = 0
        self.theta1 = 0


    def fit(self,X,y):
        self.cost = []
        n = X.shape[0] 

        for _ in range(self.n_iter):
            linear_pred = self.theta1 + self.theta0
            y_pred = sigmoid(linear_pred)
            cost = -(1/n) * np.sum(y * np.log(y_pred) + (1-y) * np.log(1-y_pred))
            self.cost.append(cost)

            self.theta1 = self.theta1 - (-2/n) * self.lr * np.sum(X*(y-y_pred))
            self.theta0 = self.theta0 - (-2/n) * self.lr * np.sum(y-y_pred)

    def predict(self,X):
        linear_pred = self.theta1 + self.theta0
        y_pred = sigmoid(linear_pred)
        class_pred = [0 if y<=0.5 else 1 for y in y_pred]
        return class_pred
    
        