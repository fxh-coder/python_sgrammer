from StopWords import readFile,seg_doc
from FreqWord import *


def freqword(fdist):
    wordlist =[]
    print('='*3,'打印统计的词频','='*3)
    for key in fdist.keys():
        if fdist.get(key)>2 and fdist.get(key)<15:
            wordlist.append(key+':'+str(fdist.get(key)))
    return wordlist


if __name__=='__main__':
    # 1 读取文本
    path= r'./fxh.txt'
    str_doc = readFile(path)
    word_list =seg_doc(str_doc)
    # 2 选择高低词
    fdist = nltk_wf_feature(word_list)
    wordlist=freqword(fdist)
    print(wordlist)