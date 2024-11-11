import os,argparse,cv2

import file_operate as fo

def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--img")
    parser.add_argument("--label")
    known_args, _ = parser.parse_known_args()
    return known_args


if __name__ == "__main__":
    arge = parse_arguments()


    img_list = fo.get_file(arge.img)

    for img_f in img_list:
        img_f = img_f.split('.')[0]
        print(img_f,'\n')
        img = cv2.imread(os.path.join(arge.img,'{}.jpg'.format(img_f)))
        with open(os.path.join(arge.label,'{}.txt'.format(img_f)),'r')as f :
            text_d = f.readlines()
        f.close()
        # print(text_d,'\n')
        count = 0
        for label in text_d:
            # print('x:{},y:{},w:{},h:{}'.format(label.split(' ')[1],label.split(' ')[2],label.split(' ')[3],label.split(' ')[4]))
            w = (int(float(label.split(' ')[3])*img.shape[1]))
            h = (int(float(label.split(' ')[4])*img.shape[0]))
            xc = (int(float(label.split(' ')[1])*img.shape[1]))
            yc = (int(float(label.split(' ')[2])*img.shape[0]))
            xmin = int(xc - (w/2))
            ymin = int(yc - (h/2))
            xmax = int(xc + (w/2))
            ymax = int(yc + (h/2))
            print('x:{},y:{},w:{},h:{}'.format(xc,yc,w,h))
            img = cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,0,0),3)
            count += 1
        cv2.namedWindow('show',cv2.WINDOW_FREERATIO)
        cv2.resizeWindow('show',(1200,1000))
        cv2.imshow('show',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print('file number:{}'.format(count))