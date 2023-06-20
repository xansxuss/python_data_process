import cv2 ,os,argparse
from file_operate import check_path
def open_img(name,folder):
    p=os.path.join(folder,name)
    img=cv2.imread(p)
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name,2000,2000)
    cv2.imshow(name,img)
    # cv2.waitKey(0) == ord('q')
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

def open_multi_folder_img(folder_path,folder_list):
    for i in folder_list:
        path = os.path.join(folder_path,i)
        name_list = os.listdir(path)
        for n in name_list:
            img=cv2.imread(os.path.join(path,n))
            cv2.namedWindow('{} + {}'.format(i,n),cv2.WINDOW_NORMAL)
            cv2.resizeWindow('{} + {}'.format(i,n),2000,2000)
            cv2.imshow('{} + {}'.format(i,n),img)
            cv2.waitKey(500)
            cv2.destroyAllWindows()


def open_video(name,folder):
    p=os.path.join(folder,name)
    cap = cv2.VideoCapture(p)
    while(cap.isOpened()):
        ret, frame = cap.read()

        cv2.imshow(name,frame)
        fps=cap.get(cv2.CAP_PROP_FPS)
        print(fps)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def show_img(name,img):
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name,2000,2000)
    cv2.imshow(name,img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

def write_img(out_name,out_img):
    cv2.imwrite(out_name,out_img)

def get_file(path):
    file_list=[]
    files=os.listdir(path)
    for i in range(len(files)):
        # name=files[i].split('.')[0]
        # file_list.append(name)
        file_list.append(files[i])
    return file_list
def save_video_frame(data_path,floders,save_path):
    num=0
    for folder in floders:
        name_list = get_file(os.path.join(data_path,folder))
        
        for name in name_list:
            n = name.split('.')[0]
            if '.mp4' in name:
                x
                print('do:{}'.format(n))
                cam = cv2.VideoCapture(os.path.join(data_path,folder,name))
                frame_end = cam.get(cv2.CAP_PROP_FRAME_COUNT)
                num = num + frame_end
                while(cam.isOpened()):
                    ret,frame=cam.read()
                    frame_count = cam.get(cv2.CAP_PROP_POS_FRAMES)
                    cv2.imwrite('{}/{}_{}.jpg'.format(save_path,n,x),frame)
                    x= x+1
                    if frame_count == frame_end:
                        break
                    
                    # cv2.imshow(name,frame)
                    # fps=cam.get(cv2.CAP_PROP_FPS)
                    # print(fps)
                    # if cv2.waitKey(1) & 0xFF == ord('q'):
                    #     break
    print(int(num))
    cam.release()
    cv2.destroyAllWindows()




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path')
    parser.add_argument('--save_path')
    parser.add_argument('--folder',help="folder_list",nargs='+')
    args=parser.parse_args()
    # check_path(args.save_path)
    # name_list = get_file(args.path)
    # for i in range(len(name_list)):
    #     open_img(name_list[i],args.path)
    #     open_video(name_list[i],args.path)
    # f_list=os.listdir(args.path)
    # open_multi_folder_img(args.path,f_list)
    # save_video_frame(args.input_path,args.folder,args.save_path)

    for flist in args.folder:
        pname = os.path.join(args.input_path,flist)
        file_lists=os.listdir(pname)
        for nfile in file_lists:
            file_name = os.path.join(pname,nfile)
            # print(file_name)
            img=cv2.imread(file_name)
            show_img(nfile,img)