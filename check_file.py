import os


# img_path = '/home/xanxus/Desktop/Dataset/palm/JPEGImages'
# label_path= '/home/xanxus/Desktop/Dataset/palm/Annotations'
# set_path='/home/xanxus/Desktop/Dataset/palm/ImageSets/Main/'

img_path = '/home/xanxus/Desktop/re/Dataset/head/JPEGImages'
label_path= '/home/xanxus/Desktop/re/Dataset/head/Annotations'
set_path='/home/xanxus/Desktop/re/Dataset/head/ImageSets/Main/'

train_list=[]
val_list=[]

with open(os.path.join(set_path,'{}.txt'.format('train'))) as ft:
    contents = [line for line in ft.readlines()]
    for content in contents:
        content=content.split('\n')[0]
        train_list.append(content)
ft.close()
# print('train_list:',train_list)
# print('\n','\n')

with open(os.path.join(set_path,'{}.txt'.format('val'))) as fv:
    contents = [line for line in fv.readlines()]
    for content in contents:
        content=content.split('\n')[0]
        val_list.append(content)
fv.close()
# print('val_list:',val_list)

img_list=os.listdir(img_path)
label_list=os.listdir(label_path)
print(len(img_list))
print(len(label_list))
print(len(train_list))
print(len(val_list))