import numpy as np
import cv2
def showImage(img):
    from matplotlib import pyplot as plt

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Corrigir tons da imagem
    plt.imshow(img)
    plt.show()

def main():
    obj_img = cv2.imread("img/joe.jfif")
    # obj_img = cv2.imread("img/joe.jfif", 0) -> para a imagem aparecer a preto e branco
    altura, largura, canais_de_cor = obj_img.shape
    print("Dimensoes da Imagem " + str(largura) + "," + str(altura))
    print("Canais de cor: ", canais_de_cor)
    #Acessar pixels com fors
    for y in range(0,altura):
        for x in range(0, largura):
            print(obj_img[y][x])
    showImage(obj_img) #Função para mostrar a imagem

main()
