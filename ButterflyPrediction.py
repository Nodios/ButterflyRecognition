from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter.filedialog import askopenfilenames
import azureWebService as azure

root = Tk()

root.title("Butterfly recognition")
root.geometry("500x300")

image_formats= [("JPEG", "*.jpg")]
file_path_list = askopenfilenames(filetypes=image_formats, initialdir="/", title='Please select a picture to analyze')

for file_path in file_path_list:
    image = Image.open(file_path)

    [imageSizeWidth, imageSizeHeight] = image.size

newImageSizeWidth = 300
newImageSizeHeight = 300 

image = image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

Canvas1 = Canvas(root)

Canvas1.create_image(newImageSizeWidth/2,newImageSizeHeight/2,image = img)    
Canvas1.pack(side=LEFT,expand=True,fill=BOTH)

x = azure.getImage(0,1,False,file_path)
azure.getPrediction(azure.predictButterfly(x))
mlabel = Label(text = azure.getPrediction(azure.predictButterfly(x)))
mlabel.pack()
root.mainloop()
