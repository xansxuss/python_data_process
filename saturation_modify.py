import os,cv2
import numpy as np


# 調整亮度
def modify_lightness(img):
    orin_img=img
    fimg=img.astype(np.float32)
    fimg=fimg/255.0

    hlsimg=cv2.cvtColor(fimg,cv2.COLOR_BGR2HLS)
    hlscopy=np.copy(hlsimg)

    lightness=-950
    hlscopy[:,:,1]=(1+lightness/1000.0)* hlscopy[:, :, 1]
    hlscopy[:, :, 1][hlscopy[:, :, 1] > 1] = 1

    rimg = cv2.cvtColor(hlscopy,cv2.COLOR_HLS2BGR)
    rimg=((rimg *255)).astype(np.uint8)
    return rimg

# 調整飽和度
def modify_saturation(img):

    orin_img=img
    fimg=img.astype(np.float32)
    fimg=fimg/255.0

    hlsimg=cv2.cvtColor(fimg,cv2.COLOR_BGR2HLS)
    hlscopy=np.copy(hlsimg)

    saturation=-1000
    hlscopy[:,:,2]=(1+saturation/1000.0)* hlscopy[:, :, 2]
    hlscopy[:, :, 2][hlscopy[:, :, 2] > 1] = 1

    rimg = cv2.cvtColor(hlscopy,cv2.COLOR_HLS2BGR)
    rimg=((rimg *255)).astype(np.uint8)
    return rimg


if __name__ == "__main__":
    path = '/home/xanxus/Desktop/Mask_face/imgs/1_Handshaking_Handshaking_1_254.jpg'

    img = cv2.imread(path)
    lightness_img = modify_lightness(img)
    cv2.imshow('orin',img)
    cv2.imshow('lightness',lightness_img)

    saturat_img = modify_saturation(img)
    # cv2.imshow('orin',img)
    cv2.imshow('saturation',saturat_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows