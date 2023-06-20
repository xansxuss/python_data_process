import cv2,os
from retinaface import RetinaFace
from file_operate import move_f


detector = RetinaFace(quality="normal")



def get_flie(path):
    img_path=[]
    img_path=os.listdir(path)
    return img_path



def single_img(img_path):
    img_bgr = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    detections = detector.predict(img_rgb)
    # print(detections)
    return detections

def single_img_in(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    detections = detector.predict(img_rgb)
    # print(detections)
    return detections


# def multi_img(img_path):
#     img_list=get_flie(img_path)
#     for i in range(len(img_list)):
#         img_name=os.path.join(img_path,img_list[i])
#         img_bgr = cv2.imread(img_name, cv2.IMREAD_COLOR)
#         img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
#         detections = detector.predict(img_rgb)
#         # print(detections)
#         return detections




axis=['x1','y1','x2','y2']
label = 'head'
if __name__ == "__main__":
    l=[]
    img_path = '/home/xanxus/Desktop/data_process/unzip/peace'
    img_list=get_flie(img_path)
    for i in range(len(img_list)):
        p=os.path.join(img_path,img_list[i])
        data=single_img(p)
        if data :
            print(data)
        else:
            l.append(img_list[i])
            move_f(img_list[i].split('.')[0],'jpg',img_path,'/home/xanxus/Desktop/HaGRID_data/NO/peace')
    print(l)






# single image
# img_path = '/home/xanxus/Downloads/HaGRID_data/train_val_stop/0a0f01f4-eda5-4679-82ba-94a4659e1d6e.jpg'
# img_bgr = cv2.imread(img_path, cv2.IMREAD_COLOR)
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# detections = detector.predict(img_rgb)
# print(detections)

# img_result = detector.draw(img_rgb, detections)
# img = cv2.cvtColor(img_result, cv2.COLOR_RGB2BGR)
# cv2.imshow("windows", img)
# key = cv2.waitKey()
# if key == ord("q"):
#    print("exit")
# cv2.destroyWindow("windows")




# multi image

# path = '/home/xanxus/Desktop/data_process/unzip/fist'
# img_list=get_flie(path)

# for i in range(len(img_list)):
#     img_name=os.path.join(path,img_list[i])
#     img_bgr = cv2.imread(img_name, cv2.IMREAD_COLOR)
#     img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
#     detections = detector.predict(img_rgb)
#     print(detections)
#     img_result = detector.draw(img_rgb, detections)
#     img = cv2.cvtColor(img_result, cv2.COLOR_RGB2BGR)
#     cv2.namedWindow("windows",cv2.WINDOW_NORMAL)
#     cv2.resizeWindow("windows",1000,1000)
#     cv2.imshow("windows", img)
#     cv2.waitKey(0) & 0xFF == ord('q')
# cv2.destroyWindow("windows")