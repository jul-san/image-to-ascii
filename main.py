import time
from PIL import Image

# creates a variable to open the imgae the user chooses to
image = Image.open('./gudetama.jpeg')

#obtains the length and width of the image (in pixels)
w, h = image.size

# loads the image
pix = image.load();

# outer for-loop represents the height
for x in range(h):

    # nested for loop represents the width
    for y in range(w):

        # obtains the RGB values for each of the pixels
        r, g, b = pix[y, x]

        # conditionals will print a certain character based on the RGB value
        if r >= 238:
            print("@",end="")
        elif r >= 221:
            print("X",end="")
        elif r >= 204:
            print("=",end="")
        elif r >= 187:
            print("Q",end="")
        elif r >= 170:
            print("A",end="")
        elif r >= 153:
            print("%",end="")
        elif r >= 136:
            print("#",end="")
        elif r >= 119:
            print("&",end="")
        elif r >= 102:
            print("$",end="")
        elif r >= 85:
            print("8",end="")
        elif r >= 68:
            print("+",end="")
        elif r >= 51:
            print("%",end="")
        elif r >= 34:
            print("*",end="")
        elif r >= 17:
            print("Z",end="")
        else:
            print("E",end="")


    print()
    time.sleep(0.005)

