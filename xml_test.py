import os ,shutil
import xml.etree.cElementTree as ET
import xml_operate as xo
import file_operate as fo 



path = '/home/eray/project/mxic_truck/video_pipe/xml/'

file_list = fo.get_file(path)
for file in file_list:
    tree = ET.parse(os.path.join(path,'{}.xml'.format(file)))
    root=tree.getroot()
    if root.findall('object') :
        print(file)
        shutil.copy(os.path.join("/home/eray/project/mxic_truck/video_pipe/xml",'{}.xml'.format(file)),"/home/eray/project/mxic_truck/video_pipe/preprocess/xml/")
        shutil.move(os.path.join("/home/eray/project/mxic_truck/video_pipe/images",'{}.jpg'.format(file)),"/home/eray/project/mxic_truck/video_pipe/preprocess/images/")