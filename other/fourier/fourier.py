from datetime import MAXYEAR
from decimal import Decimal
from complex import *

def readComplex(file):
    vec = [Complex(0,0) for _ in range(1000)]
    with open(file) as f:
        f.readline()
        for line in f:
            array = line.split()
            vec[int(array[0])]=(Complex(float(array[1]), float(array[2])))

    return vec

def writeComplex(file, data, epsilon=-1.0):
    with open(file, 'w') as f:
        f.write("1000\n")
        for i in range(len(data)):
            if data[i].abs()>epsilon:
                f.write(str(i)+"\t"+str(data[i].getReal())+"\t"+str(data[i].getImg())+"\n")


def transformed(data, direction):
    transformed = []

    N = len(data)
    factor = 1/math.sqrt(N)
    for n in range(N):
        c = Complex(0,0)
        for k in range(N):
            if direction==True:
                c+=data[k][1] * Complex(-(2.0 * math.pi * k * n)/N)
            else:
                c+=data[k][1] * Complex((2.0 * math.pi * k * n)/N)
        
        c*=factor
        transformed.append((data[n][0],c))
        
        
    return transformed

def deviation(data1, data2):
    sub = []
    for i in range(len(data1)):
        sub.append((data2[i]-data1[i]).abs())
    return max(sub)


data = readComplex("./data/original_data.txt")
fourier_transformed = transformed(data, True)

writeComplex("./data/transformed_default.txt",fourier_transformed)
writeComplex("./data/transformed_01.txt",fourier_transformed,0.1)
writeComplex("./data/transformed_001.txt",fourier_transformed, 0.01)
writeComplex("./data/transformed_0001.txt",fourier_transformed, 0.001)

#default
datanew = readComplex("./data/transformed_default.txt")
fourier_transformed = transformed(datanew, False)
writeComplex("./data/transformedback_default.txt", fourier_transformed)

#0.1
datanew = readComplex("./data/transformed_01.txt")
fourier_transformed = transformed(datanew, False)
writeComplex("./data/transformedback_01.txt", fourier_transformed)

#0.01
datanew = readComplex("./data/transformed_001.txt")
fourier_transformed = transformed(datanew, False)
writeComplex("./data/transformedback_001.txt", fourier_transformed)

#0.001
datanew = readComplex("./data/transformed_0001.txt")
fourier_transformed = transformed(datanew, False)
writeComplex("./data/transformedback_0001.txt", fourier_transformed)

epsilondefault = readComplex("./data/transformedback_default.txt")
epsilon_0001 = readComplex("./data/transformedback_0001.txt")
epsilon_001 = readComplex("./data/transformedback_001.txt")
epsilon_01 = readComplex("./data/transformedback_01.txt")

print("Maximum deviation with default epsilon: ", deviation(data, epsilondefault))
print("Maximum deviation with epsilon = 0.001: ", deviation(data, epsilon_0001))
print("Maximum deviation with epsilon = 0.01: ", deviation(data, epsilon_001))
print("Maximum deviation with epsilon = 0.1: ", deviation(data, epsilon_01))
