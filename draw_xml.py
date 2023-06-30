import os, re,time,argparse
import cv2 ,json
import xml.etree.cElementTree as ET
from img_open import write_img,show_img
from file_operate import get_file
import xml_operate as xo





def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="load data")
    # parser.add_argument("--img_path",help="image dataset path")
    # parser.add_argument("--label_path",help="label path")
    parser.add_argument("--save_path",help="output save path")
    parser.add_argument("--data_path",help="data path")
    parser.add_argument('--folder',help="folder_list",nargs='+')
    known_args, _ = parser.parse_known_args()
    return known_args



def draw_bbox(img,name,label_d):
    label_data=label_d.setdefault(name,0)
    print('draw:{}'.format(name))
    
    for i in range(len(label_data)):
        label,xmin,ymin,xmax,ymax=label_data[i]
        img_out=cv2.rectangle(img_o,(int(xmin),int(ymin)),(int(xmax),int(ymax)),(255,0,0),2)
        img_out=cv2.putText(img_out,label,(int(xmin),int(ymax)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1,cv2.LINE_AA)
        # cv2.imwrite('{}/{}_out.jpg'.format(args.save_path,out_name),img_out)
    return img_out


if __name__ == "__main__":
    args=parse_arguments()
    for folder in args.folder:
        img_path = os.path.join(args.data_path,folder,'imgs')
        label_path = os.path.join(args.data_path,folder,'labels')
        if args.save_path:
            if not os.path.exists(args.save_path):
                os.mkdir(args.save_path)
            else:
                for i in os.listdir(args.save_path):
                    os.remove(os.path.join(args.save_path,i))
        img_list=get_file(img_path)
        label_lists=get_file(label_path)
        
        for i in range(len(label_lists)):
            name=label_lists[i].split('.')[0]
            img_name=os.path.join(img_path,'{}.jpg'.format(name))
            img_o=cv2.imread(img_name)
            label_list=xo.get_label(label_path,label_lists[i])
            axis_list=xo.get_axis(label_path,label_lists[i])

            label_data = {}
            label_array=[]
            for label,axis in zip(label_list,axis_list):
                label_array.append([label,axis[0],axis[1],axis[2],axis[3]])
                print(label_array)
                
            label_data[label_lists[i]]=label_array
            
            img = draw_bbox(img_path,name,label_data)

            if args.save_path:
                write_img('{}/{}_out.jpg'.format(args.save_path,folder,name),img)
                # open_img('{}_out.jpg'.format(name),args.save_path)
            else:
                show_img(name,img)

        
        







