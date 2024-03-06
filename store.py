import random
import time
import linecache

#à utilisé une fois dans befor_run
def store_shuffle(shuf : list):
    with open('shuffel.txt', '+w') as f:
        test = '\n'.join([','.join(map(str,element)) for element in shuf])
        f.write(test)
        f.close()

#à utilisé à chaque changement de pixel
def store_stage(no_stage : int):
    with open('progression.txt','r+') as f:
        f.truncate(0)
        f.writelines(str(no_stage)+'\n')

def store_notfull(notfull : int):
    with open('notfull.txt','r+') as f:
        f.truncate(0)
        f.writelines(str(notfull)+'\n')

#à utilisé seulement quand le temps actuelle n'est pas égal ou sup au temps de départ
def befor_run(shuf : list):
    store_shuffle(shuf)
    store_stage(0)

#ne pas utilisé sauf si vraiment nécessaire
def get_pixel(no_line: int):
    return linecache.getline('shuffel.txt', no_line)

#pour retransformer une ligne en tuple
def tup(element):
    pos = element.split(",")
    return (int(pos[0]),int(pos[1]))

#pour récoupérer l'ordre de tous les pixels #important si le programme crash
def get_pixels():
    with open('shuffel.txt', 'r') as f:
        lines = f.readlines()
    return list(map(tup,lines))

#seulement utilisé si le programme crash
def get_stage():
    with open('progression.txt','r') as f:
        return int(f.readline())
    
def get_notfull():
    with open('notfull.txt','r') as f:
        return float(f.readline()[0:-1])

