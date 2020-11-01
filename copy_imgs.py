#!/home/user/anaconda3/bin/python
import os

root = '/home/user/lab3/data_host/mydata/img/license_plate_img'
image_folder = '/home/user/lab3/data_host/mydata/images'
for base, dirs, files in os.walk(root):
    for f in files:
        fpath = os.path.join(base, f)
        if fpath.endswith('.png'):
            to_path = os.path.join(image_folder, f)
            os.replace(fpath, to_path) 