import jieba
text1 = "明天我要去五棵松体育场打篮球"
text2 = "华为联手中国电信，完成了武汉火神山医院首个远程会诊平台的网络铺设和设备调试"
print("待分词语句1：" + text1)
print("\n待分词语句2：" + text2)

seg11 = jieba.cut(text1,True) #cut_all=True:全模式 把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义
seg21 = jieba.cut(text2,True)
print("全模式1：" + "/ ".join(seg11))
print("\n全模式2：" + "/ ".join(seg21))

seg12 = jieba.cut(text1,False) #cut_all=False:精确模式：试图将句子最精确地切开，适合文本分析；
seg22 = jieba.cut(text2,False)
print("\n精确模式1：" + "/ ".join(seg12))
print("\n精确模式2：" + "/ ".join(seg22))

seg13 = jieba.cut_for_search(text1)  #搜索引擎模式：在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
seg23 = jieba.cut_for_search(text2)
print("\n搜索引擎模式1：" + "/ ".join(seg13))
print("\n搜索引擎模式2：" + "/ ".join(seg23))
#jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的生成器 generator，可以使用 for 循环来获得分词后得到的每一个词语
#jieba.lcut 以及 jieba.lcut_for_search 可以直接返回 list



#关键词提取
#主要基于无监督算法，如：TF-IDF 算法，TextRank 算法和主题模型算法（包括LSA，LSI，LDA等）
from jieba import analyse
anal_text = "天安门广场，位于北京市中心，地处北京市东城区东长安街，北起天安门，南至正阳门，东起中国国家博物馆，西至人民大会堂，南北长880米，东西宽500米，面积达44万平方米，可容纳100万人举行盛大集会，是世界上最大的城市广场。广场地面全部由经过特殊工艺技术处理的浅色花岗岩条石铺成，中央矗立着人民英雄纪念碑和庄严肃穆的毛主席纪念堂，天安门两边是劳动人民文化宫和中山公园，与天安门浑然一体，共同构成天安门广场。"
print("文本：", anal_text)

#TF-IDF 用以评估一个词语对于一个文件集或一个语料库中的一份文件的重要程度:一个词语在一篇文章中出现次数越多，同时在所有文档中出现次数越少，越能够代表该文章
tf_idf = analyse.extract_tags
print("TF-IDF算法提取的20个关键词：\n")
for x, w in tf_idf(anal_text, withWeight=True):
    print('%s : %s' % (x, w))

#TextRank 通过把文本分割成若干组成单元（单词、句子）并建立图模型，利用投票机制对文本中的重要成分进行排序，仅利用单篇文档本身的信息即可实现关键词提取、文摘
trank = analyse.textrank
print("TextRank 算法提取的20个关键词：\n")
for x, w in trank(anal_text, withWeight=True):
    print('%s : %s' % (x, w))



#词性标注
from jieba import posseg
pseg_text = "天安门坐落在中华人民共和国首都北京市的中心、故宫的南端，占地面积4800平方米，以杰出的建筑艺术和特殊的政治地位为世人所瞩目。"
print("文本：", pseg_text)
pwords = posseg.cut(pseg_text)
for word, flag in pwords:
    print("{} : {}".format(word, flag))
