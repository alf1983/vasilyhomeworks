import os
import shutil

root_folder = "my_project"
glob_dir_template = root_folder + "/" + "templates"
if not os.path.exists(glob_dir_template):
    os.mkdir(glob_dir_template)
for root, dirs, files in os.walk(root_folder):
    if root.find('templates') > 0 and root != glob_dir_template:
        for dir_template in dirs:
            print(root + "/" + dir_template)
            print(glob_dir_template)
            print(shutil.copytree(root + "/" + dir_template, glob_dir_template + "/" + dir_template))
