import jieba

def countWords(excludes, merges):
    txt = open('novels/sanguo.txt', 'r', encoding = 'utf-8').read()
    words = jieba.lcut(txt)
    counts = {}
    # 取出长度为一的词和符号以及excludes中的词
    for word in words:
        if len(word) == 1 or word in excludes:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    # 合并名称相同的人名
    for merge in merges:
        for name in merge[1]:
            counts[merge[0]] += counts.get(name, 0)
            del counts[name]
    word_list = list(counts.items())
    word_list.sort(key = lambda x : x[1], reverse = True)
    return word_list


excludes = {'却说','二人','不可','主公','陛下','汉中','只见','众将','后主','蜀兵','上马','大叫','太守','此人','夫人',
            '先主','后人','背后','城中','天子','一面','何不','大军','忽报','先生','百姓','何故','不能','如此','如何',
            '然后','先锋','不如','赶来','原来','令人','江东','下马','喊声','正是','徐州','忽然','荆州','左右','军马',
            '因此','成都','不见','未知','大败','大事','之后','一军','引军','起兵','军中','接应','引兵','次日','大喜',
            '进兵','大惊','可以','以为','大怒','不得','心中','下文','一声','追赶','粮草','天下','东吴','于是','都督',
            '曹兵','一齐','分解','回报','分付','只得','出马','三千','大将','许都','随后','报知','今日','不敢','魏兵',
            '前面','之兵','且说','众官','洛阳','领兵','商议','军士','星夜','精兵','城上','之计','不肯','相见','其言',
            '一日','而行','文武','襄阳','准备','若何','出战','亲自','必有','一人','人马','不知','何人','此事','之中',
            '伏兵','祁山','乘势','忽见','大笑','樊城','兄弟','首级','立于','西川','传令','当先','五百','一彪','坚守',
            '此时','之间','投降','五千','埋伏','长安','三路','遣使','将军','关兴','军师','朝廷','三军','大王','回见',
            '大将军','必然','将士','是夜','小路' }

merges = [  ('刘备',('玄德','玄德曰','玄德问','刘玄德','玄德大','玄德自','玄德闻','皇叔','刘皇叔')),
            ('关羽',('关公','云长','关云长')),
            ('孔明',('诸葛亮','孔明曰','孔明笑','孔明之','孔明自')),
            ('曹操',('丞相','孟德','曹公','曹孟德')),
            ('张飞',('翼德','张翼德'))
        ]



word_list = countWords(excludes, merges)
for i in range(30):
    word, count = word_list[i]
    print('{0:^10}{1:{3}^10}{2:^15}'.format(i+1, word, count, chr(12288))) # chr(12288)为中文空格
