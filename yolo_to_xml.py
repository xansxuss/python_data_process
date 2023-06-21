import os,cv2,argparse
import file_operate as fo
import xml_operate as xo

def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--label_path",help="label path")
    parser.add_argument("--img_path",help="img path")
    parser.add_argument("--folder",help="multi folder",nargs='+')
    known_args, _ = parser.parse_known_args()
    return known_args

if __name__== "__main__":
    args=parse_arguments()
    # path='/home/xanxus/Desktop/yolov5-crowdhuman/runs/detect/15'
    # name = '0_2_out_13650'
    # w , h = 608,608
    for folder in args.folder:
        img_p=os.path.join(args.img_path,folder,'imgs')
        label_p=os.path.join(args.label_path,folder,'labels')
        
        label_list=fo.get_file(label_p)
        for lname in label_list:
            img = cv2.imread(os.path.join(img_p,'{}.jpg'.format(lname)))
            with open(os.path.join(label_p,'{}.txt'.format(lname))) as f:
                contents = [line for line in f.readlines()]
            f.close
            xml_path=os.path.join(args.img_path,folder,'labels')
            fo.check_path(xml_path)
            if not os.path.isfile(os.path.join(xml_path,'{}.xml'.format(lname))):
                xo.create_xml(xml_path,lname,img.shape,folder)
            for content in contents:
                d = content.split(' ')
                if d[0] == '1':
                    # x,ycenter an bbox width height
                    x=int(float(d[1])*float(img.shape[1]))
                    y=int(float(d[2])*float(img.shape[0]))
                    w=int(float(d[3])*float(img.shape[1]))
                    h=int(float(d[4])*float(img.shape[0]))
                    # bboxx axis
                    label='head'
                    x1=int(x - w / 2) 
                    y1=int(y - h / 2)
                    x2=int(x + w / 2)
                    y2=int(y + h /2 )
                    axis=[x1,y1,x2,y2]
                    # print(x1,y1,x2,y2)
                    xo.add_label(xml_path,lname,label,axis)
    
    
    
    
    #             draw img
    #             img_o = cv2.rectangle(img,(x1,y1),(x2,y2),(255,255,0),1)
    #             img_o=cv2.circle(img_o,(int(x1),int(y1)),1,(0,0,0),0)
    #             # img_o=cv2.circle(img_o,(int(x2),int(y2)),1,(0,0,0),0)
    #             cv2.imshow('test',img_o)
    #             cv2.waitKey(0)
    # cv2.destroyAllWindows()


