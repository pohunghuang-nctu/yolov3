#!/bin/bash
python resample.py /home/user/lab3/data_host/mydata/images
python train.py --data /home/user/lab3/data_host/mydata/obj.data --cfg /home/user/lab3/data_host/mydata/yolov3_obj.cfg --weights weights/last.pt --epochs 90
