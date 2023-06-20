import os,cv2,argparse
import file_operate as op


def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--data_path",help="data path")
    parser.add_argument("--ng_path",help="ng img path")
    parser.add_argument("--folder",help="multi folder",nargs='+')
    known_args, _ = parser.parse_known_args()
    return known_args

if __name__ == "__main__":
    args=parse_arguments()
    op.check_path(args.ng_path)
    for folder in args.folder:
        path = os.path.join(args.data_path,folder)
        name_list=op.get_file(path)
        for name in name_list:
            img = cv2.imread(os.path.join(path,'{}.jpg'.format(name)))
            cv2.namedWindow(name,cv2.WINDOW_NORMAL)
            cv2.resizeWindow(name,2000,2000)
            cv2.imshow(name,img)
            key = cv2.waitKey(0)
            if key == ord('c'):
                print('pass')
                cv2.destroyWindow(name)
                continue
            elif key == ord('m'):
                print('NG')
                op.move_f(name,'jpg',path,args.ng_path)
            else:
                key & 0xFF == ord('q')
                break
            cv2.destroyAllWindows()
