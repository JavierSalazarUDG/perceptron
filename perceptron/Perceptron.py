import numpy as np
import matplotlib.pyplot as plt
class Perceptron:
    def __init__(self,n):
        self.pesos = np.random.rand(n)
        self.n =n


    def propagacion(self,entradas):
        self.salida = 1*(self.pesos.dot(entradas)>0) 
        self.entradas = entradas


    def actualiza(self,alfa,salidad):
        for i in range(0,self.n):
            self.pesos[i]=self.pesos[i]+alfa*(salidad-self.salida)*self.entradas[i]

    def evalua(self,entrada):
        result = 1*(self.pesos.dot(entrada)>0)
        print(result)