import os ,argparse,cv2
import xml.etree.cElementTree as ET
from file_operate import get_file,check_path






def img_resize(src_img,dst_size,name,out_path):
    src_h,src_w=src_img.shape[:2]
    dst_h,dst_w=dst_size

    h = dst_w*(float(src_h)/src_w)
    w = dst_h*(float(src_w)/src_h)
    # print('w:{},h:{},(src_h)/src_w:{},(src_w)/src_h:{}'.format(w,h,float(src_h)/src_w,float(src_w)/src_h))
    if h <= dst_h:
        img_dst=cv2.resize(src_img,(dst_w,int(h)))
    else:
        img_dst=cv2.resize(src_img,(int(w),dst_h))

    out_h,out_w=img_dst.shape[:2]

    top = int((dst_h - out_h) / 2)
    down = int((dst_h - out_h+1) / 2)
    left = int((dst_w - out_w) / 2)
    right = int((dst_w - out_w+1) / 2)

    value = [0,0,0]
    borderType = cv2.BORDER_CONSTANT
    img_dst = cv2.copyMakeBorder(img_dst, top, down, left, right, borderType, None, value)
    cv2.imwrite(os.path.join(out_path,'{}.jpg'.format(name)),img_dst)
    return img_dst

def bbox_resize(bbox,src_size,dst_size):
    bbox_o=[]
    src_h,src_w=src_size
    dst_h,dst_w=dst_size
    scale =min(dst_w/src_w,dst_h/src_h)
    nw = int(src_w * scale)
    nh = int(src_h * scale)
    dx=(dst_w - nw) / 2
    dy=(dst_h - nh) / 2

    for i in bbox:
        xmin=int(int(i[0]) * (nw/src_w) + dx)
        ymin=int(int(i[1]) * (nh/src_h) + dy)
        xmax=int(int(i[2]) * (nw/src_w) + dx)
        ymax=int(int(i[3]) * (nh/src_h) + dy)
        bbox_o.append([xmin,ymin,xmax,ymax])
        
    return bbox_o


def read_xml(xml_path):
    etree=ET.parse(xml_path)
    root=etree.getroot()
    box=[]
    for obj in root.iter('object'):
        
        xmin,ymin,xmax,ymax=(x.text for x in obj.find('bndbox'))
        box.append([xmin,ymin,xmax,ymax])
    return box
def write_xml(label_list, file_name,dst_size,save_path):
    name = os.path.join(args.label_path,'{}.xml'.format(file_name))
    etree=ET.parse(name)
    root = etree.getroot()
    for obj in root.iter('size'):
        obj.find('height').text = str(dst_size[0])
        obj.find('width').text = str(dst_size[1])
    for obj, bo in zip(root.iter('object'),label_list):
        for index,x in enumerate(obj.find('bndbox')):
            x.text = str(bo[index])
    etree.write(os.path.join(save_path,'{}.xml'.format(file_name)))

    return

def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--img_path",help="image dataset path")
    parser.add_argument("--label_path",help="label path")
    parser.add_argument("--save_xml",help="output save path")
    parser.add_argument("--save_img",help="output save path")
    parser.add_argument("--scale")
    known_args, _ = parser.parse_known_args()
    return known_args

if __name__ == "__main__":
    args=parse_arguments()
    # check_path(args.save_img)
    # check_path(args.save_xml)
    # dst_size = (int(args.scale),int(args.scale))
    # file_list = get_file(args.label_path)
    # for fl in file_list:
    #     src_img=cv2.imread(os.path.join(args.img_path,'{}.jpg'.format(fl)))
    #     src_size=src_img.shape[:2]
    #     print(src_size)
    #     img_dst=img_resize(src_img,dst_size,fl,args.save_img)
    #     bbox = read_xml(os.path.join(args.label_path,'{}.xml'.format(fl)))
    #     bbox = bbox_resize(bbox,src_size,dst_size)
    #     write_xml(bbox,fl,dst_size,args.save_xml)

    for floder in args.folder:
        img_path=os.path.join(args.data_path,floder,'imgs')
        label_path=os.path.join(args.data_path,floder,'labels')
        save_img=os.path.join(args.save_path,floder,'imgs')
        save_label=os.path.join(args.save_path,floder,'labels')
        check_path(save_img)
        check_path(save_label)
        dst_size = (int(args.scale),int(args.scale))
        file_list=get_file(label_path)
        for fl in file_list:
            src_img=cv2.imread(os.path.join(img_path,'{}.jpg'.format(fl)))
            src_size=src_img.shape[:2]
            print(src_size)
            img_dst=img_resize(src_img,dst_size,fl,save_img)
            bbox = read_xml(os.path.join(label_path,'{}.xml'.format(fl)))
            bbox = bbox_resize(bbox,src_size,dst_size)
            write_xml(label_path,bbox,fl,dst_size,save_label)


# img_path ='./data/image/train_val_palm/0a1cbe0d-ce68-4228-8a08-9a9a54c59713.jpg'
# xml_path ='./data/label/anno_xml_palm/0a1cbe0d-ce68-4228-8a08-9a9a54c59713.xml'
# save_path='./data/123/1/4'
# img_src = cv2.imread(img_path)
# src_size = img_src.shape[:2]
# dst_size=(512,512)

# img_dst=img_resize(img_src,dst_size)
# print(img_dst.shape)


# bbox = read_xml(xml_path)
# print('old:{}'.format(bbox))
# bbox = bbox_resize(bbox,src_size,dst_size)
# print(bbox)
# write_xml(bbox,xml_path,dst_size,save_path)

# for l in bbox:
#     img_dst=cv2.rectangle(img_dst,(l[0],l[1]),(l[2],l[3]),(255,255,255),1)



# cv2.imshow('test',img_dst)
# if 27 == cv2.waitKey():
#     cv2.destroyAllWindows()
# for root,dirs,files in os.walk(save_path):
#     print(root)
    # for fname in files:
	#     print(os.path.join(root, fname))

# def check_path(path):
#     if not os.path.isdir(path):
#        os.makedirs(path) 
