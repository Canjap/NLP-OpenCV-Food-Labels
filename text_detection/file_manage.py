import os # file management lib

for image in os.listdir("images"): #access image file names in images folder
    os.remove(f"images\\{image}") #using its path name, remove each image