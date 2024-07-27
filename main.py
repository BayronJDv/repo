import os
import time

""" manejando archivos """

with open('hola.txt','w') as f:
    f.write('text at the end of the file')
    
time.sleep(3)
os.remove('hola.txt')

          

