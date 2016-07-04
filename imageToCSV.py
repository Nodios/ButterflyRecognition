from __future__ import with_statement
from colorthief import ColorThief as CT
import webcolors

class Image(object):
    rd,gd,bd,r1,g1,b1,r2,g2,b2,r3,g3,b3,r4,g4,b4,r5,g5,b5,r6,g6,b6 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    name = ""


def loadImageCT(path):
    #Loads image to ColorThief
    out = CT(path)
    return out;

def colorPaletteToCSV():

    path = "Images/"
    folder = ["americanSnout", "blueMorpho", "gardenTigerMoth", "goliathBirdwing"]

    with open('butterflyData.csv', 'w+') as f:
        f.write('rd,gd,bd,r1,g1,b1,r2,g2,b2,r3,g3,b3,r4,g4,b4,r5,g5,b5,r6,g6,b6,name\n')
        for i in range(0,4):
            print("Folder: " + folder[i])
            for j in range(1,16):
                print("Image: " + str(j))
                image = loadImageCT(path+folder[i]+"/"+str(j)+".jpg")
                dominant = image.get_color(quality=1) #1 is highest quality
                palette = image.get_palette(color_count=6, quality=1) #return list of tuples in form (r,g,b)

                d = str(dominant[0])+','+str(dominant[1])+','+str(dominant[2])
                
                c1 = str(palette[0][0])+','+str(palette[0][1])+','+str(palette[0][2])
                c2 = str(palette[1][0])+','+str(palette[1][1])+','+str(palette[1][2])
                c3 = str(palette[2][0])+','+str(palette[2][1])+','+str(palette[2][2])
                c4 = str(palette[3][0])+','+str(palette[3][1])+','+str(palette[3][2])
                c5 = str(palette[4][0])+','+str(palette[4][1])+','+str(palette[4][2])
                c6 = str(palette[5][0])+','+str(palette[5][1])+','+str(palette[5][2])


                f.write('{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(d,c1,c2,c3,c4,c5,c6,folder[i]))


def outputSingle(species=0, butterfly=1, testFolder=False, customImage=''):
    '''
    Creates Image object needed for prediction alghoritm.

    Output is Image object.
    '''

    #Image object init
    outputData = Image()

    if not customImage:    
        if testFolder is False:
            path = "Images/"
        else:
            path = "Images/Testing images/"

        folder = ["americanSnout", "blueMorpho", "gardenTigerMoth", "goliathBirdwing"]

        image = loadImageCT(path+folder[species]+"/"+str(butterfly)+".jpg")
    else:
        image = loadImageCT(customImage)
    print("Image loaded")

    dominant = image.get_color(quality=1) #1 is highest quality
    print("Got dominant")
    palette = image.get_palette(color_count=6, quality=1) #return list of tuples in form (r,g,b)
    print("Got palette")

    d = str(dominant[0])+','+str(dominant[1])+','+str(dominant[2])
    print("d")
    c1 = str(palette[0][0])+','+str(palette[0][1])+','+str(palette[0][2])
    print("c1")
    c2 = str(palette[1][0])+','+str(palette[1][1])+','+str(palette[1][2])
    print("c2")
    c3 = str(palette[2][0])+','+str(palette[2][1])+','+str(palette[2][2])
    print("c3")
    c4 = str(palette[3][0])+','+str(palette[3][1])+','+str(palette[3][2])
    print("c4")
    c5 = str(palette[4][0])+','+str(palette[4][1])+','+str(palette[4][2])
    print("c5")
    c6 = str(palette[5][0])+','+str(palette[5][1])+','+str(palette[5][2])
    print("c6")

    print(d,c1,c2,c3,c4,c5,c6,folder[species])

    outputData.rd = dominant[0]
    outputData.gd = dominant[1]
    outputData.bd = dominant[2]
    outputData.r1 = palette[0][0]
    outputData.g1 = palette[0][1]
    outputData.b1 = palette[0][2]
    outputData.r2 = palette[1][0]
    outputData.g2 = palette[1][1]
    outputData.b2 = palette[1][2]
    outputData.r3 = palette[2][0]
    outputData.g3 = palette[2][1]
    outputData.b3 = palette[2][2]
    outputData.r4 = palette[3][0]
    outputData.g4 = palette[3][1]
    outputData.b4 = palette[3][2]
    outputData.r5 = palette[4][0]
    outputData.g5 = palette[4][1]
    outputData.b5 = palette[4][2]
    outputData.r6 = palette[5][0]
    outputData.g6 = palette[5][1]
    outputData.b6 = palette[5][2]
    outputData.name = folder[species]

    print("output ready")
    return outputData
