import os, json,cv2,shutil
from lxml import etree
import xml.etree.cElementTree as ET
import argparse
from file_operate import get_file
from xml_operate import add_label,create_xml


# def get_file(path):
#     file_list=os.listdir(path)
#     return file_list

def read_img(img_path):
    img=cv2.imread(img_path)
    return img


def convert(path,folder,label_path,save_path,img_path,name_list):
    file_NG=[]
    with open(label_path,'r',encoding='utf-8') as f :
        f= json.load(f)
    for i in range(len(name_list)):
        print(name_list[i])
        img=read_img(os.path.join(img_path,'{}.jpg'.format(name_list[i])))
        img_h,img_w,img_d=img.shape
        # print(img_w,img_h)
        name=name_list[i].split('.')[0]
        # print('name:{}'.format(name),f[name]["bboxes"])
        xml_path=os.path.join(save_path,'{}.xml'.format(name))
        if not os.path.isfile(xml_path):
            create_xml(save_path,name,img.shape,folder)
        labels=[]
        axises=[]
        
        for index in range(len(f[name]["bboxes"])):
            if f[name]["labels"][index] == 'no_gesture':
                continue
                # file_NG.append(name)
            else:
                label=f[name]["labels"][index]
                # label.append(f[name]["labels"][index])
                # print(f[name]["labels"][index])
                x,y,w,h=f[name]["bboxes"][index]
                x = int(x * img_w)
                y = int(y * img_h)
                w = int(w* img_w)
                h = int(h *img_h)
                # axis.append(f[name]["bboxes"][index])
                # print(f[name]["bboxes"][index])
                add_label(save_path,name,label,[x,y,x+w,y+h])
    print(file_NG)
    
def parse_arguments() :
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path')
    parser.add_argument('--save_path')
    parser.add_argument('--json_path')
    parser.add_argument("--folder",help="multi folder",nargs='+')
    known_args, _ = parser.parse_known_args()
    return known_args

if __name__ == '__main__':

    args=parse_arguments()

    for folder in args.folder:
        if args.json_path:
            json_path = args.json_path
        else:
            json_path = os.path.join(args.data_path,'{}.json'.format(folder))
        if args.save_path:
            if not os.path.exists(args.save_path):
                os.mkdir(args.save_path)
            else:
                for i in os.listdir(save_path):
                    os.remove(os.path.join(save_path,i))
        else:
            save_path = os.path.join(args.data_path,folder,'labels')
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            else:
                for i in os.listdir(save_path):
                    os.remove(os.path.join(save_path,i))

            img_path=os.path.join(args.data_path,folder,'imgs')
            img_list=get_file(img_path)
            convert(args.data_path,folder,json_path,save_path,img_path,img_list)