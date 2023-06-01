from tensorflow import keras
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np


filename = 'test.png'

img = mpimg.imread(filename)[:,:,:3]
img = color.rgb2gray(img)
img = resize(img, (28, 28))

plt.figure()
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()


# prebaciti sliku u vektor odgovarajuce velicine
img = img.reshape(1,28*28)


# vrijednosti piksela kao float32 (bijela znamenka na crnoj pozadini) - po potrebi zakomentirajte ovisno kakva je input slika
img = 1 - img.astype('float32')


# TODO: ucitaj istreniranu neuronsku mrezu


# TODO: napravi predikciju 


# TODO: ispisi predikciju u terminal ili dodaj predikciju u title slike


