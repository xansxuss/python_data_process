import os, cv2,math,random,argparse,shutil
import numpy as np
from skimage.util import random_noise
import file_operate as fo
import xml_operate as xo
import draw_xml as dxi
import img_open as io

# class DataAugmentForObjectDetection():
    # def __init__(self, rotation_rate=0.5, max_rotation_angle=5, 
    #             crop_rate=0.5, shift_rate=0.5, change_light_rate=0.5,
    #             add_noise_rate=0.5, flip_rate=0.5, 
    #             erase_rate=0.5, erase_length=50, erase_holes=1, erase_threshold=0.5):
    #     self.rotation_rate = rotation_rate
    #     self.max_rotation_angle = max_rotation_angle
    #     self.crop_rate = crop_rate
    #     self.shift_rate = shift_rate
    #     self.change_light_rate = change_light_rate
    #     self.add_noise_rate = add_noise_rate
    #     self.flip_rate = flip_rate
    #     self.erase_rate = erase_rate
    #     self.erase_length = erase_length
    #     self.erase_holes = erase_holes
    #     self.erase_threshold = erase_threshold

    # add noise
def addnoisse(img,mean=0,sigma=0.1):
    # def addnoisse(self,img,mean=0,sigma=0.1):
        origin_img = img
        # 圖片歸一化，且轉換為浮點型
        img=img.astype(np.float32)
        img=img/255.0
        noise=np.random.normal(mean,sigma,img.shape)
        gaussian_out=img+noise
        gaussian_img = np.uint8(gaussian_out*255)

        return gaussian_img
    # adjust lightness
def changeLight(img,lightness):
    # def changeLight(self,img,lightness):
    origin_img = img
        # 圖片歸一化，且轉換為浮點型
    img=img.astype(np.float32)
    img=img/255.0
        # 顏色空間轉換 BGR -> HLS
    hlsimg=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
    hlscopy=np.copy(hlsimg)
        # 亮度調整
    hlscopy[:, :, 1] = (1 + lightness / 100.0) * hlscopy[:, :, 1]
    hlscopy[:, :, 1][hlscopy[:, :, 1] > 1] = 1  # 應該要介於 0~1，計算出來超過1 = 1

        # 顏色空間反轉換 HLS -> BGR 
    result_img = cv2.cvtColor(hlscopy, cv2.COLOR_HLS2BGR)
    changeLight_img = ((result_img * 255).astype(np.uint8))

    return changeLight_img
def changesaturation(img,saturation):
    # def changesaturation(self,img,saturation):
        orin_img=img
        # 圖片歸一化，且轉換為浮點型
        fimg=img.astype(np.float32)
        fimg=fimg/255.0
        # 顏色空間轉換 BGR -> HLS
        hlsimg=cv2.cvtColor(fimg,cv2.COLOR_BGR2HLS)
        hlscopy=np.copy(hlsimg)
        # 飽和度調整
        hlscopy[:, :, 2] = (1 + saturation / 100.0) * hlscopy[:, :, 2]
        hlscopy[:, :, 2][hlscopy[:, :, 2] > 1] = 1  # 應該要介於 0~1，計算出來超過1 = 1
         # 顏色空間反轉換 HLS -> BGR 
        result_img = cv2.cvtColor(hlscopy, cv2.COLOR_HLS2BGR)
        change_saturation = ((result_img * 255).astype(np.uint8))
        return change_saturation
    # crop img
