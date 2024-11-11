import os,cv2,argparse
import xml.etree.cElementTree as ET
from file_operate import check_path,get_file

def replace_label(path,name,label_str,l_list):
    xml_name = os.path.join(path,'{}.xml'.format(name))
    tree=ET.parse(xml_name)
    root=tree.getroot()
    for i in root.iter('object'):
        label = i[0].text
        if label != label_str and label not in l_list:
            i[0].text=label_str
            # print('name',name)
            # print('new',i[0].text)
        else:
            # print('pass')
            continue
        tree.write(os.path.join(path,'{}.xml'.format(name)))
        print('write {} in file'.format(name))

def delete_label(path,name,label_list):
    print(name)
    xml_name = os.path.join(path,'{}.xml'.format(name))
    tree=ET.parse(xml_name)
    root=tree.getroot()
    for object in root.findall('object'):
        label=object[0].text
        print(label_list)
        if label in label_list:
            root.remove(object)
    tree.write(xml_name)  

def add_label(path,name,label,axis):
    
    xml_name = os.path.join(path,'{}.xml'.format(name))
    # print(xml_name)
    tree=ET.parse(xml_name)
    root=tree.getroot()
    
    new_node=ET.Element("object")
    new_node_ch1=ET.SubElement(new_node,"name")
    new_node_ch1.text=str(label)
    new_node_ch2=ET.SubElement(new_node,"pose")
    new_node_ch2.text="Unspecified"
    new_node_ch3=ET.SubElement(new_node,"truncated")
    new_node_ch3.text="0"
    new_node_ch3=ET.SubElement(new_node,"difficult")
    new_node_ch3.text="0"
    new_node_ch4=ET.SubElement(new_node,"bndbox")
    bndbox_ch1=ET.SubElement(new_node_ch4,"xmin")
    bndbox_ch1.text=str(axis[0])
    bndbox_ch2=ET.SubElement(new_node_ch4,"ymin")
    bndbox_ch2.text=str(axis[1])
    bndbox_ch3=ET.SubElement(new_node_ch4,"xmax")
    bndbox_ch3.text=str(axis[2])
    bndbox_ch4=ET.SubElement(new_node_ch4,"ymax")
    bndbox_ch4.text=str(axis[3])

    root.append(new_node)
    tree.write(xml_name)
    
def get_label(path,name):
    label_list=[]
    xml_name = os.path.join(path,'{}.xml'.format(name))
    tree=ET.parse(xml_name)
    root=tree.getroot()
    if root.findall('object') :
        for i in root.iter('object'):
            label = i[0].text
            label_list.append(label)
        return label_list
    else:
        print(name)
        print("no find label")
        

def get_axis(path,name):
    axis=[]
    xml_name = os.path.join(path,'{}.xml'.format(name))
    tree=ET.parse(xml_name)
    root=tree.getroot()
    if root.findall('object') :
        for i in root.iter('object'):
            xmin,ymin,xmax,ymax=(x.text for x in i.find('bndbox'))
            axis.append([xmin,ymin,xmax,ymax])
    # else:
        # print(name)
        # print("no find label")
    return axis

def get_size(path,name): 
    size=[]
    xml_name = os.path.join(path,'{}.xml'.format(name))
    tree=ET.parse(xml_name)
    root=tree.getroot()
    if root.findall('size') :
        width,height,depth=(x.text for x in root.find('size'))
        size.append(width)
        size.append(height)
    # else:
        # print(name)
        # print("no find label")
    return size

def check_label(path,name):
    check_bbox = lambda x,Max: 0 > x or x > Max
    label=get_label(path,name)
    axis_list=get_axis(path,name)
    size_list=get_size(path,name)
    if label:
        for axis in axis_list:
            x_list=[axis[0],axis[2]]
            y_list=[axis[1],axis[3]]
            for i in range(2):
                # if check_bbox(int(x_list[i]),int(size_list[0])) or check_bbox(int(y_list[i]),int(size_list[1])) or int(axis[2]) - int(axis[0]) <= 5 or int(axis[3]) - int(axis[1]) <= 5 :
                if check_bbox(int(x_list[i]),int(size_list[0])) or check_bbox(int(y_list[i]),int(size_list[1])):
                    # error_xml.add(name)
                    return name
    else :
        print('{} No label'.format(name))  
    # print('fail:{}'.format(error_xml))
    
def create_xml(xml_path,file_name,img_shape,foldern):
    xml=os.path.join(xml_path,'{}.xml'.format(file_name))
    imgn=os.path.join(xml_path,'{}.jpg'.format(file_name))
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
    # root.append(root)
    tree.write(xml)

def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--label_path",help="label path")
    parser.add_argument("--img_path",help="img path")
    parser.add_argument("--data_path",help="data path")
    parser.add_argument("--folder",help="multi folder",nargs='+')
    parser.add_argument("--save_xml",help="output save path")
    parser.add_argument("--label_list",type=str,help="label_list",nargs='+')
    parser.add_argument("--axis_list",help="axis point",nargs='+')
    parser.add_argument("--label_change",help="change label str")
    parser.add_argument("--flag",help="option flag",default='label')
    known_args, _ = parser.parse_known_args()
    return known_args

if __name__ == "__main__":
    args=parse_arguments()

    print('mode:{}'.format(args.flag))
    if args.save_xml:
        check_path(args.save_xml)
    for folder in args.folder:
        print('do:{}'.format(folder))
        label_p=(os.path.join(args.data_path,folder,'labels'))
        img_p=(os.path.join(args.data_path,folder,'imgs'))
        name_list=get_file(label_p)
        label_dict={}
        error_lists = set()
        label_lists = set()
        no_label=set()
        for name in name_list:
            if args.flag == 'label':
                label_list=get_label(label_p,name)
                if label_list :
                    # print('{}:{},{}'.format(name,label_list,len(label_list)))
                    for label in label_list:
                        label_lists.add(label)
                else:
                    no_label.add(name)
            elif args.flag == 'add':
                for label,axises in zip(args.label_list,args.axis_list):
                    axis=axises.split(',')
                add_label(label_p,name,label,axis)
            elif args.flag == 'delete':
                delete_label(label_p,name,args.label_list)
            elif args.flag == 'change':
                replace_label(label_p,name,args.label_change,args.label_list)
            elif args.flag == 'axis':
                ng=set()
                axis_list=get_axis(label_p,name)
                print('{}:{},{}'.format(name,axis_list,len(axis_list)))
            elif args.flag =='check':
                error_name=check_label(label_p,name)
                if error_name:
                    error_lists.add(error_name)
            elif args.flag =='create':
                imgp=os.path.join(img_p, "{}.jpg".format(name))
                img = cv2.imread(imgp)
                labelp=os.path.join(label_p,"{}.xml".format(name))
                create_xml(labelp,name,img.shape,args.folder)
        if args.flag =='check':
            print('error_file_list:{}'.format(list(error_lists)))
        elif args.flag =='label':
            print('label:{}'.format(list(label_lists)))
            print('NO_label_name:{}'.format(list(no_label)))
