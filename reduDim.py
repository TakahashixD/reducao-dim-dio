import cv2

imagem_colorida = cv2.imread("cavalo.jpg")

imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)
cv2.imwrite("cavalo_cinza.jpg", imagem_cinza)  

limiar = 140
_, imagem_binaria = cv2.threshold(imagem_cinza, limiar, 255, cv2.THRESH_BINARY)
cv2.imwrite("cavalo_binario.jpg", imagem_binaria)  

# Exibir as imagens
cv2.imshow("Imagem Cinza", imagem_cinza)
cv2.imshow("Imagem Binarizada", imagem_binaria)
cv2.waitKey(0) 
cv2.destroyAllWindows()