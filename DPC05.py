from itertools import combinations
from functools import reduce, partial
import enchant
import multiprocessing as mp


dicts = ["en_BW", "en_AU", "en_BZ", "en_GB", "en_JM", "en_DK", "en_HK", "en_GH", "en_US", "en_ZA", "en_ZW", "en_SG", "en_NZ", "en_BS", "en_AG", "en_PH", "en_IE", "en_NA", "en_TT", "en_IN", "en_NG", "en_CA"]

us = enchant.Dict("en_AU")

def split(word): 
    return list(word) 

def check(y, l):
    return enchant.Dict(l).check(y)

def checkwords(lang, n):
    print(lang + " Starting: ")
    all_comb = [*filter(partial(check, l = lang) , n)]
    comb = [x for x in n if x not in all_comb]
    print(lang + " - " + str(len(all_comb)) + ", " + str(len(comb)))
    return all_comb
      
# Driver code 
if __name__ == '__main__':
    word = "zieglersgiantbar"
    comb = []
    for i in range(1, 18):
        comb.append([*combinations(split(word), i )])

    comb = [*map(lambda x : [*map(lambda y: ' '.join(y).replace(" ", ""), x)], comb)]
    #    all_comb = reduce(lambda x, y: x + y, [x for x in [*map (lambda x : [*filter(check , x)], [*map(lambda x : [*map(lambda y: ' '.join(y).replace(" ", ""), x)], comb)])] if x])
    comb = reduce(lambda x, y: x + y, [x for x in comb if x])

    with mp.Pool(4) as p:
        words = p.map(partial(checkwords, n = comb), dicts)

    words = reduce(lambda x, y: x + y, [x for x in words if x])
    print("Total: " + str(len(list(set(words))))) 
