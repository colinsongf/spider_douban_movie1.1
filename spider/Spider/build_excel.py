# -*- coding: utf-8 -*-
import xlwt
import os

def build_excel(dirs,tags):
    dirs = 'E:\\douban_movie\\'
    if os.path.exists(dirs):
        print("文件夹已存在，不需要重建")
    else:
        os.makedirs(dirs)
    for tag in tags:
        excle_name = tag
        #根据不同的标签创建相应的Excel
        if os.path.exists(dirs+excle_name+'.xls'):
            print("文件已存在，不需要新建")
        else:
            workbook = xlwt.Workbook(encoding='ascii')
            worksheet = workbook.add_sheet('My Worksheet')
            workbook.save(dirs+excle_name+'.xls')
    print("excle has build successful")
    return True
