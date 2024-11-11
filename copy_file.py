import os,argparse,shutil,random
import file_operate as fo

def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--source")
    parser.add_argument("--target")
    parser.add_argument("--type",type=str)
    known_args, _ = parser.parse_known_args()
    return known_args




if __name__ == "__main__":
    arge = parse_arguments()
    # file_list = os.listdir(arge.target)
    # for file in file_list:
    #     name = file.split('.')[0]
    #     if arge.type == "label":
    #         shutil.copy2(os.path.join(arge.source,'{}.xml'.format(name)),arge.target)
    #     elif arge.type == "image":
    #         shutil.copy2(os.path.join(arge.source,'{}.jpg'.format(name)),arge.target)
    
    
    file_list = fo.get_file(os.path.join(arge.source,'images'))
    len_file = len(file_list)
    trainset_n = int(len_file *0.8)
    random.shuffle(file_list)
    train_list = file_list[:trainset_n]
    val_list = file_list[trainset_n:]


    img_train = os.path.join(arge.target,'images','train')
    img_val = os.path.join(arge.target,'images','val')
    label_train =os.path.join(arge.target,'labels','train')
    label_val =os.path.join(arge.target,'labels','val')
    fo.check_path(img_train)
    fo.check_path(img_val)
    fo.check_path(label_train)
    fo.check_path(label_val)



    for train_f in train_list:
        base_name = fo.get_base(train_f)
        shutil.copy2(os.path.join(arge.source,'images','{}.jpg'.format(base_name)),img_train)
        shutil.copy2(os.path.join(arge.source,'yolo','{}.txt'.format(base_name)),label_train)
    for val_f in val_list:
        base_name = fo.get_base(val_f)
        shutil.copy2(os.path.join(arge.source,'images','{}.jpg'.format(base_name)),img_val)
        shutil.copy2(os.path.join(arge.source,'yolo','{}.txt'.format(base_name)),label_val)


    # file_list_s = fo.get_file("/home/eray/project/mxic_truck/video_pipe/xml")
    # file_list_c = fo.get_file("/home/eray/project/mxic_truck/video_pipe/xml2")
    # print(len(file_list_s))
    # print(len(file_list_c))
    # for file in file_list_s:
    #     if file in file_list_c:
    #         file_list_s.remove(file)
    #     else:
    #         shutil.copy(os.path.join("/home/eray/project/mxic_truck/video_pipe/xml",file),"/home/eray/project/mxic_truck/video_pipe/preprocess/xml")
    #         file_j = file.spilt('.')[1]
    #         shutil.move(os.path.join("/home/eray/project/mxic_truck/video_pipe/images",'{}.jpg'.format(file_j)),"/home/eray/project/mxic_truck/video_pipe/preprocess/images")
    

    # print(len(file_list_s))