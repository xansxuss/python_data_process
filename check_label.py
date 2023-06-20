import os, argparse
import xml.etree.cElementTree as ET
from file_operate import check_path,get_file,move_f
from xml_operate import get_label



def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--label_path",help="label path")
    parser.add_argument("--img_path",help="img path")
    parser.add_argument("--out_path",help="out_path")
    known_args, _ = parser.parse_known_args()
    return known_args

if __name__ == "__main__":
    args=parse_arguments()
    name_list=get_file(args.label_path)
    for name in name_list:
        print('name:{}'.format(name))
        label_list=get_label(args.label_path,name)
        print('label:{}'.format(label_list,))
        if not label_list:
            move_f(name,'jpg',args.img_path,args.out_path)
            move_f(name,'xml',args.label_path,args.out_path)
