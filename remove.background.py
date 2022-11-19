from rembg import remove
from PIL import Image

def remove_background(image_select):

    img = Image.open(image_select)
    img_without_back = remove(img)
    img_without_back.save('img_without_back.png')
    print('Sucess')