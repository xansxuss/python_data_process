import os,shutil,argparse

# source = '/home/xanxus/Desktop/HaGRID_data/data/label/anno_xml_stop'
# target ='/home/xanxus/Desktop/HaGRID_data/t/stop/xml/'
source = '/home/xanxus/Desktop/SSD_data/CrowdHuman'
target ='/home/xanxus/Desktop/SSD_data/CrowdHuman/NG'
name_list=['282555,d93bf00039a433d9']
# def get_file(path):
#     file_list=[]
#     files=os.listdir(path)
#     for i in range(len(files)):
#         if '.' in files[i]:
#             name=files[i].split('.')[0]
#             print(files[i])
#             file_list.append(name)
#         else:
#             # print("it is folder")
#             continue
#     return file_list

def move_f(file_name ,ex_name,source,target):
    # source=os.path.join(source,file_name)
    # shutil.move(source,target)
    shutil.move(os.path.join(source,'{}.{}'.format(file_name,ex_name)),target)
    # print(os.path.join(source,'{}.{}'.format(file_name,ex_name)))

def copy_f(source ,target):
    shutil.copy(source,target)

def get_extension(name):
    return name.split('.')[1]
    
def get_base(name):
    return name.split('.')[0]

def decide_file_exist(name):
    if not os.path.exists(name):
        os.mkdir(name)    
def get_file(path):
    file_list=[]
    files=os.listdir(path)
    for i in range(len(files)):
        name=files[i].split('.')[0]
        file_list.append(name)
    return file_list
def check_path(path):
    if not os.path.isdir(path):
       os.makedirs(path) 
def check_file_number(path):
    number = len(os.listdir(path))
    return number
def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--path",help="label path")
    known_args, _ = parser.parse_known_args()
    return known_args
if __name__ == "__main__":
    check_path(target)
    for i in range(len(name_list)):
        shutil.move(os.path.join(source,'labels','{}.xml'.format(name_list[i])),target)
        shutil.move(os.path.join(source,'imgs','{}.jpg'.format(name_list[i])),target)
    # args=parse_arguments()
    # ls = os.listdir(args.path)
    # for l in ls:
    #     n=l.split('.')
    #     if len(n)>2:
    #         print('name:{},split:{},len:{}'.format(l,n,len(n)))

    # img_l=get_file(os.path.join('/home/xanxus/Desktop/HaGRID_data/Dataset/stop','img'))
    # label_l=get_file(os.path.join('/home/xanxus/Desktop/HaGRID_data/Dataset/stop','label'))
    # out=list(set(img_l).symmetric_difference(set(label_l)))
    # print(out)