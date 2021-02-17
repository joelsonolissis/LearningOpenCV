import numpy as np
import cv2
def showImage(img):
    from matplotlib import pyplot as plt

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def main():
    obj_img = cv2.imread("img/joe.jfif")
    altura, largura, canais_de_cor = obj_img.shape
    print("Dimensoes da Imagem " + str(largura) + "," + str(altura))
    print("Canais de cor: ", canais_de_cor)
    showImage(obj_img)

main()
