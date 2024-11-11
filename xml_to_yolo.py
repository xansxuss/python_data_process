import os,cv2,argparse,shutil
import file_operate as fo
import xml.etree.cElementTree as ET


def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--label_path",help="label path")
    parser.add_argument("--img_path",default='',help="img path")
    parser.add_argument("--folder",help="multi folder",nargs='+')
    parser.add_argument("--cls_path",default='',help="class file path")
    parser.add_argument("--flag",default='',help="select mode")
    known_args, _ = parser.parse_known_args()
    return known_args


if __name__ == "__main__":
    args=parse_arguments()
    cls_list = []
    with open(args.cls_path,'r') as cls_f:
        cls_list = cls_f.readlines()
    cls_f.close()
    cls_list = [item.replace('\n', '') for item in cls_list]
    print(cls_list)
    for folder in args.folder:
        xml_p=os.path.join(args.label_path,folder)

        

        label_list = fo.get_file(xml_p)
        for lname in label_list:
            print('name:{}'.format(lname),'\n')
            xml_name = os.path.join(args.label_path,folder,lname)
            data_list = [] 
            tree=ET.parse('{}.xml'.format(xml_name))
            root=tree.getroot()
            if root.findall('object') :
                for i in root.iter('object'):
                    label = i[0].text
                    xc = int(i.find('bndbox')[0].text) + ((int(i.find('bndbox')[2].text) - int(i.find('bndbox')[0].text)) / 2)
                    yc = int(i.find('bndbox')[1].text) + ((int(i.find('bndbox')[3].text) - int(i.find('bndbox')[1].text)) / 2)
                    w = (int(i.find('bndbox')[2].text) - int(i.find('bndbox')[0].text))
                    h = (int(i.find('bndbox')[3].text) - int(i.find('bndbox')[1].text))
                    print(label,xc,yc,w,h)
                    data_list.append([label,xc,yc,w,h])
            else:
                print("no find label")

            
            fo.check_path(os.path.join(args.label_path,'yolo'))
            lname_base = fo.get_base(lname)
            
            with open(os.path.join(args.label_path,'yolo','{}.txt'.format(lname_base)),'w') as yolo_f:
                for count in data_list:
                    # if count[0] in cls_list:
                    cls_index = cls_list.index(count[0])
                    print(cls_index)
                    print(count[1]/1920,count[2]/1080,count[3]/1920,count[4]/1080)
                    yolo_f.write('{} {:.5f} {:.5f} {:.5f} {:.5f}'.format(cls_index,count[1]/1920,count[2]/1080,count[3]/1920,count[4]/1080))
                    yolo_f.write('\n')
                yolo_f.close()