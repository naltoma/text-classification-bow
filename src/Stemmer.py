import MeCab

def mecab_stemmer(datasets):
    mecab = MeCab.Tagger()

    stemmed_dataset = []
    for data in datasets:
        mecab.parse(data)
        node = mecab.parseToNode(data)
        temp = []
        while node:
            fs = node.feature.split(",")
            #print(fs)
            if fs[0] == '動詞':
                this_word = fs[7]
            else:
                this_word = node.surface
            if this_word not in ["", "*"]:
                temp.append(this_word)
            node = node.next
        stemmed_dataset.append(' '.join(temp))

    return stemmed_dataset
