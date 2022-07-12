import cv2
import numpy as np

xI, yI, xF, yF = 0, 0, 0, 0
interruptor=False
img=cv2.imread('Qwe.jpeg')

def dibujar_rectangulo(event, x, y, flags, param):
    global xI, yI, xF, yF, interruptor
    if event == cv2.EVENT_LBUTTONDOWN:
        xI, yI = x, y
        interruptor=False
    elif event == cv2.EVENT_LBUTTONUP:
        xF, yF = x, y
        interruptor=True
        recorte=img[yI:yF,xI:xF]
        cv2.imwrite("recorte.jpg",recorte)
        # cv2.imshow('imagen',recorte)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


def recorte():
    # img=cv2.imread('Qwe.jpeg')
    cv2.namedWindow('display')
    cv2.setMouseCallback('display', dibujar_rectangulo)
    while True:
        img=cv2.imread('Qwe.jpeg')
        if interruptor==True:
            cv2.rectangle(img, (xI, yI), (xF, yF), (0, 0, 0), 2)
            # cv2.imshow('display', img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # break
        cv2.imshow('display', img)
        k=cv2.waitKey(1)&0xFF
        if k==27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    recorte()