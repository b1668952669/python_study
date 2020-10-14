import jieba

def getWords():
    txt = open('novels/sanguo.txt', 'r', encoding = 'utf-8').read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    word_list = list(counts.items())
    word_list.sort(key = lambda x : x[1], reverse = True)
    return word_list
