# -*- coding: utf-8 -*-
from xlrd import open_workbook
from xlutils.copy import copy


def save_to_excel(dirs, tag, excel_row, movie_name, rate, people_num, movie_url):
    excel_name = tag
    rb = open_workbook(dirs+excel_name+'.xls', formatting_info=True)
    wb = copy(rb)
    sheet=wb.get_sheet(0)
    sheet.write(excel_row, 0, movie_name)
    sheet.write(excel_row, 1, people_num)
    sheet.write(excel_row, 2, rate)
    sheet.write(excel_row, 3, movie_url)
    wb.save(dirs+excel_name+'.xls')
    print(tag+str(excel_row)+'has saved')

