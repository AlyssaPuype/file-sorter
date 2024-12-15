#!/usr/bin/env python3

import os

'''
1) get sorter path
2) get files in sorter folder
3) sort files according to exentsion and drop in the corresponding sub-folder: audio, docs, images, video, ebooks
4) print message that confirms 
'''

APP_FOLDER = "/sorter"
APP_SUB_FOLDERS = ['audio','video','images','docs', 'ebooks']
audio_folder, video_folder, image_folder, docs_folder, book_folder = APP_SUB_FOLDERS
AUDIO_EXTENSIONS = ('.mp3', '.wav')
VIDEO_EXTENSIONS = ('.mp4', '.mov', '.avi', '.webm')
IMAGE_EXTENSIONS = ('.png', '.jpg', '.gif', '.svg', '.ico')
DOCS_EXTENSIONS = ('.txt', '.doc', '.txt', '.xlsx', '.csv', '.pdf', '.ppt')
BOOK_EXTENSIONS = ('.epub',)


app_path = os.getcwd() + APP_FOLDER
print("app path : " + app_path)
folder_all_items = os.listdir(app_path)

'''
using list comprehension:
'''
folder_items = [item for item in folder_all_items if item not in APP_SUB_FOLDERS] 
print(folder_items)

for item in folder_items:
	item_and_extension = item.split(".")
	print(item_and_extension[1])
	if item_and_extension[1] =






