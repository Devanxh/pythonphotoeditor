from image import Image
import numpy as np

def brightness(image, factor):
    #if the factor is > 1 the image will be ligthened and if the factor < 1 the image will be darkened
    x_pixels, y_pixels, num_channels = image.array.shape
    # clone of og image so the og image will not be ruined
    new_image = Image(x_pixels=x_pixels, y_pixels=y_pixels,num_channels=num_channels)
    new_image.array = image.array*factor
    return new_image
    

if __name__ == '__main__':
    sky = Image(filename='sky1.png')
    brightened_im = brightness(sky,1.7)
    brightened_im.write_image('brd.png')
    #city = Image(filename='city.png')
