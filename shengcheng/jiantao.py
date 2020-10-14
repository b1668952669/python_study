# -*- coding: utf-8 -*-
import random
import xlrd

ExcelFile = xlrd.open_workbook(r'test.xlsx')
sheet = ExcelFile.sheet_by_name('Sheet1')
i = []
x = input("请输入具体事件：")
y = int(input("要求字数："))
while len(str(i)) < y * 1.2:
    s = random.randint(1, 60)
    rows = sheet.row_values(s)
    i.append(*rows)
print (" "*8+"检讨书"+"\n"+"宝贝：")
print("我不应该" + str(x)+"，" , *i)
print("再次请宝贝原谅!")