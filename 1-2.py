import os
import json


def create_empty_file(new_f_name):
    with open(new_f_name, "w", encoding='utf-8') as new_file:
        new_file.write("")
    return True


def create_empty_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    return True


def create_sub_dirs(folder_tree, root_f):
    dir_list = []
    for root_folders in folder_tree:
        create_empty_dir(root_f + root_folders)
        dir_list.append(root_f + root_folders)
    return dir_list


def recurse_folder(folder_tre, folder_path):
    # print(folder_tre)
    # print(folder_path)
    if type(folder_tre) is list:
        for file_name in folder_tre:
            if type(file_name) is str:
                create_empty_file(os.path.join(folder_path, file_name))
            else:
                recurse_folder(file_name, folder_path)
    else:
        for folder, file in folder_tre.items():
            current_folder = folder_path + folder
            create_empty_dir(current_folder)
            recurse_folder(file, current_folder + "/")


with open("config.yaml", "r", encoding='utf-8') as config:
    tree = config.read()
tree = json.loads(tree)
root_folder_name = "my_project"
create_empty_dir(root_folder_name)
root_folder_name += "/"
recurse_folder(tree, root_folder_name)
# for folders, files in tree.items():
#     create_empty_dir(root_folder_name + folders)
#     for file in files:
#         print(file)
