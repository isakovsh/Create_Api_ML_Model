import numpy as np

class LinearRegressionGD:
    def __init__(self,lr=0.01,n_iterations=10000):
        self.lr  = lr
        self.n_iterations = n_iterations
        self.theta1 = 0
        self.theta0 = 0
    
    def fit(self,X,y):
        n = X.shape[0]
        self.theta1 = 0
        self.theta0 = 0
        self.cost_ = []

        for _ in range(self.n_iterations):
            y_pred = self.theta1 * X + self.theta0 
            cost = (1/n)* sum(data**2 for data in (y-y_pred))
            self.cost_.append(cost)
             
            self.theta1 = self.theta1 - (-2/n) * self.lr * np.sum(X*(y-y_pred))
            self.theta0 = self.theta0 - (-2/n) * self.lr * np.sum(y-y_pred)
    
    def predict(self,X):
        pred = self.theta1 * X + self.theta0
        return pred