import os # file management lib

def deleteImages():
    try: 
        for image in os.listdir("images"): #access image file names in images folder
            os.remove(f"images\\{image}") #using its path name, remove each image
        print("Images folder is cleared")
    except Exception as e:
        print(e)
deleteImages()
images_folder = [image for image in os.listdir("images")]
print(images_folder)