def crop_img_bboxes(img, bboxes):
    # def crop_img_bboxes(self, img, bboxes):
        # 剪裁圖片
        width = img.shape[1]
        height = img.shape[0]
        x_min = width  
        x_max = 0
        y_min = height
        y_max = 0
        for bbox in bboxes:
            x_min = min(x_min, int(bbox[0]))
            y_min = min(y_min, int(bbox[1]))
            x_max = max(x_max, int(bbox[2]))
            y_max = max(y_max, int(bbox[3]))
        d_to_left = x_min             # 所有目标框的最小框到左邊的距離
        d_to_right = width - x_max    # 所有目标框的最小框到右邊的距離
        d_to_top = y_min              # 所有目标框的最小框到顶端的距離
        d_to_bottom = height - y_max  # 所有目标框的最小框到底部的距離
        # 取得隨機剪裁大小
        crop_x_min = int(x_min - random.uniform(0, d_to_left))
        crop_y_min = int(y_min - random.uniform(0, d_to_top))
        crop_x_max = int(x_max + random.uniform(0, d_to_right))
        crop_y_max = int(y_max + random.uniform(0, d_to_bottom))
        # 確保不越界
        crop_x_min = max(0, crop_x_min)
        crop_y_min = max(0, crop_y_min)
        crop_x_max = min(width, crop_x_max)
        crop_y_max = min(height, crop_y_max)
        # 另存剪裁後圖片
        crop_img = img[crop_y_min:crop_y_max, crop_x_min:crop_x_max]

        # 剪裁後bbonx
        crop_bboxes = list()
        for bbox in bboxes:
            crop_bboxes.append([int(bbox[0])-crop_x_min, int(bbox[1])-crop_y_min, int(bbox[2])-crop_x_min, int(bbox[3])-crop_y_min])
        return crop_img, crop_bboxes
    #  shift
def shift_pic_bboxes(img, bboxes):
    # def shift_pic_bboxes(self, img, bboxes):
        #---------------------- 平移圖片 ---------------------------
        width = img.shape[1]
        height = img.shape[0]
        x_min = width  
        x_max = 0
        y_min = height
        y_max = 0
        for bbox in bboxes:
            x_min = min(x_min, int(bbox[0]))  # bbox的x最小值小於width，x最大值大於0
            y_min = min(y_min, int(bbox[1]))
            x_max = max(x_max, int(bbox[2]))  
            y_max = max(y_max, int(bbox[3]))
        # x_min是所有目标框的x的最小值，y_min是所有目标框的y的最小值
        # x_max是所有目标框的x的最大值，y_max是所有目标框的y的最大值
        d_to_left = x_min             # 包含所有目标框的最大左移動距離
        d_to_right = width - x_max    # 包含所有目标框的最大右移動距離
        d_to_top = y_min              # 包含所有目标框的最大上移動距離
        d_to_bottom = height - y_max  # 包含所有目标框的最大下移動距離

        x = random.uniform(-(d_to_left-1) / 3, (d_to_right-1) / 3)
        y = random.uniform(-(d_to_top-1) / 3, (d_to_bottom-1) / 3)
        # x為向左或向右移動的像素值,正為向右,負為向左; 
        # y為向上或向下移動的像素值,正為向下,負為向上
        M = np.float32([[1, 0, x], [0, 1, y]]) 
        shift_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

        #---------------------- 平移BBox ----------------------
        shift_bboxes = list()
        for bbox in bboxes:
            shift_bboxes.append([int(bbox[0])+x, int(bbox[1])+y, int(bbox[2])+x, int(bbox[3])+y])

        return shift_img, shift_bboxes
def rotate_img_bbox(img, bboxes, angle=1, scale=1.):
    # def rotate_img_bbox(self, img, bboxes, angle=1, scale=1.):
        # 旋轉圖片
        width = img.shape[1]
        height = img.shape[0]
        # 角度邊弧度
        rangle = np.deg2rad(angle)
        # 計算新圖片寬與高分別為最高與最低點的垂直距離
        nw = (abs(np.sin(rangle)*height) + abs(np.cos(rangle)*width))*scale
        nh = (abs(np.cos(rangle)*height) + abs(np.sin(rangle)*width))*scale
        # getRotationMatrix2D(Point2f center, double angle, double scale)
                        # Point2f center：表示旋转的中心點
                        # double angle：表示旋轉的角度
                        # double scale：圖片縮放比例
                        #参考：https://www.geeksforgeeks.org/python-opencv-getrotationmatrix2d-function/ https://docs.opencv.org/3.4/da/d54/group__imgproc__transform.html#gafbbc470ce83812914a70abfb604f4326
        rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, scale)
        # 新中心與舊中心之間的距離
        rot_move = np.dot(rot_mat, np.array([(nw-width)*0.5, (nh-height)*0.5, 0]))
        rot_mat[0,2] += rot_move[0]
        rot_mat[1,2] += rot_move[1]
        # 仿射轉換
        rot_img = cv2.warpAffine(img, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4) # ceil向上取整
        # bbox坐標轉換
        # rot_mat是最後旋轉矩阵
        # 取得原始bbox的四個點，然后将这四個點轉換到旋轉後的坐標系下
        rot_bboxes = list()
        for bbox in bboxes:
            xmin = int(bbox[0])
            ymin = int(bbox[1])
            xmax = int(bbox[2])
            ymax = int(bbox[3])
            point1 = np.dot(rot_mat, np.array([(xmin+xmax)/2, ymin, 1]))
            point2 = np.dot(rot_mat, np.array([xmax, (ymin+ymax)/2, 1]))
            point3 = np.dot(rot_mat, np.array([(xmin+xmax)/2, ymax, 1]))
            point4 = np.dot(rot_mat, np.array([xmin, (ymin+ymax)/2, 1]))
            # 合並np.array
            concat = np.vstack((point1, point2, point3, point4))
            # 改變array type
            concat = concat.astype(np.int32)
            # 得到旋转后的坐標
            rx, ry, rw, rh = cv2.boundingRect(concat)
            rx_min = rx
            ry_min = ry
            rx_max = rx+rw
            ry_max = ry+rh
            # 加入list中
            rot_bboxes.append([rx_min, ry_min, rx_max, ry_max])

        return rot_img, rot_bboxes



