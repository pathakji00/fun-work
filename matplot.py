import numpy as np
import matplotlib.pyplot as plt
import time as t

a = 2
    
start = t.time()

fig, ax = plt.subplots()


while(a == 1):
    while(1):
        elapsed =t.time()- start 
        x = np.linspace(start*2*np.pi, elapsed*2*np.pi, 1000)
        c = np.sin(x)
        ax.cla()
        
        ax.set_ylim(-1.1, 1.1)
        ax.set_xlim(0, 2*np.pi)
        ax.plot(x, c, label='sine-wave', color='blue')
        
        plt.pause(1e-10)
        
        
    plt.show()




while(a == 2):
    while(1):
        elapsed =t.time()- start 
        x = np.linspace(start*2*np.pi, elapsed*2*np.pi, 100)
        c = np.sin(x)
        ax.cla()
        
        ax.set_ylim(-1.1, 1.1)
        

        ax.plot(x, c, label='sine-wave', color='blue')
        
        plt.pause(1e-10)
        
    plt.show()

while(a == 3):
    while(1):
        elapsed =t.time()- start 
        x = np.linspace(start*2*np.pi, elapsed*2*np.pi, 100)
        c = np.tan(x)
        ax.cla()
        
        ax.set_ylim(-1e+2,1e+2)
        

        ax.plot(x, c, label='sine-wave', color='blue')
        
        plt.pause(1e-2)
        
    plt.show()
