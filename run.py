#!/usr/bin/env python3

import os

'''
1) get sorter path
2) get files in sorter folder
3) sort files according to exentsion and drop in the corresponding sub-folder: audio, docs, images, video
4) print message that confirms 
'''

APP_FOLDER = "/sorter"
APP_SUB_FOLDERS = ['audio','video','images','docs']

app_path = os.getcwd() + APP_FOLDER
print(app_path)
folder_all_items = os.listdir(app_path)

'''
using list comprehension:
'''
folder_items = [item for item in folder_all_items if item not in APP_SUB_FOLDERS] 
print(folder_items)




