import os,argparse,random
import file_operate as fo
import xml_operate as xo

img_exname=['jpg','png','jpeg']

def create_data_structure(path):
    p_list=['Annotations','ImageSets','JPEGImages']
    for i in range(len(p_list)):
        l_path=os.path.join(path,p_list[i])
        fo.decide_file_exist(l_path)
    fo.decide_file_exist(os.path.join(path,'ImageSets/Main'))

def get_train_num(path,folder_list):
    num=[]
    for folder in folder_list:
        file_list=os.listdir(os.path.join(path,folder,'imgs'))
        num.append(len(file_list))
    return num





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--xml_path')
    parser.add_argument('--img_path')
    parser.add_argument('--data_path')
    parser.add_argument('--save_path')
    parser.add_argument('--folder',help="folder_list",nargs='+')
    parser.add_argument('--num',help="file number")
    args=parser.parse_args()
    fo.check_path(args.save_path)
    create_data_structure(args.save_path)
    num = get_train_num(args.data_path,args.folder)
    print(num)
    min_num=min(num)
    



    for folder in args.folder:
        i_files=fo.get_file(os.path.join(args.data_path,folder,'imgs'))
        l_files=fo.get_file(os.path.join(args.data_path,folder,'labels'))
        print('{}:start'.format(folder))
        # print(len(l_files))
        x= 0
        for n in l_files:
            name = n .split('.')[0]
            error_name=xo.check_label(os.path.join(args.data_path,folder,'labels'),name)
            # print(error_name)
            if error_name:
                x= x+1
                l_files.remove(error_name)
        # print(x)
        print(len(l_files))


        if args.num and len(l_files)>=int(args.num):
            num=int(args.num)
            new_n_list1=random.sample(l_files,num)
            new_n_list2=list(set(l_files).symmetric_difference(set(new_n_list1)))
            new_n_list2=random.sample(new_n_list2,int(num*0.2))
            new_n_list3=new_n_list1+new_n_list2
            # print('{}'.format(l_files),len(l_files),'\n')
            # print('{}'.format(new_n_list1),len(new_n_list1),'\n')
            # print('{}'.format(new_n_list2),len(new_n_list2),'\n')
            # print('{}'.format(new_n_list3),len(new_n_list3))
            with open('{}/ImageSets/Main/train.txt'.format(args.save_path),'a+') as ft:
                for fts in range(len(new_n_list1)):
                    ft.write(new_n_list1[fts])
                    ft.write('\n')
            ft.close()
            with open('{}/ImageSets/Main/val.txt'.format(args.save_path),'a+') as fv:
                for fvs in range(len(new_n_list2)):
                    fv.write(new_n_list2[fvs])
                    fv.write('\n')
            fv.close()
            
            ## img cpoy
            for i in new_n_list3:
                    sorce=os.path.join(args.data_path,folder,'imgs','{}.jpg'.format(i))
                    target=os.path.join(args.save_path,'JPEGImages','{}.jpg'.format(i))
                    fo.copy_f(sorce,target)
            ## label copy
                    sorce=os.path.join(args.data_path,folder,'labels','{}.xml'.format(i))
                    target=os.path.join(args.save_path,'Annotations','{}.xml'.format(i))
                    fo.copy_f(sorce,target)
            print('{}:finish'.format(folder))
        else:
            new_n_list1=random.sample(l_files,int(min_num*0.8))
            new_n_list2=list(set(l_files).symmetric_difference(set(new_n_list1)))
            
            with open('{}/ImageSets/Main/train.txt'.format(args.save_path),'a+') as ft:
                for fts in range(len(new_n_list1)):
                    ft.write(new_n_list1[fts])
                    ft.write('\n')
            ft.close()
            with open('{}/ImageSets/Main/val.txt'.format(args.save_path),'a+') as fv:
                for fvs in range(len(new_n_list2)):
                    fv.write(new_n_list2[fvs])
                    fv.write('\n')
            fv.close()
            
            ## img cpoy          
            for i in l_files:
                    sorce=os.path.join(args.data_path,folder,'imgs','{}.jpg'.format(i))
                    target=os.path.join(args.save_path,'JPEGImages','{}.jpg'.format(i))
                    fo.copy_f(sorce,target)
            ## label copy
                    sorce=os.path.join(args.data_path,folder,'labels','{}.xml'.format(i))
                    target=os.path.join(args.save_path,'Annotations','{}.xml'.format(i))
                    fo.copy_f(sorce,target)
            print('{}:finish'.format(folder))
