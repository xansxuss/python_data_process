import os, json,cv2,shutil
from lxml import etree
import xml.etree.cElementTree as ET
import argparse
from PIL import Image, ImageOps
import numpy as np


def get_file(path):
    file_list=os.listdir(path)
    return file_list

def read_img(img_path):
    img=cv2.imread(img_path)
    return img

def toxml(path,file_name,label,bbox,img_shape,foldern):
    xml=os.path.join(path,'labels','{}.xml'.format(file_name))
    imgn=os.path.join(path,'{}.jpg'.format(file_name))
    if not os.path.isfile(xml):
        with open(xml,'w')as f:
            f.write("<annotation verified=\"yes\">")
            f.write("</annotation>")
        f.close
    tree=ET.parse(xml)
    root=tree.getroot()
    
    folder=ET.SubElement(root,"folder")
    folder.text=str(foldern)

    filename=ET.SubElement(root,"filename")
    filename.text=str('{}.jpg'.format(file_name))
    filepath=ET.SubElement(root,"path")
    filepath.text=str(imgn)
    
    source=ET.SubElement(root,"source")
    database=ET.SubElement(source,"database")
    database.text="Unknown"
    
    size=ET.SubElement(root,"size")
    width=ET.SubElement(size,'width')
    width.text=str(img_shape[1])
    height=ET.SubElement(size,'height')
    height.text=str(img_shape[0])
    depth=ET.SubElement(size,'depth')
    depth.text=str(img_shape[2])

    segmented=ET.SubElement(root,'segmented')
    segmented.text='0'

    object=ET.SubElement(root,'object')
    for i in range(len(label)):
        label_name=ET.SubElement(object,"name")
        label_name.text=str(label[i])
        pose=ET.SubElement(object,"pose")
        pose.text="Unspecified"
        truncated=ET.SubElement(object,"truncated")
        truncated.text="0"
        difficult=ET.SubElement(object,"difficult")
        difficult.text="0"
        bndbox=ET.SubElement(object,"bndbox")
        xmin=ET.SubElement(bndbox,"xmin")
        xmin.text=str(bbox[0])
        ymin=ET.SubElement(bndbox,"ymin")
        ymin.text=str(bbox[1])
        xmax=ET.SubElement(bndbox,"xmax")
        xmax.text=str(bbox[0]+bbox[2])
        ymax=ET.SubElement(bndbox,"ymax")
        ymax.text=str(bbox[1]+bbox[3])
    tree.write(xml)



def convert(path,label_path,img_path,name_list,folder):
    file_NG=[]
    with open(label_path,'r',encoding='utf-8') as f :
        f= json.load(f)
    for i in range(len(name_list)):
        print(name_list[i])
        img=read_img(os.path.join(img_path,name_list[i]))
        img_h,img_w,img_d=img.shape
        print(img_w,img_h)
        name=name_list[i].split('.')[0]
        # print('name:{}'.format(name),f[name]["bboxes"])
        label=[]
        
        for index in range(len(f[name]["bboxes"])):
            if f[name]["labels"][index] == 'no_gesture':
                continue
                # file_NG.append(name)
            else:
                label.append(f[name]["labels"][index])
                print(f[name]["labels"][index])
                x,y,w,h=f[name]["bboxes"][index]
                x = int(x * img_w)
                y = int(y * img_h)
                w = int(w* img_w)
                h = int(h *img_h)
        
        toxml(name,label,[x,y,w,h],img.shape,args.output_path)
    print(file_NG)
        
    #             img = cv2.rectangle(img,(int(x),int(y)),(int(w),int(h)),(0,0,255),3)
    #             image=cv2.putText(img,f[name]["labels"][index],(int(x),int(y)),cv2.FONT_HERSHEY_SIMPLEX,1,(100,100,100),2)
    #             image = cv2.circle(image,(x,y),5, (0, 0, 0), 5)
    #             image = cv2.circle(image,(w,h),5, (0, 255, 0), 5)
    #             cv2.imshow('test',image)
    #             cv2.waitKey()
    # cv2.destroyAllWindows()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--json_path',default='./')
    parser.add_argument('--img_path')
    parser.add_argument('--output_path')
    args=parser.parse_args()
    if not os.path.exists(args.output_path):
        os.mkdir(args.output_path)
    else:
        for i in os.listdir(args.output_path):
            os.remove(os.path.join(args.output_path,i))
    img_list=get_file(args.img_path)
    convert(args.json_path,args.img_path,img_list)
    # toxml('3d3d0c3f-bff1-4720-bb7a-4c580be616cb',["stop"],[5305616,48369474,7010857,8303638],(1920,1440,3),args.output_path)


    
    
    

