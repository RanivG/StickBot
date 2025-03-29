import os
import time
from PIL import Image


def crop(l,w, im) -> Image:
    if True:
        print("pp")
    elif (l > w):
        print("cropping top and bottom to fit...")
        newL = l/2
        newbox = (0, newL-160, w, newL + 160)
        re_sized = im.resize((320,320) , box= newbox)
    elif (w > l):
        print("cropping left and right to fit...")
        newW = w/2
        newbox = (newW-160, 0, newW+160, l)
        re_sized = im.resize((320,320) , box= newbox)
    return re_sized

def square(l,w,im) -> Image:
    if l == w:
        resize = im
    elif l > w:
        barSize = ((l-w)//2, l)
    elif w > l:
        barSize = (w, (w-l)//2)

infile = input("Please input the file path of the image you would like to edit: \n")
outfile = input("Please input the name you would like to use for the edited image (include path for saving to different folder): \n")
inName, sourceExt = os.path.splitext(infile)
outName, destExt = os.path.splitext(outfile)

while(outfile==infile):
    print("Error! Input file and output file are the same! Please change one of the 2:\n ")
    a = input("new input file name(hit enter instead of re-pasting old name): \n")
    if(a != ''):
        infile = a
    b = input("new output file name(hit enter instead of re-pasting old name):\n")
    if(b != ''):
        outfile = b


try: 
    with Image.open(infile) as im:
        w,l = im.size
        if(l == 320) and (w==320):
            print("perfect!")
            re_sized = im
        else:
            op = input(f"Error! File dimensions are {l}x{w} and do not match the required dimensions. Would you like to Crop?(Y/n): \n")
            if op == "Y":
                re_sized = crop(l, w, im)
            else:
                op = input("Would you like to squash the image to fit (1) or make it square before converting? : \n")
                if op == "1":
                    re_sized = im.resize((320,320))
                else:
                    re_sized = square(l,w,im)

        re_sized.save(outfile , "PNG")
        print("Success! Here is your new file: ")
        time.sleep(2)
        re_sized.show()

        #print("if the crop is bad, type up to move the window up, down to move window down, l to move window left and r to move window right")




except OSError:
    print(f"Conversion of file {infile} to {outfile} failed")