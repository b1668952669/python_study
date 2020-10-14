# -*- coding: cp936 -*-
import random
title='XXX周例会\n会议时间: '
timelist=['6月6日','6月13日','6月20日','6月27日','7月4日','7月11日','7月18日','7月25日',
          '8月1日','8月8日','8月15日','8月22日','8月29日',
          '9月5日','9月12日','9月19日','9月26日',
          ]#包含17个日期的列表
str1='会议地点: XXX房间\n'
str2='主持人: 张三\n'
str3='参加人员: AAA、BBB、ccc\n会议内容：\n '
list1=['第一段(A型)\n','第一段(B型)\n','第一段(C型)\n','第一段(D型)\n']
list2=['第二段(A型)\n','第二段(B型)\n','第二段(C型)\n','第二段(D型)\n']
list3=['第三段(A型)\n','第三段(B型)\n','第三段(C型)\n','第三段(D型)\n']
list4=['第四段(A型)\n','第四段(B型)\n','第四段(C型)\n','第四段(D型)\n']
for i in range(0,17):
    aa=random.randint(0,3)#随机赋给aa“0、1、2,3”三个值
    bb=random.randint(0,3)
    cc=random.randint(0,3)
    dd=random.randint(0,3)
    print(timelist[i])
    print(aa,bb,cc,dd)
    f=open('XXX周例会'+timelist[i]+'.txt','w')# 新建文件，文件名是“标题+日期”。r只读，w可写，a追加
    f.write(title + timelist[i] + '\n' + str1 + str2 + str3 + list1[aa] + list2[bb] + list3[cc] + list4[dd] + '\n')
    #在文件中写入随机生成的第一段，第二段，第三段，第四段。
    f.close()#关闭文件读写。