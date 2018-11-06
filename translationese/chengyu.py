"""
chengyu (4-character idiom) as features for Chinese
We use normalized count of chengyu in each chunk as feature
"""

__author__ = 'Hai Hu'
__email__ = 'huhai@indiana.edu'

# from translationese.chengyu_list import CHENGYUS
from collections import Counter

VARIANTS = [0, 1, 2]
# 0: normalized counts for all chengyu in total
# 1: normalized counts for each chengyu

MY_CHENGYU = {
    "引人注目", "成千上万","无论如何","众所周知","有朝一日",
    "雄心勃勃","前所未有","自给自足","难以置信","无家可归"
}

def quantify_variant(analysis, variant):
    """ Quantify chengyu """
    if analysis.lang != 'zh':
        print('language "{}" not implemented for chengyu'.format(analysis.lang))
        exit()
    else:
        result = Counter(analysis.chengyus())
        # for chengyu in CHENGYUS:
        #     for sent in analysis.sentences():
        #         result[chengyu] = result.get(chengyu, 0) + sent.count(chengyu)
    n_tokens = len(analysis.tokens())

    if variant == 0:
        return { 'chengyu': sum(result.values()) / n_tokens }
    elif variant == 1:
        return { k : v / n_tokens for k, v in result.items() }
    elif variant == 2:
        return { k : v for k, v in result.items() if k in MY_CHENGYU}



