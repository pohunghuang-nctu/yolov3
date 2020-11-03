#!/bin/bash
python detect.py --source ~/lab3/data_host/mydata/sources/ --output ~/lab3/data_host/mydata/output_best --names ~/lab3/data_host/mydata/obj.names --cfg ~/lab3/data_host/mydata/yolov3_obj.cfg --weights ~/lab3/data_host/yolov3/weights/yolov3_obj_best.pt --save-txt
