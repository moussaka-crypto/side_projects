from os import read
from PIL import Image
from fourier import *

img = Image.open("./img/egg.png")
width, height = img.size

def write_rgba_to_file():
    im = img.load()
    with open("./data/red.txt","w") as r_file, \
        open("./data/green.txt","w") as g_file, \
        open("./data/blue.txt","w") as b_file:
        for x in range(width):
            for y in range(height):
                r,g,b,a =im[x,y]
                r_file.write(str(x)+"\t"+ str(y)+"\t" + str(r) +"\t"+ str(0)+ "\n")
                g_file.write(str(x)+"\t"+ str(y)+"\t" + str(g) +"\t" + str(0)+ "\n")
                b_file.write(str(x)+"\t"+ str(y)+"\t" + str(b) +"\t" + str(0)+ "\n")
    
    r_file.close()
    g_file.close()
    b_file.close()

def write_vec_to_file(vec, name, epsilon):
    with open("./data/transformed_"+name, 'w') as file:
        file.write("_\n")
        for x in vec:
            if epsilon!=0:
                if x[1].abs()>epsilon:
                    file.write(str(x[0][0])+ "\t" +str(x[0][1])+ "\t"+ str(x[1].getReal()) +"\t"+ str(x[1].getImg()) + "\n")
            else:
                file.write(str(x[0][0])+ "\t" +str(x[0][1])+ "\t"+ str(x[1].getReal()) +"\t"+ str(x[1].getImg()) + "\n")
        
    file.close()

def read_single_data_from_file(file):
    vec = []
    for i in range(width):
        for j in range(height):
            vec.append(((str(i),str(j)), Complex(0,0)))
    
    with open(file) as data:
        data.readline()
        for line in data:
            array = line.split()
            for i in range(len(vec)):
                if vec[i][0] == (array[0], array[1]):
                    vec[i]=(((array[0], array[1]), Complex(float(array[2]), float(array[3]))))
    data.close()

    return vec;

def set_image_pixel(vecR, vecG, vecB, target):
    img = Image.open(target)
    im = img.load();

    for i in range(len(vecR)):
        x = int(vecR[i][0][0])
        y = int(vecR[i][0][1])
        im[x,y]=(int(vecR[i][1].getReal()), int(vecG[i][1].getReal()), int(vecB[i][1].getReal()), 255)

    img.save(target)

def process_image(epsilon):
    
    vecR = read_single_data_from_file("./data/red.txt")
    vecG = read_single_data_from_file("./data/green.txt")
    vecB = read_single_data_from_file("./data/blue.txt")

    #Transform
    r_transformed= transformed(vecR, True)
    g_transformed = transformed(vecG, True)
    b_transformed = transformed(vecB, True)
    write_vec_to_file(r_transformed, str(epsilon) + "_red.txt", epsilon)
    write_vec_to_file(g_transformed, str(epsilon) + "_green.txt", epsilon)
    write_vec_to_file(b_transformed, str(epsilon) + "_blue.txt", epsilon)
    
    #Transform back
    r_transformed = read_single_data_from_file("./data/transformed_"+ str(epsilon) + "_red.txt")
    g_transformed = read_single_data_from_file("./data/transformed_"+ str(epsilon) + "_green.txt")
    b_transformed = read_single_data_from_file("./data/transformed_"+ str(epsilon) + "_blue.txt")

    set_image_pixel(r_transformed, g_transformed, b_transformed,"./img/transformed_"+str(epsilon)+".png")


    r_back = transformed(r_transformed, False)
    g_back = transformed(g_transformed, False)
    b_back = transformed(b_transformed, False)
    write_vec_to_file(r_back, "back_"+str(epsilon)+"_red.txt", epsilon)
    write_vec_to_file(g_back, "back_"+str(epsilon)+"_green.txt", epsilon)
    write_vec_to_file(b_back, "back_"+str(epsilon)+"_blue.txt", epsilon)

    #Change target image
    r_back = read_single_data_from_file("./data/transformed_back_"+str(epsilon)+"_red.txt")
    g_back = read_single_data_from_file("./data/transformed_back_"+str(epsilon)+"_green.txt")
    b_back = read_single_data_from_file("./data/transformed_back_"+str(epsilon)+"_blue.txt")

    set_image_pixel(r_back, g_back, b_back, "./img/transformed_"+str(epsilon)+"_back.png")

if __name__ == "__main__": 
    process_image(60)
