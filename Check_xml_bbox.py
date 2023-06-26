import xml.etree.ElementTree as ET
import os,shutil,argparse,shutil
from file_operate import move_f,check_path

# xml_folder_path = '/home/xanxus/Desktop/HaGRID_data/data/label/anno_xml_stop'
# img_folder_path = 'home/xanxus/Desktop/HaGRID_data/data/image/train_val_stop'
error_xml = set()


check_bbox = lambda x,Max: 0 > x or x > Max
def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--label_path",help="label path")
    parser.add_argument("--out_label_path",help="move label path")
    parser.add_argument("--img_path",help="image path")
    parser.add_argument("--out_img_path",help="move image path")
    known_args, _ = parser.parse_known_args()
    return known_args

arge=parse_arguments()

for xml in os.listdir(arge.label_path):
    # print(xml)
    if '.xml' in xml:
        xml = os.path.join(arge.label_path,xml)
        tree = ET.parse(xml)
        root = tree.getroot()
        width = int(root.find('size').find('width').text)
        height = int(root.find('size').find('height').text)
        for neighbor in root.iter('bndbox'):
            bbox_error = False
            xmin = int(neighbor.find('xmin').text)
            ymin = int(neighbor.find('ymin').text)
            xmax = int(neighbor.find('xmax').text)
            ymax = int(neighbor.find('ymax').text)
            if check_bbox(xmin, width) or check_bbox(ymin, height) or check_bbox(xmax, width) or check_bbox(ymax, height) or width == 0 or height == 0 :
                print('w:{},h:{},xmin:{},ymin:{},xmax:{},ymax:{}'.format(width,height,xmin,ymin,xmax,ymax))
                error_xml.add(xml)
print(error_xml)
print(len(error_xml))

name_list=[]
if arge.out_label_path :
    check_path(arge.out_label_path)
    check_path(arge.out_img_path)
    for i in error_xml:
        basename=os.path.basename(i)
        name=basename.split('.')[0]
        ex_name=basename.split('.')[1]
        move_f(name,ex_name,arge.label_path,arge.out_label_path)
        move_f(name,'jpg',arge.img_path,arge.out_img_path)

else:
    for i in error_xml:
        basename=os.path.basename(i)
        name=basename.split('.')[0]
        name_list.append(name)
        


