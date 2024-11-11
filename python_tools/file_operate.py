import os,shutil,argparse,logging

logging.basicConfig(level=logging.INFO,format='%(filename)s %(funcname)s %(messages)s')

def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--source")
    parser.add_argument("--target")
    parser.add_argument("--type",type=str)
    known_args, _ = parser.parse_known_args()
    return known_args

def check_file(file_name):
    
    if not os.path.isdir(file_name):
        logging.info(f'floder not exist build new folder')
        return False
    else:
        return True

def check_folder(folder_name):
    if not os.path.isdir(folder_name):
        logging.info(f'floder not exist build new folder')
    

def get_file(path):
    file_list = []
    files = os.listdir(path)
    for f in files:
        if os.path.isfile(os.path.join(path,f)):
            name = get_basename(f)
            file_list.append(name)
    return file_list

def get_folder(path):
    folder_list = []
    folders = os.listdir(path)
    for f in folders:
        if os.path.isdir(os.path.join(path,f)):
            name = get_basename(f)
            folder_list.append(name)
    return folder_list

def get_basename(name):
    basename = name.split('.')[0]
    return basename

def get_subname(name):
    subname = name.split('.')[1]
    return subname

def check_file_number(path):
    folder_list = [] 
    folders = os.listdir(path)
    for f in folders:
        if os.path.isdir(os.path.join(path,f)):
            folder_list.append(f)
    return len(folder_list)

def check_file_number(path):
    file_list = [] 
    files = os.listdir(path)
    for f in files:
        if os.path.isfile(os.path.join(path,f)):
            file_list.append(f)
    return len(file_list)

def move_file():
    return 0

def copy_file():
    return 0





if __name__ == "__main__":
    arge = parse_arguments()
