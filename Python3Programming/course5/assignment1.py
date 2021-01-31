import PIL
from PIL import Image, ImageDraw, ImageFont

# read image and convert to RGB
image = Image.open("cclogo.jpeg")
image = image.convert('RGBA')

# loop over pixels
def colorChange(color,percent,row):
    newIm = Image.new("RGBA",(image.width,int(image.height*1.1)))
    newIm.paste(image,(0,0))
    height = newIm.height
    width = newIm.width
    for x in range(width):
        for y in range(height):
            r = newIm.getpixel((x,y))[0]
            g = newIm.getpixel((x,y))[1]
            b = newIm.getpixel((x,y))[2]
            if color == "red":
                r = int(r * percent)
            if color == "green":
                g = int(g * percent)
            if color == "blue":
                b = int(b * percent)
            newIm.putpixel((x,y),(r,g,b))
    r = 255
    g = 255
    b = 255
    if color == "red":
        r = int(255 * percent)
    if color == "green":
        g = int(255 * percent)
    if color == "blue":
        b = int(255 * percent)
    txt = ImageDraw.Draw(newIm)
    font = ImageFont.truetype("/Users/docopeland/IdeaProjects/python-coursera/Python3Programming/course5/arial.ttf",15)
    txt.text((0,image.height),"channel {} intensity {}".format(row,percent),fill=(r,g,b),font=font)
    return newIm

images = []
for row in range(3):
    if row == 0:
        color = "red"
    if row == 1:
        color = "green"
    if row == 2:
        color = "blue"
    for col in range(3):
        if col == 0:
            img = colorChange(color,0.1,row)
        if col == 1:
            img = colorChange(color,0.5,row)
        if col == 2:
            img = colorChange(color,0.9,row)
        images.append(img)


# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.show()