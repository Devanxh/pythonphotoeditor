from image import Image
import numpy as np

def brightness(image, factor):
    #if the factor is > 1 the image will be ligthened and if the factor < 1 the image will be darkened
    x_pixels, y_pixels, num_channels = image.array.shape
    # clone of og image so the og image will not be ruined
    new_image = Image(x_pixels=x_pixels, y_pixels=y_pixels,num_channels=num_channels)
    new_image.array = image.array*factor
    return new_image

# def combine_images(image1,image2):
#     x_pixels, y_pixels, num_channels = image1.array.shape
#     new_image = Image(x_pixels=x_pixels, y_pixels=y_pixels,num_channels=num_channels)
#     # for x in range(x_pixels):
#     #     for y in range(y_pixels):
#     #         for z in range()
#     new_image.array[x_pixels,y_pixels,num_channels]=(image1.array[x_pixels,y_pixels,num_channels]+image2.array[x_pixels,y_pixels,num_channels])**0.5
#     return new_image
    

if __name__ == '__main__':
    sky = Image(filename='sky1.png')
    # moto = Image(filename='moto.png')
    # brightened_im = brightness(sky,1.7)
    # brightened_im.write_image('brd.png')
    # combine_image = combine_images(sky,moto)
    # combine_image.write_image('nice.png')
