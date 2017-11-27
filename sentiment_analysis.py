#!/usr/bins/env python3
# -*- coding = utf-8 -*-

import re
import jieba.posseg
import loadDirectory
from functools import reduce

def print_group(word, kind):
    print(word.join(' ').join(kind))

def not_empty(s):
    return s and s.strip()

path = "C:\\Users\\huzehao666\\PycharmProjects\\untitled\\resource\\"
t = path+"正面情感词语（中文）.txt"

positiveDictory = loadDirectory.loadDict(path,"正面评价词语（中文）.txt",1)
loadDirectory.appendDict(positiveDictory,path,"正面情感词语（中文）.txt", 1)
negativeDictory = loadDirectory.loadDict(path,"负面情感词语（中文）.txt",-1)
loadDirectory.appendDict(negativeDictory, path,"负面评价词语（中文）.txt",-1)
extentDictory = loadDirectory.loadExtentDict(path,"程度级别词语（中文）")
#print(negativeDictory)

reverseList = []
with open(path+"否定词语.txt",encoding="utf-8") as f:
    for items in f:
        item = items.strip()
        reverseList.append(item)
#print(reverseList)
score = 0
scoreOfGroup = 0
numOfReverseWordBeforeSentimentWord = 0
haveSentimentWord = False
haveExtentWord = False
def get_score(dictory,key):
    return dictory.get(key,0)

senseWord = {"v","vd","vn","vf" ,"vx" ,"vi" ,"vl" ,"vg","a","ad","an","ag","al","d","dg"}

def reduceOperation(item1,item2):
     return item1*item2


with open("g:\\test.txt","r",encoding="utf-8") as f:
    document = f.read()
    document = document.split('\n')                          #划分为段落
    document = ['我难过而且悲伤.']
    for paragraph in document:
        #paragraph = '建议酒店把老的标准间从新改善.'
        paragraph = re.split('[。？！；.?!;“”]',paragraph)  #划分为句子
        if paragraph[-1] == '':
            paragraph.pop()
        #print(paragraph)
        for sentence in paragraph:
            sentence = re.split('[，,]',sentence)             #句子划分意群
            if sentence[-1] == '':
                sentence.pop()
            #print(sentence)
            for group in sentence:
                if len(group) != 0:
                    words = jieba.posseg.cut(group)           #对意群进行分词
                    stack =[]
                    for word, kind in words:
                       # if kind in senseWord:
                            if word in reverseList:
                                stack.append(-1)
                            else:
                                stack.append(get_score(extentDictory,word))
                                if stack[-1] == 0:
                                    stack.pop()
                                    stack.append(get_score(positiveDictory, word))
                                    if stack[-1] == 0:
                                        stack.pop()
                                        stack.append(get_score(negativeDictory,word))
                                        if stack[-1] != 0:
                                            haveSentimentWord = True
                                        else: stack.pop()
                                    else: haveSentimentWord = True
                                else: haveExtentWord = True
                            if len(stack) > 0:
                                print(word, kind, stack[-1])
                            else:
                                print(word, kind)
                    if haveSentimentWord == True:
                        if stack[0] == -1 and haveExtentWord == True:
                            scoreOfGroup = reduce(reduceOperation, stack)*(-0.5)
                        else: scoreOfGroup = reduce(reduceOperation, stack)
                        #print(scoreOfGroup)
                        score +=scoreOfGroup
                    haveExtentWord = False
                    haveSentimentWord = False
                    stack.clear()

print(score)



