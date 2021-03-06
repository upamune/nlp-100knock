# -*- coding: utf-8 -*-
# @author = himkt
# @create = 2015/07/21

'''
30. 形態素解析結果の読み込み

形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），
基本形（base），
品詞（pos），
品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
'''



def knock30():

    sentense_morph_list = []
    morph_mapping_list = []

    for line in open('../data/neko.mecab', 'r'):
        line = line.rstrip()
    
        if line == 'EOS':
            sentense_morph_list.append(morph_mapping_list)
            morph_mapping_list = []
            continue
    
        elements = line.split("\t")
        morph_info = elements[1].split(",")
    
        morph = {
           'surface' : elements[0],
            'base'   : morph_info[6],
            'pos'    : morph_info[0],
            'pos1'   : morph_info[1]
        }

        morph_mapping_list.append(morph)
    
    return sentense_morph_list

if __name__ == '__main__':

    sentense_morph_list = knock30()
    print len(sentense_morph_list)
