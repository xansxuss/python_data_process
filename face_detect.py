import os,cv2,argparse,shutil
import xml.etree.cElementTree as ET
from Face_Detection import single_img_in
from file_operate import get_file,check_path
from xml_operate import add_label,create_xml

def face_detect(img):
    point=[]
    # img=cv2.imread(os.path.join(img_path,'{}{}'.format(name,'.jpg')))
    point_list=single_img_in(img)
    if point_list:
        # print(point_list)
        for l in range(len(point_list)):
            a=[]
            for i,(k,v) in enumerate(point_list[l].items()):
                # print(type(k),type(v))
                
                if k == 'x1':
                    a.append(v)
                elif k == 'y1':
                    a.append(v)
                elif k =='x2':
                    a.append(v)
                elif k == 'y2':
                    a.append(v)
                else:
                    continue
            # print(a)
            point.append(a)

    return point



def write_xml(file_name,xml_path,point):
    xml_content=[]
    label='head'
    name=os.path.join(xml_path,'{}{}'.format(file_name,'.xml'))
    tree=ET.parse(name)
    root=tree.getroot()

    new_object=ET.Element("object")
    new_name=ET.Element("name")
    new_name.text=label
    new_object.append(new_name)

    new_pose=ET.Element("pose")
    new_pose.text="Unspecified"
    new_object.append(new_pose)

    new_truncated=ET.Element("truncated")
    new_truncated.text='0'
    new_object.append(new_truncated)

    new_difficult=ET.Element("difficult")
    new_difficult.text='0'
    new_object.append(new_difficult)

    new_bndbox=ET.Element("bndbox")

    new_object.append(new_bndbox)

    new_xmin=ET.Element("xmin")
    new_xmin.text=str(point[0])
    new_bndbox.append(new_xmin)
    new_ymin=ET.Element("ymin")
    new_ymin.text=str(point[1])
    new_bndbox.append(new_ymin)
    new_xmax=ET.Element("xmax")
    new_xmax.text=str(point[2])
    new_bndbox.append(new_xmax)
    new_ymax=ET.Element("ymax")
    new_ymax.text=str(point[3])
    new_bndbox.append(new_ymax)

    root.append(new_object)
    tree.write(name)
    



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('--xml_path')
    # parser.add_argument('--img_path')
    parser.add_argument('--data_path')
    parser.add_argument('--save_path')
    parser.add_argument("--folder",help="multi folder",nargs='+')
    parser.add_argument('--ng_path',default='/home/xanxus/Desktop/368_data/ng')
    args=parser.parse_args()
    for folder in args.folder:
        print('do:{}'.format(folder))
        path=os.path.join(args.data_path,folder,'imgs')
        check_path(os.path.join(args.data_path,folder,'labels'))
        name_list=get_file(path)
        
        for i in range(len(name_list)):
            print('{}'.format(name_list[i]))
            img=cv2.imread(os.path.join(path,'{}{}'.format(name_list[i],'.jpg')))
            point=face_detect(img)
            if not os.path.isfile(os.path.join(args.data_path,folder,'labels','{}.xml'.format(name_list[i]))):
                create_xml(os.path.join(args.data_path,folder,'labels'),name_list[i],img.shape,folder)
        
            if point:
                for n in range(len(point)):
                    print(name_list[i])
                    add_label(os.path.join(args.data_path,folder,'labels'),name_list[i],'head',point[n])
                
            # else:
            #     print('\n{} no detect face\n'.format(name_list[i]))
            #     # shutil.move(os.path.join(args.img_path,'{}.jpg'.format(name_list[i])),args.ng_path)
            #     # shutil.move(os.path.join(args.xml_path,'{}.xml'.format(name_list[i])),args.ng_path)
