#!/bin/bash
python detect_new.py --source ~/lab3/data_host/mydata/sources/ --output ~/lab3/data_host/mydata/output --names ~/lab3/data_host/mydata/obj.names --cfg ~/lab3/data_host/mydata/yolov3_obj.cfg --weights ~/lab3/data_host/yolov3/weights/last.pt --save-txt
