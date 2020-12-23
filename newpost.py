from time import localtime
ltime = localtime()
import os

name = input("Enter the name of new post:\n")
addr = 'E:\\Blog\\juvenile\\source\\_posts\\' + name + ".md"

lookup = {
    'CTF': ('REVERSE', 'CRYPTO', '其他'),
    'MATHMATIC & ALGORITHM': ('排序和顺序统计量', '数据结构', '分析技术', '树和图', '数论、密码与编码', '其他'),
    'C++': ('C++ Reference', '其他'),
    'PYTHON': ('Lib & Package', '其他')
}

upper = """---
title: {}
date: {}-{}-{} {}:{}:{}
tags:
{}
categories:
{}
---"""

key_lst = list(lookup.keys())
cnt = 0
for key, value in lookup.items():
    print('【', cnt, '】' ,key, ':', value)
    cnt += 1

tags_str, categories_str = str(), str()
choice_1 = list(map(int, tuple(input("选择大类：\n").split())))

for i in choice_1:  tags_str += '\t- {}\n'.format(key_lst[i])

for i in choice_1:
    print("选择{}大类中的小类：\n".format(key_lst[i]))
    cnt = 0
    for val in lookup[key_lst[i]]:
        print('【', cnt, '】', val)
        cnt += 1
    choice_2 = list(map(int, tuple(input().split())))
    for k in choice_2:
        tags_str += '\t- {}\n'.format(lookup[key_lst[i]][k])
        categories_str += '\t- [{}, {}]\n'.format(key_lst[i], lookup[key_lst[i]][k])

file = open(addr, 'w')
file.write(upper.format(name, ltime.tm_year, ltime.tm_mon, ltime.tm_mday, ltime.tm_hour, ltime.tm_min, ltime.tm_sec, tags_str, categories_str))
file.close()

os.mkdir('E:\\Blog\\juvenile\\source\\_posts\\' + name)