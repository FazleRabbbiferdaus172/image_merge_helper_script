from PIL import Image

def crop_windows_10(im):
    (left, upper, right, lower) = (80, 200, 1820, 1010)
    im = im.crop((left, upper, right, lower))
    return im

def crop_ubuntu(im):
    (left, upper, right, lower) = (500, 295, 1465, 915)
    im = im.crop((left, upper, right, lower))
    return im