def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--data_path",help="data path")
    parser.add_argument("--save_path",help="output save path")
    parser.add_argument("--flag",help="option flag",default='label')
    parser.add_argument("--folder",help="multi folder",nargs='+')
    known_args, _ = parser.parse_known_args()
    return known_args

if __name__ == "__main__":
    args=parse_arguments()

    for folder in args.folder:
        img_path=os.path.join(args.data_path,folder,'imgs')
        label_path=os.path.join(args.data_path,folder,'labels')
        img_list=fo.get_file(img_path)
        for name in img_list:
            orin_img=cv2.imread(os.path.join(img_path,'{}.jpg'.format(name)))
            for i in range(60,100,10):
                light_img=changeLight(orin_img,lightness=-i)
                save_img_path=os.path.join(args.save_path,'{}_light_{}'.format(folder,i),'imgs')
                save_label_path=os.path.join(args.save_path,'{}_light_{}'.format(folder,i),'labels')
                fo.check_path(save_img_path)
                fo.check_path(save_label_path)
                cv2.imwrite(os.path.join(save_img_path,'{}_light_{}.jpg'.format(name,i)),light_img)
                fo.copy_f(os.path.join(label_path,'{}.xml'.format(name)),os.path.join(save_label_path,'{}_light_{}.xml'.format(name,i)))
    #         #     io.show_img('light_img_{}:{}'.format(i,name),light_img)
    #         #     saturation_img=changesaturation(orin_img,saturation=-i)
    #         #     io.show_img('saturation_img_{}:{}'.format(i,name),saturation_img)
    #         label=xo.get_label(label_path,name)
    #         axises=xo.get_axis(label_path,name)
    #         shift_img,shift_bboxes=shift_pic_bboxes(orin_img,axises)
    #         print(name,shift_bboxes)
            
    #         crop_img,crop_bboxes=crop_img_bboxes(orin_img,axises)
    #         print(name,crop_bboxes)
    # path = '/home/xanxus/Desktop/HaGRID_data/raw_data/palm/JPEGImages/'
    # name='0d88827e-f724-431b-aa75-186d51ee2485'
    # orin_img=cv2.imread(os.path.join(path,'{}.jpg'.format(name)))
    # for i in range(60,100,10):
    #     light_img=changeLight(orin_img,lightness=-i)
    #     # io.show_img('light_img_{}:{}'.format(i,name),light_img)
    #     cv2.imwrite(os.path.join('/home/xanxus/Desktop/test','{}_light{}.jpg'.format(name,i)),light_img)
    # for i in range(30,60,10):
    #     saturation_img=changesaturation(orin_img,saturation=-i)
    #     # io.show_img('saturation_img_{}:{}'.format(i,name),saturation_img
    #     cv2.imwrite(os.path.join('/home/xanxus/Desktop/test','{}_saturation{}.jpg'.format(name,i)),saturation_img)