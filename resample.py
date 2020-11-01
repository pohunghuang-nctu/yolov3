#!/home/user/anaconda3/bin/python
import sys
import zipfile
import tarfile
import os
import random


def main():
    image_folder = sys.argv[1]
    gen_lists(image_folder)


def check_label(label_folder):
    for label_file in os.listdir(label_folder):
        label_path = os.path.join(label_folder, label_file)
        img_path = label_path.replace('labels', 'images').replace(os.path.splitext(label_file)[-1], '.png')
        if not os.path.exists(img_path):
            print('%s has no image file' % label_file)
            os.replace(label_path, label_path.replace('labels', 'error_labels'))
            continue
        print('Dealing with %s' % label_path)
        with open(label_path, 'r') as lfile:
            for line in lfile:
                line = line.strip()
                elements = line.split(' ')
                class_id = int(elements[0])
                if class_id > 35 or class_id < 0:
                    print('%s has invalid class: %d' % (label_path, class_id))
                    os.replace(label_path, label_path.replace('labels', 'error_labels'))
                    break


def gen_lists(image_folder):
    valid_set = []
    base_dir = os.path.dirname(image_folder)
    cnt = 0
    not_found = 0
    total = 0
    for img in os.listdir(image_folder):
        total += 1
        img_path = os.path.join(image_folder, img)
        label_path = img_path.replace('images', 'labels').replace(os.path.splitext(img)[-1], '.txt')
        if os.path.exists(label_path):
            valid_set.append(img_path)
            cnt += 1
        else:
            # print('%s not found.' % label_path)
            not_found += 1
    print('Total %d valid images found.' % cnt)
    print('Total %d images.' % total)
    print('Total %d no label found.' % not_found)
    train_set = random.sample(valid_set, int(len(valid_set) * 0.8))
    with open(os.path.join(base_dir, 'train.txt'), 'w') as tfile:
        tfile.write('\n'.join(train_set))
    test_set = []
    for item in valid_set:
        if item not in train_set:
            test_set.append(item)
    with open(os.path.join(base_dir, 'test.txt'), 'w') as sfile:
        sfile.write('\n'.join(test_set))
    

def move_label_file(theDir, label_folder):
    for root, dirs, files in os.walk(theDir):
        for f in files:
            if f.endswith('.txt'):
                fpath = os.path.join(root, f)
                print('moving %s' % fpath)
                os.replace(fpath, os.path.join(label_folder, f))


def recursive_extract(path):
    if not zipfile.is_zipfile(path) and\
            not tarfile.is_tarfile(path):
        return
    theDir = os.path.dirname(path)
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(theDir)
    elif tarfile.is_tarfile(path):
        with tarfile.open(path) as tar_ref:
            tar_ref.extractall(theDir)
    os.remove(path)
    for base, dirs, files in os.walk(theDir):
        for f in files:
            fpath = os.path.join(base, f)
            print(fpath)
            if os.path.exists(fpath) and\
                    (zipfile.is_zipfile(fpath) or\
                    tarfile.is_tarfile(fpath)):
                recursive_extract(fpath)


if __name__ == '__main__':
    main()