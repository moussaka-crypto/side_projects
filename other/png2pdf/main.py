from tkinter import filedialog
import os
from fpdf import FPDF

if __name__ == '__main__':
    dir_path = filedialog.askdirectory(title="Choose dir with .png files")
    directory_files = os.listdir(dir_path) # Exceptionhandling still missing (be careful)
    pdf = FPDF(unit="pt", format=[width,heigth]) # Choose width and heigth of images
    
    for page in range(0,directory_files.__len__()):
        data = dir_path+"/Data_"+str(page)+".png"
        pdf.add_page()
        pdf.image(data,x=0,y=0,w=0, h=0) # Images are placed at top left corner 
        print("Page: " + str(page+1) + " has been added.")
        
    pdf.output("merged.pdf",'F') 
