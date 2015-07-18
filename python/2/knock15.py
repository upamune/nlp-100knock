# -*- coding: utf-8 -*-
# @create = 2015/07/19
# @modify = 2015/07/19

'''
15. 末尾のN行を出力

自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
'''

import sys

argvs = sys.argv
n = int(argvs[1])+1

f = open('../data/hightemp.txt','r')
f_arr = f.read().split("\n")
f_len = len(f_arr)

for i in range(f_len-n, f_len):
    print f_arr[i]
