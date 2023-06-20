import os,shutil

path = '/home/xanxus/Desktop/number_data/digit_6'

img_p=os.path.join(path,'imgs')
label_p=os.path.join(path,'labels')

name_list=os.listdir(img_p)
for name in name_list:
    name_ds = name.split('.')
    # img rename
    shutil.move(os.path.join(img_p,name),os.path.join(img_p,'{}_{}_{}.jpg'.format(name_ds[0],name_ds[1],name_ds[-2])))
    
    
    
name_list=os.listdir(label_p)
for name in name_list:
    name_ds = name.split('.')   
    shutil.move(os.path.join(label_p,name),os.path.join(label_p,'{}_{}_{}.xml'.format(name_ds[0],name_ds[1],name_ds[-2])))