from PIL import Image

img = Image.open('emoji1.png')
img = img.rotate(-90)
img.save('rotated.png')