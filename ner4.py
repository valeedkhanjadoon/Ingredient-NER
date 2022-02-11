# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 21:58:45 2022

@author: vkjinx
"""

import spacy
import re

nlp = spacy.load("models/v2")
nlp0 = spacy.load("en_core_web_sm")

def ingId(string):
    
    stop_words = ['', 'start', 'select', 'serve','delicious', 'wrap', 'perfect', 'good', 'great', 'value', 'ingredient', 'breakfast', 'bite', 'variety', 'favorite', 'portion', 'house', 'made', 'hilltop', 'acre', 'plate', 'menu', 'website', 'list', 'up-to-date', 'gf', 'choice', 'local', 'piece', 'thick', 'thin', 'top', 'bottle', 'liter', 'per', 'person', 'can', 'cut', 'obtain', 'price']
    
    doc = nlp("aa, "+string.lower())

    lst = []
    for ent in doc.ents:
        # Remove punctations
        word = ''.join(e for e in ent.text if e.isalnum() or e.isspace() or e == '-')
        lst.append(word)
        # print(ent.text, ent.label_)
    
    # print("No Puncts: ",lst)

    foods = []
    for item in lst:
        doc0 = nlp0(item)
        tmp = ''
        for sent in doc0:
            # Remove articles
            if sent.pos_ in ["DET"]:
                continue
            # remove stop words and lemmatize
            elif sent.lemma_ not in stop_words:
                tmp = tmp+sent.lemma_+" "
        foods.append(tmp.strip())

    # print("\nNo Lemma : ",foods)

    f_lst = []
    # Remove duplicates in list
    for item in foods:
        if item == '':
            continue
        if item == 'fry':
            f_lst.append("fries")
        elif item not in f_lst:
            f_lst.append(item.strip())
    
    # sorted ingredient list
    final_list = sorted(f_lst)
    # convert list to string
    _str = ','.join(final_list)
    f_str = re.sub(' +', ' ', _str)
    # return string
    return f_str

result = ingId("Breaded fried chicken tossed in buffalo     sauce, red   onion, carrot, cucumber and tomato over mixed greens with bleu     cheese dressing")

print(result)