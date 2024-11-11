import os,cv2,argparse

def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--video_folder",help="video_folder")
    parser.add_argument("--save_path",help="save image path")
    known_args, _ = parser.parse_known_args()
    return known_args

def get_extension(path,name):
    if not (os.path.isdir(os.path.join(path,name))):
        exname=name.split('.')[1]
        return exname

def get_file(path):
    file_list=[]
    files=os.listdir(path)
    for i in files:
        name=get_extension(path,i)
        if name == 'mp4':
            file_list.append(i)
    return file_list

def check_path(path):
    if not os.path.isdir(path):
       os.makedirs(path) 

if __name__ == "__main__":
    args=parse_arguments()
    
    video_list = get_file(args.video_folder)
    
    for file in video_list:
        cam = cv2.VideoCapture(os.path.join(args.video_folder,file))
        frame_end = cam.get(cv2.CAP_PROP_FRAME_COUNT)
        count =0
        while (cam.isOpened()):
            if count > frame_end:
                break
            ret,frame = cam.read()
            if not ret:
                break
            cv2.namedWindow('show',cv2.WINDOW_NORMAL)
            cv2.imshow('show',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            path_name = os.path.join(args.save_path,file.split('.')[0])
            file_name = '{}_{}.jpg'.format(file.split('.')[0],count)
            check_path(path_name) 
            cv2.imwrite('{}'.format(os.path.join(path_name,file_name)),frame)
            count+=1
        
        cam.release()
        cv2.destroyAllWindows()