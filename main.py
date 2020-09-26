import numpy as np
import matplotlib.pyplot as plt
from  perceptron.Perceptron import *

if __name__ == '__main__':
    per =  Perceptron(3)
    xor = np.array([
        [0,0,1,0],
        [0,1,1,1],
        [1,0,1,1],
        [1,1,1,1]
    ])
    hist_pesos = [per.pesos]
    for epoca in range(0,100):
        for i in range(0,4):
            per.propagacion(xor[i,0:3])
            per.actualiza(0.01,xor[i,3])
            print(per.pesos)
            hist_pesos = np.concatenate((hist_pesos,[per.pesos]),axis=0)
    
    plt.plot(hist_pesos[:,0],'k')
    plt.plot(hist_pesos[:,1],'r')
    plt.plot(hist_pesos[:,2],'b')
    print('evaluando :',0,1)
    per.evalua([1,1,1])
    plt.show()